#include <Python.h>

#include "ldapconnection.h"
#include "ldapentry.h"
#include "ldapvaluelist.h"
#include "ldapsearchiter.h"
#include "ldapmodlist.h"
#include "ldapconnectiter.h"
#include "utils.h"

PyObject *LDAPDNObj = NULL;

/* Get the vendor's name and version of the LDAP library. */
static PyObject *
bonsai_get_vendor_info(PyObject *self) {
    int rc = 0;
    LDAPAPIInfo info;

    info.ldapai_info_version = LDAP_API_INFO_VERSION;
    rc = ldap_get_option(NULL, LDAP_OPT_API_INFO, &info);
    if (rc != LDAP_SUCCESS) {
        PyErr_SetString(PyExc_Exception, "Failed to receive API info.");
        return NULL;
    }

    return Py_BuildValue("(s,i)", info.ldapai_vendor_name,
            info.ldapai_vendor_version);
}


/* Get the name of the underlying TLS library implementation. */
static PyObject *
bonsai_get_tls_impl_name(PyObject *self) {
    int rc = 0;
    char *package = NULL;

    rc = ldap_get_option(NULL, LDAP_OPT_X_TLS_PACKAGE, &package);
    if (rc != LDAP_SUCCESS || package == NULL) {
        PyErr_SetString(PyExc_Exception, "Failed to receive name of the"
                " TLS implementation.");
        return NULL;
    }

    return PyUnicode_FromString(package);
}

/* Check that the module is build with additional KRB5 support. */
static PyObject *
bonsai_has_krb5_support(PyObject *self) {
#if defined(HAVE_KRB5) || defined(WIN32)
    Py_RETURN_TRUE;
#else
    Py_RETURN_FALSE;
#endif
}

static void
bonsai_free(PyObject *self) {
    Py_DECREF(LDAPDNObj);
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyMethodDef bonsai_methods[] = {
    {"get_vendor_info", (PyCFunction)bonsai_get_vendor_info, METH_NOARGS,
        "Returns the vendor information of LDAP library."},
    {"get_tls_impl_name", (PyCFunction)bonsai_get_tls_impl_name, METH_NOARGS,
        "Returns the name of the underlying TLS implementation."},
    {"has_krb5_support", (PyCFunction)bonsai_has_krb5_support, METH_NOARGS,
        "Check that the module is build with additional Kerberos support."},
    {NULL, NULL, 0, NULL}  /* Sentinel */
};

static PyModuleDef bonsai2module = {
    PyModuleDef_HEAD_INIT,
    "_bonsai",
    "Python C extension for accessing directory servers using LDAP.",
    -1,
    bonsai_methods, NULL, NULL, NULL, (freefunc)bonsai_free
};

PyMODINIT_FUNC
PyInit__bonsai(void) {
    PyObject* module = NULL;

    /* Import LDAPDN object. */
    LDAPDNObj = load_python_object("bonsai.ldapdn", "LDAPDN");
    if (LDAPDNObj == NULL) return NULL;

    UniqueListType.tp_base = &PyList_Type;
    LDAPValueListType.tp_base = &UniqueListType;
    LDAPEntryType.tp_base = &PyDict_Type;

    if (PyType_Ready(&LDAPConnectionType) < 0) return NULL;
    if (PyType_Ready(&LDAPSearchIterType) < 0) return NULL;
    if (PyType_Ready(&LDAPConnectIterType) < 0) return NULL;
    if (PyType_Ready(&LDAPEntryType) < 0) return NULL;
    if (PyType_Ready(&LDAPValueListType) < 0) return NULL;
    if (PyType_Ready(&LDAPModListType) < 0) return NULL;

    module = PyModule_Create(&bonsai2module);
    if (module == NULL) return NULL;

    Py_INCREF(&LDAPEntryType);
    PyModule_AddObject(module, "ldapentry", (PyObject *)&LDAPEntryType);

    Py_INCREF(&LDAPConnectionType);
    PyModule_AddObject(module, "ldapconnection", (PyObject *)&LDAPConnectionType);

    Py_INCREF(&LDAPValueListType);
    PyModule_AddObject(module, "ldapvaluelist", (PyObject *)&LDAPValueListType);

    return module;
}
