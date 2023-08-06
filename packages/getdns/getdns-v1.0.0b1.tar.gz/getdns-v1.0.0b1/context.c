/*
 * Copyright (c) 2014, Versign, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 * * Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 * * Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution.
 * * Neither the name of the <organization> nor the
 * names of its contributors may be used to endorse or promote products
 * derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL Verisign, Include. BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <Python.h>
#include <getdns/getdns.h>
#include <getdns/getdns_extra.h>
#include <arpa/inet.h>
#include <sys/wait.h>
#include "pygetdns.h"

int
context_init(getdns_ContextObject *self, PyObject *args, PyObject *keywds)
{
    static char *kwlist[] = {
        "set_from_os",
        0
    };
    struct getdns_context *context = 0;
    int  set_from_os = 1;       /* default to True */
    getdns_return_t ret;
    PyObject *py_context;

    if (!PyArg_ParseTupleAndKeywords(args, keywds, "|i", kwlist,
                                     &set_from_os))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((set_from_os > 1) || (set_from_os < 0))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_create(&context, set_from_os)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    py_context = PyCapsule_New(context, "context", 0);
    Py_INCREF(py_context);
    self->py_context = py_context;
    return 0;
}


void
context_dealloc(getdns_ContextObject *self)
{
    getdns_context *context;
    int status;

    if ((context = PyCapsule_GetPointer(self->py_context, "context")) == NULL)  {
        return;
    }
    Py_XDECREF(self->py_context);
    getdns_context_destroy(context);
    (void)wait(&status);        /* reap the process spun off by unbound */
    return;
}


int
context_set_timeout(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    uint64_t value;
    
#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((long)(value = PyLong_AsLong(py_value)) < 0)  {
#else
    if ((long)(value = PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_timeout(context, value)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_idle_timeout(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    uint64_t value;
    
#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((long)(value = PyLong_AsLong(py_value)) < 0)  {
#else
    if ((long)(value = PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_idle_timeout(context, value)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_resolution_type(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    getdns_resolution_t value;
    
#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((long long)(value = (getdns_resolution_t)PyLong_AsLong(py_value)) < 0)  {
#else
    if ((long long)(value = (getdns_resolution_t)PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if (!((value == GETDNS_RESOLUTION_RECURSING) || (value == GETDNS_RESOLUTION_STUB)))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_resolution_type(context, value)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_limit_outstanding_queries(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    long value;
    
#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((value = PyLong_AsLong(py_value)) < 0)  {
#else
      if ((value = PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
      if ((ret = getdns_context_set_limit_outstanding_queries(context, (uint16_t) value)) !=
          GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_follow_redirects(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    uint64_t value;
    
#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((long)(value = PyLong_AsLong(py_value)) < 0)  {
#else
    if ((long)(value = PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if (!((value == GETDNS_REDIRECTS_FOLLOW) || (value == GETDNS_REDIRECTS_DO_NOT_FOLLOW)))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_follow_redirects(context, (getdns_redirects_t)value)) !=
        GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_append_name(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    uint64_t value;
    
#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((long)(value = PyLong_AsLong(py_value)) < 0)  {
#else
    if ((long)(value = PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if (!((value == GETDNS_APPEND_NAME_ALWAYS) ||
          (value == GETDNS_APPEND_NAME_ONLY_TO_SINGLE_LABEL_AFTER_FAILURE) ||
          (value == GETDNS_APPEND_NAME_ONLY_TO_MULTIPLE_LABEL_NAME_AFTER_FAILURE) ||
          (value == GETDNS_APPEND_NAME_NEVER)))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_append_name(context, (getdns_append_name_t)value)) !=
        GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_suffix(getdns_context *context, PyObject *py_value)
{
    getdns_list *values;
    getdns_return_t ret;
    Py_ssize_t len;
    PyObject *a_value;
    int i;

    if (!PyList_Check(py_value))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    len = PyList_Size(py_value);

    values = getdns_list_create();
    for (i = 0 ; i < len ; i++)  {
        getdns_bindata value;

        if ((a_value = PyList_GetItem(py_value, (Py_ssize_t)i)) != NULL)  {
#if PY_MAJOR_VERSION >= 3
            if (!PyUnicode_Check(a_value))  {
#else
            if (!PyString_Check(a_value))  {
#endif
                PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return -1;
            }
#if PY_MAJOR_VERSION >= 3
            value.data = (uint8_t *)strdup(PyBytes_AsString(PyUnicode_AsEncodedString(PyObject_Str(a_value), "ascii", NULL)));
#else
            value.data = (uint8_t *)strdup(PyString_AsString(a_value));
#endif
            value.size = strlen((char *)value.data);
            getdns_list_set_bindata(values, (size_t)i, &value);
        }  else  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return -1;
        }
    }
    if ((ret = getdns_context_set_suffix(context, values)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_dnssec_allowed_skew(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    uint32_t value;
    
#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((long)(value = (uint32_t)PyLong_AsLong(py_value)) < 0)  {
#else
    if ((long)(value = (uint32_t)PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_dnssec_allowed_skew(context, (uint32_t)value)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_edns_maximum_udp_payload_size(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    uint16_t value;
    
#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((long)(value = PyLong_AsLong(py_value)) < 0)  {
#else
    if ((long)(value = PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_edns_maximum_udp_payload_size(context, (uint16_t)value))
        != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_edns_extended_rcode(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    uint8_t value;
    
#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((value = (uint8_t)PyLong_AsLong(py_value)) < 0)  {
#else
    if ((value = (uint8_t)PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_edns_extended_rcode(context, (uint8_t)value))
        != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_tls_authentication(getdns_context *context, PyObject *py_value)  
{
    getdns_return_t ret;
    getdns_tls_authentication_t value;

#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((int)(value = (getdns_tls_authentication_t)PyLong_AsLong(py_value)) < 0)  {
#else
    if ((int)(value = (getdns_tls_authentication_t)PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_tls_authentication(context, value))
        != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


#if GETDNS_NUMERIC_VERSION > 0x00050000
int
context_set_tls_query_padding_blocksize(getdns_context *context, PyObject *py_value)  
{
    getdns_return_t ret;
    uint16_t value;

#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    } 
#if PY_MAJOR_VERSION >= 3
    if ((value = (uint16_t)PyLong_AsLong(py_value)) < 0)  {
#else
    if ((value = (uint16_t)PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_tls_query_padding_blocksize(context, value))
        != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}
#endif

#if GETDNS_NUMERIC_VERSION > 0x00050000
int
context_set_edns_client_subnet_private(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    uint8_t value;
    
#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((value = (uint8_t)PyLong_AsLong(py_value)) < 0)  {
#else
    if ((value = (uint8_t)PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if (! ((value == 0) || (value == 1)) )  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_edns_client_subnet_private(context, (uint8_t)value))
        != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}
#endif

int
context_set_edns_version(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    uint8_t value;
    
#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((value = (uint8_t)PyLong_AsLong(py_value)) < 0)  {
#else
    if ((value = (uint8_t)PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_edns_version(context, (uint8_t)value))
        != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_edns_do_bit(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    uint8_t value;

#if PY_MAJOR_VERSION >= 3
    if (!PyLong_Check(py_value))  {
#else
    if (!PyInt_Check(py_value))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
#if PY_MAJOR_VERSION >= 3
    if ((value = (uint8_t)PyLong_AsLong(py_value)) < 0)  {
#else
    if ((value = (uint8_t)PyInt_AsLong(py_value)) < 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if (!((value == 0) || (value == 1)))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((ret = getdns_context_set_edns_do_bit(context, (uint8_t)value))
        != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_namespaces(getdns_context *context, PyObject *py_value)
{
    size_t count;
    getdns_namespace_t *namespaces;
    getdns_return_t ret;
    int i;

    if (!PyList_Check(py_value))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((count = (int)PyList_Size(py_value)) == 0)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((namespaces = malloc(sizeof(getdns_namespace_t) * count)) == 0)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_MEMORY_ERROR_TEXT);
        return -1;
    }
    for (i = 0 ; i < count ; i++)  {
#if PY_MAJOR_VERSION >= 3
        namespaces[i] = (getdns_namespace_t)PyLong_AsLong(PyList_GetItem(py_value, (Py_ssize_t)i));
#else
        namespaces[i] = (getdns_namespace_t)PyInt_AsLong(PyList_GetItem(py_value, (Py_ssize_t)i));
#endif
        if ((namespaces[i] < GETDNS_NAMESPACE_DNS) || (namespaces[i] > GETDNS_NAMESPACE_NIS))  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return -1;
        }
    }
    if ((ret = getdns_context_set_namespaces(context, count, namespaces)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}        


int
context_set_dns_root_servers(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    getdns_list *addresses;
    Py_ssize_t len;
    int i;
    PyObject *an_address;
    PyObject *str;
    getdns_dict *addr_dict;
    int domain;
    unsigned char buf[sizeof(struct in6_addr)];

    if (!PyList_Check(py_value))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    len = PyList_Size(py_value);
    addresses = getdns_list_create();
    for (i = 0 ; i < len ; i++)  {
        getdns_bindata addr_data;
        getdns_bindata addr_type;

        if ((an_address = PyList_GetItem(py_value, (Py_ssize_t)i)) != NULL)  {
            if (PyDict_Size(an_address) != 2)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return -1;
            }
            addr_dict = getdns_dict_create();
            if ((str = PyDict_GetItemString(an_address, "address_type")) == NULL)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return -1;
            }
#if PY_MAJOR_VERSION >= 3
            if (!PyUnicode_Check(str))  {
#else
            if (!PyString_Check(str))  {
#endif
                PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return -1;
            }
#if PY_MAJOR_VERSION >= 3
            addr_type.data = (uint8_t *)strdup(PyBytes_AsString(PyUnicode_AsEncodedString(PyObject_Str(str), "ascii", NULL)));
#else
            addr_type.data = (uint8_t *)strdup(PyString_AsString(str));
#endif
            addr_type.size = strlen((char *)addr_type.data);
            if (strlen((char *)addr_type.data) != 4)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_WRONG_TYPE_REQUESTED_TEXT);
                return -1;
            }
            if (!strncasecmp((char *)addr_type.data, "IPv4", 4))
                domain = AF_INET;
            else if (!strncasecmp((char *)addr_type.data, "IPv6", 4))
                domain = AF_INET6;
            else  {
                PyErr_SetString(getdns_error,  GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return -1;
            }
            getdns_dict_set_bindata(addr_dict, "address_type", &addr_type);

            if ((str = PyDict_GetItemString(an_address, "address_data")) == NULL)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return -1;
            }
#if PY_MAJOR_VERSION >= 3
           if (!PyUnicode_Check(str))  {
#else 
           if (!PyString_Check(str))  {
#endif
                PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return -1;
            }
#if PY_MAJOR_VERSION >= 3
           if (inet_pton(domain, PyBytes_AsString(PyUnicode_AsEncodedString(PyObject_Str(str), "ascii", NULL)), buf) <= 0)  {
#else
            if (inet_pton(domain, PyString_AsString(str), buf) <= 0)  {
#endif
                PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return -1;
            }
            addr_data.data = (uint8_t *)buf;
            addr_data.size = (domain == AF_INET ? 4 : 16);
            getdns_dict_set_bindata(addr_dict, "address_data", &addr_data);
            getdns_list_set_dict(addresses, (size_t)i, addr_dict);
        }
    }
    if ((ret = getdns_context_set_dns_root_servers(context, addresses)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}
            

int
context_set_dnssec_trust_anchors(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    getdns_list *addresses;
    Py_ssize_t len;
    int i;
    PyObject *an_address;

    if (!PyList_Check(py_value))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    len = PyList_Size(py_value);
    addresses = getdns_list_create();
    for (i = 0 ; i < len ; i++)  {
        getdns_bindata *value = 0;

        if ((an_address = PyList_GetItem(py_value, (Py_ssize_t)i)) != NULL)  {
#if PY_MAJOR_VERSION >= 3
            if (!PyUnicode_Check(an_address))  {
#else
            if (!PyString_Check(an_address))  {
#endif
                PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return -1;
            }
#if PY_MAJOR_VERSION >= 3
            value->data = (uint8_t *)strdup(PyBytes_AsString(PyUnicode_AsEncodedString(PyObject_Str(py_value), "ascii", NULL)));
#else
            value->data = (uint8_t *)strdup(PyString_AsString(py_value));
#endif
            value->size = strlen((char *)value->data);
            getdns_list_set_bindata(addresses, (size_t)i, value);
        }  else  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return -1;
        }
    }
    if ((ret = getdns_context_set_dnssec_trust_anchors(context, addresses)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}


int
context_set_upstream_recursive_servers(getdns_context *context, PyObject *py_value)
{
    int  len;
    PyObject *py_upstream;
    struct getdns_list *upstream_list;
    int  i;
    getdns_return_t ret;

    if (!PyList_Check(py_value))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((len = (int)PyList_Size(py_value)) == 0)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
        
    upstream_list = getdns_list_create();
    for (i = 0 ; i < len ; i++)  {
        getdns_dict *a_upstream;

        if ((py_upstream = PyList_GetItem(py_value, (Py_ssize_t)i)) != NULL)  {
            if ((a_upstream = getdnsify_addressdict(py_upstream)) == NULL)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return -1;
            }
            if (getdns_list_set_dict(upstream_list, i, a_upstream) != GETDNS_RETURN_GOOD)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return -1;
            }
        }  else  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return -1;
        }
    }
    if ((ret = getdns_context_set_upstream_recursive_servers(context, upstream_list)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;

}


int
context_set_dns_transport_list(getdns_context *context, PyObject *py_value)
{
    getdns_return_t ret;
    Py_ssize_t len;
    getdns_transport_list_t *transports;
    int  i;

    if (!PyList_Check(py_value))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    len = PyList_Size(py_value);
    if ((transports = (getdns_transport_list_t *)malloc(sizeof(getdns_transport_list_t)*(int)len)) ==
        (getdns_transport_list_t *)0)  {
        PyErr_SetString(getdns_error, "memory allocation error");
        return -1;
    }
    for ( i = 0 ; i < (int)len ; i++ )  {
        PyObject *py_transport;
        long transport;
        if ((py_transport = PyList_GetItem(py_value, (Py_ssize_t)i)) != NULL)  {
            transport = PyLong_AsLong(py_transport);
            if ((transport < GETDNS_TRANSPORT_UDP) || (transport > GETDNS_TRANSPORT_TLS))  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return -1;
            }
            transports[i] = (getdns_transport_list_t)transport;
        }
        else  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return -1;
        }
    }
    if ((ret = getdns_context_set_dns_transport_list(context, (size_t)len, transports)) !=
        GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return -1;
    }
    return 0;
}
            

PyObject *
context_getattro(PyObject *self, PyObject *nameobj)
{
    getdns_ContextObject *myself = (getdns_ContextObject *)self;
    struct getdns_context *context;
    getdns_dict *api_info;
    getdns_dict *all_context;
    getdns_return_t ret;
    char *attrname;

#if PY_MAJOR_VERSION >= 3
    attrname = PyBytes_AsString(PyUnicode_AsEncodedString(PyObject_Str(nameobj), "ascii", NULL));
#else
    attrname = PyString_AsString(nameobj);
#endif
    context = PyCapsule_GetPointer(myself->py_context, "context");

    if (!strncmp(attrname, "append_name", strlen("append_name")))  {
        getdns_append_name_t value;
        if ((ret = getdns_context_get_append_name(context, &value)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)value);
    }

    if (!strncmp(attrname, "dns_root_servers", strlen("dns_root_servers")))  {
        PyObject *py_rootservers;
        getdns_list *dns_root_servers;
        if ((ret = getdns_context_get_dns_root_servers(context, &dns_root_servers)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        if (dns_root_servers == (getdns_list *)0)  {
           Py_RETURN_NONE;
        }
        else  {
        if ((py_rootservers = glist_to_plist(dns_root_servers)) == NULL)  {
            PyObject *err_type, *err_value, *err_traceback;
            PyErr_Fetch(&err_type, &err_value, &err_traceback);
            PyErr_Restore(err_type, err_value, err_traceback);
            return NULL;
        }
        return py_rootservers;
        }
    }

    if (!strncmp(attrname, "suffix", strlen("suffix")))  {
        PyObject *py_suffix;
        getdns_list *suffix;

        if ((ret = getdns_context_get_suffix(context, &suffix)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        if ((py_suffix = glist_to_plist(suffix)) == NULL)
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return py_suffix;
    }

    api_info = getdns_context_get_api_information(context);
    if (!strncmp(attrname, "resolution_type", strlen("resolution_type")))  {
        getdns_resolution_t value;
        if ((ret = getdns_context_get_resolution_type(context, &value)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)value);
    }
    if ((ret = getdns_dict_get_dict(api_info, "all_context", &all_context)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return NULL;
    }
    if (!strncmp(attrname, "implementation_string", strlen("implementation_string")))  {
        getdns_bindata *implementation_string;
        if ((ret = getdns_dict_get_bindata(api_info, "implementation_string", &implementation_string)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
#if PY_MAJOR_VERSION >= 3
        return PyUnicode_FromStringAndSize((char *)implementation_string->data,
                                           (Py_ssize_t)implementation_string->size);
#else
        return PyString_FromStringAndSize((char *)implementation_string->data,
                                          (Py_ssize_t)implementation_string->size);
#endif
    }
    if (!strncmp(attrname, "version_string", strlen("version_string")))  {
        getdns_bindata *version_string;
        if ((ret = getdns_dict_get_bindata(api_info, "version_string", &version_string)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
#if PY_MAJOR_VERSION >= 3
        return PyUnicode_FromStringAndSize((char *)version_string->data,
                                           (Py_ssize_t)version_string->size);
#else
        return PyString_FromStringAndSize((char *)version_string->data,
                                          (Py_ssize_t)version_string->size);
#endif
    }
        
    if (!strncmp(attrname, "timeout", strlen("timeout")))  {
        uint64_t value;
        if ((ret = getdns_context_get_timeout(context, &value)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)value);
    }
    if (!strncmp(attrname, "idle_timeout", strlen("idle_timeout")))  {
        uint64_t timeout;
        if ((ret = getdns_context_get_idle_timeout(context, &timeout)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)timeout);
    }
    if (!strncmp(attrname, "dns_transport_list", strlen("dns_transport_list")))  {
        getdns_transport_list_t *transports;
        PyObject *py_transports;
        size_t transport_count;
        int i;
        if ((ret = getdns_context_get_dns_transport_list(context, &transport_count, &transports)) != 
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        if ((py_transports = PyList_New((Py_ssize_t)transport_count)) == NULL)  {
            PyErr_SetString(getdns_error, "Could not create PyList");
            return NULL;
        }
        for ( i = 0 ; i < transport_count ; i++ )  {
            PyList_SetItem(py_transports, (Py_ssize_t)i, PyLong_FromLong((long)transports[i]));
        }
        return py_transports;
    }

    if (!strncmp(attrname, "limit_outstanding_queries", strlen("limit_outstanding_queries")))  {
        uint16_t value;
        if ((ret = getdns_context_get_limit_outstanding_queries(context, &value)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong(value);
    }

    if (!strncmp(attrname, "tls_query_padding_blocksize", strlen("tls_query_padding_blocksize")))  {
        uint16_t tls_query_padding_blocksize;
        if ((ret = getdns_context_get_tls_query_padding_blocksize(context, &tls_query_padding_blocksize)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)tls_query_padding_blocksize);
    }

    if (!strncmp(attrname, "edns_client_subnet_private", strlen("edns_client_subnet_private")))  {
        uint8_t edns_client_subnet_private;
        if ((ret = getdns_context_get_edns_client_subnet_private(context, &edns_client_subnet_private)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)edns_client_subnet_private);
    }

    if (!strncmp(attrname, "tls_authentication", strlen("tls_authentication")))  {
        getdns_tls_authentication_t value;
        if ((ret = getdns_context_get_tls_authentication(context, &value)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)value);
    }

    if (!strncmp(attrname, "follow_redirects", strlen("follow_redirects")))  {
        getdns_redirects_t value;
        if ((ret = getdns_context_get_follow_redirects(context, &value)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)value);
    }
    if (!strncmp(attrname, "dnssec_trust_anchors", strlen("dnssec_trust_anchors")))  {
        getdns_list *value;
        PyObject *py_trust_anchors;
        if ((ret = getdns_context_get_dnssec_trust_anchors(context, &value)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        py_trust_anchors = glist_to_plist(value);
        return(py_trust_anchors);
    }

    if (!strncmp(attrname, "dnssec_allowed_skew", strlen("dnssec_allowed_skew")))  {
        uint32_t value;
        if ((ret = getdns_context_get_dnssec_allowed_skew(context, &value)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)value);
    }
    if (!strncmp(attrname, "edns_maximum_udp_payload_size", strlen("edns_maximum_udp_payload_size")))  {
        uint16_t value;
        if ((ret = getdns_context_get_edns_maximum_udp_payload_size(context, &value)) != 
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)value);
    }
    if (!strncmp(attrname, "edns_extended_rcode", strlen("edns_extended_rcode")))  {
        uint8_t value;
        if ((ret = getdns_context_get_edns_extended_rcode(context, &value)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)value);
    }
    if (!strncmp(attrname, "edns_version", strlen("edns_version")))  {
        uint8_t value;
        if ((ret = getdns_context_get_edns_version(context, &value)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)value);
    }
    if (!strncmp(attrname, "edns_do_bit", strlen("edns_do_bit")))  {
        uint8_t value;
        if ((ret = getdns_context_get_edns_do_bit(context, &value)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return PyLong_FromLong((long)value);
    }

    if (!strncmp(attrname, "namespaces", strlen("namespaces")))  {
        PyObject *py_namespaces;
        getdns_namespace_t *namespaces;
        getdns_return_t ret;
        size_t count;
        int i;

        if ((ret = getdns_context_get_namespaces(context, &count, &namespaces)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        if (count)  {
            py_namespaces = PyList_New(count);
            for (i = 0 ; i < count ; i++)
                PyList_SetItem(py_namespaces, i, PyLong_FromLong((long)namespaces[i]));
            return py_namespaces;
        }  else
            Py_RETURN_NONE;
    }

    if (!strncmp(attrname, "upstream_recursive_servers", strlen("upstream_recursive_servers")))  {
        PyObject *py_upstream_servers;
        getdns_list *upstream_list;
        getdns_return_t ret;

        if ((ret = getdns_context_get_upstream_recursive_servers(context,
                                                                 &upstream_list)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        if ((py_upstream_servers = glist_to_plist(upstream_list)) == NULL)  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return NULL;
        }
        return py_upstream_servers;
    }

    if (!strncmp(attrname, "num_pending_requests", strlen("num_pending_requests")))  {
        uint32_t num_pending_requests;

        num_pending_requests = getdns_context_get_num_pending_requests(context, 0);
        return PyLong_FromLong((long)num_pending_requests);
    }


    return PyObject_GenericGetAttr((PyObject *)self, nameobj);
}

/*
 * must be in alphabetical order by attribute name.  attribute name and the
 * name of its setter function
 */

struct setter_table setters[] = {
    { "append_name", context_set_append_name },
    { "dnssec_allowed_skew", context_set_dnssec_allowed_skew },
    { "dns_root_servers", context_set_dns_root_servers },
    { "dns_transport_list", context_set_dns_transport_list },
    { "edns_client_subnet_private", context_set_edns_client_subnet_private },
    { "edns_do_bit", context_set_edns_do_bit },
    { "edns_extended_rcode", context_set_edns_extended_rcode },
    { "edns_maximum_udp_payload_size", context_set_edns_maximum_udp_payload_size },
    { "edns_version", context_set_edns_version },
    { "idle_timeout", context_set_idle_timeout },
    { "follow_redirects", context_set_follow_redirects },
    { "limit_outstanding_queries", context_set_limit_outstanding_queries },
    { "namespaces", context_set_namespaces },
    { "resolution_type", context_set_resolution_type },
    { "suffix", context_set_suffix },
    { "timeout", context_set_timeout },
    { "tls_authentication", context_set_tls_authentication },
    { "tls_query_padding_blocksize", context_set_tls_query_padding_blocksize },
    { "upstream_recursive_servers", context_set_upstream_recursive_servers },
};

#define NSETTERS  (sizeof(setters) / sizeof(setters[0]))
static int
compare_setters(const void *key, const void *entry)
{
    struct setter_table *s1 = (struct setter_table *)key;
    struct setter_table *s2 = (struct setter_table *)entry;

    return strcmp(s1->name, s2->name);
}


int
context_setattro(PyObject *self, PyObject *attrname, PyObject *py_value)
{
    getdns_ContextObject *myself = (getdns_ContextObject *)self;
    struct getdns_context *context;
    char *name;
    struct setter_table key;
    struct setter_table *setter;

#if PY_MAJOR_VERSION >= 3
    name = PyBytes_AsString(PyUnicode_AsEncodedString(PyObject_Str(attrname), "ascii", NULL));
#else
    name = PyString_AsString(attrname);
#endif
    key.name = name;
    if ((context = PyCapsule_GetPointer(myself->py_context, "context")) == NULL)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return -1;
    }
    if ((setter = bsearch(&key, setters, NSETTERS, sizeof(struct setter_table),
                          compare_setters)) != NULL)
        return setter->setter(context, py_value);
/*
 *  if it's not an attribute we define, throw an error.  The
 *    tradeoff is between ease of use and extensibility, and
 *    given that people are getting attribute names wrong this
 *    is worth trying.  Back it out if there are complaints
 */

    PyErr_SetString(PyExc_AttributeError, "No such attribute");
    return -1;
}


PyObject *
context_get_attributes(getdns_ContextObject *self, PyObject *unused)
{
    int i;
    PyObject *py_attr_list = PyList_New(NSETTERS);

    for (i = 0 ; i < NSETTERS ; i++)  {
#if PY_MAJOR_VERSION >= 3
        (void)PyList_SetItem(py_attr_list, (Py_ssize_t) i, PyUnicode_FromString(setters[i].name));        
#else
        (void)PyList_SetItem(py_attr_list, (Py_ssize_t) i, PyString_FromString(setters[i].name));
#endif
    }
    return py_attr_list;
}


PyObject *
context_run(getdns_ContextObject *self, PyObject *args, PyObject *keywds)
{
    getdns_context *context;

    if ((context = PyCapsule_GetPointer(self->py_context, "context")) == NULL)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_BAD_CONTEXT_TEXT);
        return NULL;
    }
    getdns_context_run(context);
    Py_RETURN_NONE;
}


PyObject *
context_cancel_callback(getdns_ContextObject *self, PyObject *args, PyObject *keywds)
{
    static char *kwlist[] = {
        "transaction_id",
        0
    };
    getdns_context *context;
    getdns_transaction_t tid = 0;
    getdns_return_t ret;

    if ((context = PyCapsule_GetPointer(self->py_context, "context")) == NULL)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_BAD_CONTEXT_TEXT);
        return NULL;
    }
    if (!PyArg_ParseTupleAndKeywords(args, keywds, "L", kwlist, &tid))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return NULL;
    }
    if ((ret = getdns_cancel_callback(context, tid)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return NULL;
    }
    Py_RETURN_NONE;
}
    

PyObject *
context_str(PyObject *self)
{
    getdns_ContextObject *myself = (getdns_ContextObject *)self;
    struct getdns_context *context;
    getdns_dict *api_info;
    char *str_api_dict;

    context = PyCapsule_GetPointer(myself->py_context, "context");
    api_info = getdns_context_get_api_information(context);
    if ((str_api_dict = getdns_print_json_dict(api_info, 0)) == NULL)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
        return NULL;
    }
#if PY_MAJOR_VERSION >= 3
    return(PyUnicode_FromString(str_api_dict));    
#else
    return(PyString_FromString(str_api_dict));    
#endif
}


PyObject *
context_general(getdns_ContextObject *self, PyObject *args, PyObject *keywds)
{
    static char *kwlist[] = {
        "name",
        "request_type",
        "extensions",
        "userarg",
        "transaction_id",
        "callback",
        0
    };
    getdns_context *context;
    char *name;
    uint16_t  request_type;
    PyDictObject *extensions_obj = 0;
    struct getdns_dict *extensions_dict = 0;
    getdns_return_t ret;
    void *userarg = 0;
    getdns_transaction_t tid = 0;
    PyObject *callback = 0;
    struct getdns_dict *resp;
    PyObject *callback_func;

    if ((context = PyCapsule_GetPointer(self->py_context, "context")) == NULL)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_BAD_CONTEXT_TEXT);
        return NULL;
    }
    if (!PyArg_ParseTupleAndKeywords(args, keywds, "sH|OsLO", kwlist,
                                     &name, &request_type,
                                     &extensions_obj, &userarg, &tid, &callback))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return NULL;
    }
    if (extensions_obj)  {
        if ((extensions_dict = extensions_to_getdnsdict(extensions_obj)) == 0)  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return NULL;
        }
    }
    if (callback)  {
        userarg_blob *blob;

        if ((blob = (userarg_blob *)malloc(sizeof(userarg_blob))) == (userarg_blob *)0)  {
            PyErr_SetString(getdns_error, "Memory allocation failed");
            return NULL;
        }
        if (userarg)  
            strncpy(blob->userarg, userarg, BUFSIZ-1);
#if PY_MAJOR_VERSION >= 3
        if (PyUnicode_Check(callback))  {
            if ((callback_func = get_callback("__main__", PyBytes_AsString(PyUnicode_AsEncodedString(PyObject_Str(callback), "ascii", NULL)))) == (PyObject *)NULL)  {
#else
        if (PyString_Check(callback))  {
            if ((callback_func = get_callback("__main__", PyString_AsString(callback))) == (PyObject *)NULL)  {
#endif
                PyObject *err_type, *err_value, *err_traceback;
                PyErr_Fetch(&err_type, &err_value, &err_traceback);
                PyErr_Restore(err_type, err_value, err_traceback);
                return NULL;
            }
            blob->callback_func = callback_func;
        }  else if (PyCallable_Check(callback))  {
            blob->callback_func = callback;
        }  else  {
            PyErr_SetString(getdns_error, "Invalid callback value");
            return NULL;
        }

        if ((ret = getdns_general(context, name, request_type,
                                  extensions_dict, (void *)blob, &tid, callback_shim)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
#if PY_MAJOR_VERSION >= 3
        return(PyLong_FromUnsignedLong((long)tid));
#else
        return(PyInt_FromLong((long)tid));
#endif
    } else  {
        if ((ret = getdns_general_sync(context, name, request_type,
                                       extensions_dict, &resp)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return result_create(resp);
    }
}


PyObject *
context_address(getdns_ContextObject *self, PyObject *args, PyObject *keywds)
{
    static char *kwlist[] = {
        "name",
        "extensions",
        "userarg",
        "transaction_id",
        "callback",
        0
    };
    getdns_return_t ret;
    getdns_context *context;
    char *name;
    PyObject *callback_func;
    PyDictObject *extensions_obj = 0;
    struct getdns_dict *extensions_dict = 0;
    char *userarg = 0;
    getdns_transaction_t tid;
    PyObject *callback = 0;
    struct getdns_dict *resp;

    if ((context = PyCapsule_GetPointer(self->py_context, "context")) == NULL)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_BAD_CONTEXT_TEXT);
        return NULL;
    }
    if (!PyArg_ParseTupleAndKeywords(args, keywds, "s|OsLO", kwlist,
                                     &name, 
                                     &extensions_obj, &userarg, &tid, &callback))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return NULL;
    }
    if (extensions_obj)  {
        if ((extensions_dict = extensions_to_getdnsdict(extensions_obj)) == 0)  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return NULL;
        }
    }
    if (callback)  {
        userarg_blob *blob;

        if ((blob = (userarg_blob *)malloc(sizeof(userarg_blob))) == (userarg_blob *)0)  {
            PyErr_SetString(getdns_error, "Memory allocation failed");
            return NULL;
        }
        if (userarg)  {
            strncpy(blob->userarg, userarg, BUFSIZ-1);
        }  else  {
            blob->userarg[0] = 0;
        }
#if PY_MAJOR_VERSION >= 3
        if (PyUnicode_Check(callback))  {
            if ((callback_func = get_callback("__main__", PyBytes_AsString(PyUnicode_AsEncodedString(PyObject_Str(callback), "ascii", NULL)))) == (PyObject *)NULL)  {
#else
                   if (PyString_Check(callback))  {
            if ((callback_func = get_callback("__main__", PyString_AsString(callback))) == (PyObject *)NULL)  {
#endif
                PyObject *err_type, *err_value, *err_traceback;
                PyErr_Fetch(&err_type, &err_value, &err_traceback);
                PyErr_Restore(err_type, err_value, err_traceback);
                return NULL;
            }
            blob->callback_func = callback_func;
        }  else if (PyCallable_Check(callback))  {
            blob->callback_func = callback;
        }  else  {
            PyErr_SetString(getdns_error, "Invalid callback value");
            return NULL;
        }
                                      
        if ((ret = getdns_address(context, name, extensions_dict, (void *)blob, &tid, callback_shim)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
#if PY_MAJOR_VERSION >= 3
        return(PyLong_FromUnsignedLong((long)tid));
#else
        return(PyInt_FromLong((long)tid));
#endif
    } else  {
        if ((ret = getdns_address_sync(context, name, extensions_dict, &resp)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return result_create(resp);
    }
}


PyObject *
context_hostname(getdns_ContextObject *self, PyObject *args, PyObject *keywds)
{
    static char *kwlist[] = {
        "address",
        "extensions",
        "userarg",
        "transaction_id",
        "callback",
        0
    };
    void *address;
    PyDictObject *extensions_obj = 0;
    struct getdns_dict *extensions_dict = 0;
    void *userarg = 0;
    getdns_transaction_t tid;
    PyObject* callback = 0;
    struct getdns_dict *resp;
    getdns_context *context;
    struct getdns_dict *addr_dict;
    getdns_return_t ret;
    PyObject *callback_func;

    if ((context = PyCapsule_GetPointer(self->py_context, "context")) == NULL)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_BAD_CONTEXT_TEXT);
        return NULL;
    }
    if (!PyArg_ParseTupleAndKeywords(args, keywds, "O|OsLO", kwlist,
                                     &address, 
                                     &extensions_obj, &userarg, &tid, &callback))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return NULL; 
    }
    if (extensions_obj)  {
        if ((extensions_dict = extensions_to_getdnsdict(extensions_obj)) == 0)  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return NULL;
        }
    }
    if ((addr_dict = getdnsify_addressdict((PyObject *)address)) == NULL)  {
        PyObject *err_type, *err_value, *err_traceback;
        PyErr_Fetch(&err_type, &err_value, &err_traceback);
        PyErr_Restore(err_type, err_value, err_traceback);
        return NULL;
    }
    if (callback)  {
        userarg_blob *blob;

        if ((blob = (userarg_blob *)malloc(sizeof(userarg_blob))) == (userarg_blob *)0)  {
            PyErr_SetString(getdns_error, "Memory allocation failed");
            return NULL;
        }
        if (userarg)  {
            strncpy(blob->userarg, userarg, BUFSIZ-1);
        }  else  {
            blob->userarg[0] = 0;
        }
#if PY_MAJOR_VERSION >= 3
        if (PyUnicode_Check(callback))  {
            if ((callback_func = get_callback("__main__", PyBytes_AsString(PyUnicode_AsEncodedString(PyObject_Str(callback), "ascii", NULL)))) == (PyObject *)NULL)  {
#else
        if (PyString_Check(callback))  {
            if ((callback_func = get_callback("__main__", PyString_AsString(callback))) == (PyObject *)NULL)  {
#endif
                PyObject *err_type, *err_value, *err_traceback;
                PyErr_Fetch(&err_type, &err_value, &err_traceback);
                PyErr_Restore(err_type, err_value, err_traceback);
                return NULL;
            }
            blob->callback_func = callback_func;
        }  else if (PyCallable_Check(callback))  {
            blob->callback_func = callback;
        }  else  {
            PyErr_SetString(getdns_error, "Invalid callback value");
            return NULL;
        }

        if ((ret = getdns_hostname(context, addr_dict, extensions_dict, (void *)blob, &tid, callback_shim)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
#if PY_MAJOR_VERSION >= 3
        return(PyLong_FromUnsignedLong((long)tid));
#else
        return(PyInt_FromLong((long)tid));
#endif
    } else  {
        if ((ret = getdns_hostname_sync(context, addr_dict, extensions_dict, &resp)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return result_create(resp);
    }
}


PyObject *
context_service(getdns_ContextObject *self, PyObject *args, PyObject *keywds)
{
    static char *kwlist[] = {
        "name",
        "extensions",
        "userarg",
        "transaction_id",
        "callback",
        0
    };
    char *name;
    PyDictObject *extensions_obj = 0;
    struct getdns_dict *extensions_dict = 0;
    getdns_return_t ret;
    void *userarg;
    getdns_transaction_t tid;
    PyObject *callback = 0;
    struct getdns_dict *resp;
    getdns_context *context;
    PyObject *callback_func;

    if ((context = PyCapsule_GetPointer(self->py_context, "context")) == NULL)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_BAD_CONTEXT_TEXT);
        return NULL;
    }
    if (!PyArg_ParseTupleAndKeywords(args, keywds, "s|OsLO", kwlist,
                                     &name, 
                                     &extensions_obj, &userarg, &tid, &callback))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return NULL;            
    }
    if (extensions_obj)  {
        if ((extensions_dict = extensions_to_getdnsdict(extensions_obj)) == 0)  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return NULL;
        }
    }
    if (callback)  {
        userarg_blob *blob;

        if ((blob = (userarg_blob *)malloc(sizeof(userarg_blob))) == (userarg_blob *)0)  {
            PyErr_SetString(getdns_error, "Memory allocation failed");
            return NULL;
        }
        if (userarg)  {
            strncpy(blob->userarg, userarg, BUFSIZ-1);
        }  else  {
            blob->userarg[0] = 0;
        }
#if PY_MAJOR_VERSION >= 3
        if (PyUnicode_Check(callback))  {
            if ((callback_func = get_callback("__main__", PyBytes_AsString(PyUnicode_AsEncodedString(PyObject_Str(callback), "ascii", NULL)))) == (PyObject *)NULL)  {
#else
        if (PyString_Check(callback))  {
            if ((callback_func = get_callback("__main__", PyString_AsString(callback))) == (PyObject *)NULL)  {
#endif
                PyObject *err_type, *err_value, *err_traceback;
                PyErr_Fetch(&err_type, &err_value, &err_traceback);
                PyErr_Restore(err_type, err_value, err_traceback);
                return NULL;
            }
            blob->callback_func = callback_func;
        }  else if (PyCallable_Check(callback))  {
            blob->callback_func = callback;
        }  else  {
            PyErr_SetString(getdns_error, "Invalid callback value");
            return NULL;
        }

        if ((ret = getdns_service(context, name, extensions_dict, (void *)blob, &tid, callback_shim)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
#if PY_MAJOR_VERSION >= 3
        return(PyLong_FromUnsignedLong((long)tid));
#else
        return(PyInt_FromLong((long)tid));
#endif
    } else  {
        if ((ret = getdns_service_sync(context, name, extensions_dict, &resp)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        return result_create(resp);
    }
}


PyObject *
context_get_api_information(getdns_ContextObject *self, PyObject *unused)
{
    getdns_context *context;
    getdns_dict *api_info;
    PyObject *py_api;
    getdns_bindata *version_string;
    getdns_bindata *imp_string;
    uint32_t resolution_type;
    getdns_dict *all_context;
    PyObject *py_all_context;
    getdns_return_t ret;


    if ((context = PyCapsule_GetPointer(self->py_context, "context")) == NULL)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_BAD_CONTEXT_TEXT);
        return NULL;
    }
    py_api = PyDict_New();
    api_info = getdns_context_get_api_information(context);
    if ((ret = getdns_dict_get_bindata(api_info, "version_string", &version_string)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return NULL;
    }
#if PY_MAJOR_VERSION >= 3
    if (PyDict_SetItemString(py_api, "version_string",
                             PyUnicode_FromStringAndSize((char *)version_string->data,
                                                         (Py_ssize_t)version_string->size)))  {
#else
    if (PyDict_SetItemString(py_api, "version_string",
                             PyString_FromStringAndSize((char *)version_string->data,
                                                        (Py_ssize_t)version_string->size)))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
        return NULL;
    }
    if ((ret = getdns_dict_get_bindata(api_info, "implementation_string", &imp_string)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return NULL;
    }
#if PY_MAJOR_VERSION >= 3
    if (PyDict_SetItemString(py_api, "implementation_string",
                             PyUnicode_FromStringAndSize((char *)imp_string->data,
                                                         (Py_ssize_t)imp_string->size)))  {
#else
    if (PyDict_SetItemString(py_api, "implementation_string",
                             PyString_FromStringAndSize((char *)imp_string->data,
                                                        (Py_ssize_t)imp_string->size)))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
        return NULL;
    }
    if ((ret = getdns_dict_get_int(api_info, "resolution_type", &resolution_type)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return NULL;
    }
#if PY_MAJOR_VERSION >= 3
    if (PyDict_SetItemString(py_api, "resolution_type", PyLong_FromLong((long)resolution_type)))  {
#else
    if (PyDict_SetItemString(py_api, "resolution_type", PyInt_FromLong((long)resolution_type)))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
        return NULL;
    }
    if ((ret = getdns_dict_get_dict(api_info, "all_context", &all_context)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return NULL;
    }
    if ((py_all_context = gdict_to_pdict(all_context)) == NULL)  {
        PyErr_SetString(getdns_error, "Unable to convert all_context dict");
        return NULL;
    }
    PyDict_SetItemString(py_api, "all_context", py_all_context);
    return(py_api);
}        
