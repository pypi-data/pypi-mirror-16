/*
 * \ file pygetdns_util.c
 * @brief utility functions to support pygetdns bindings
 */


/*
 * Copyright (c) 2014, Verisign, Inc.
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
#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <getdns/getdns.h>
#include <getdns/getdns_extra.h>
#include "pygetdns.h"



int
get_status(struct getdns_dict *result_dict)
{
    uint32_t status;
    getdns_return_t ret;

    if ((ret = getdns_dict_get_int(result_dict, "status", &status)) != GETDNS_RETURN_GOOD)
        return 0;
    return (int)status;
}
        

int
get_answer_type(struct getdns_dict *result_dict)
{
    uint32_t answer_type;
    getdns_return_t ret;

    if ((ret = getdns_dict_get_int(result_dict, "answer_type", &answer_type)) != GETDNS_RETURN_GOOD)
        return 0;
    return (int)answer_type;
}


char *
get_canonical_name(struct getdns_dict *result_dict)
{
    getdns_bindata *canonical_name;
    getdns_return_t ret;

    if ((ret = getdns_dict_get_bindata(result_dict, "canonical_name", &canonical_name)) == GETDNS_RETURN_GOOD)  {
        char *dname = 0;
        if (getdns_convert_dns_name_to_fqdn(canonical_name, &dname) == GETDNS_RETURN_GOOD)
            return dname;
        else
            return (char *)canonical_name->data;
    }  else
        return 0;
}
        

PyObject *
get_just_address_answers(struct getdns_dict *result_dict)
{
    struct getdns_list *just_address_answers;
    getdns_return_t ret;

    if ((ret = getdns_dict_get_list(result_dict, "just_address_answers", &just_address_answers)) !=
        GETDNS_RETURN_GOOD)
        return NULL;
    return pythonify_address_list(just_address_answers);
}


PyObject *
get_replies_tree(struct getdns_dict *result_dict)
{
    struct getdns_list *replies_tree;
    getdns_return_t ret;

    if ((ret = getdns_dict_get_list(result_dict, "replies_tree", &replies_tree)) !=
        GETDNS_RETURN_GOOD)
        return NULL;
    return glist_to_plist(replies_tree);
}


PyObject *
get_validation_chain(struct getdns_dict *result_dict)
{
    struct getdns_list *validation_chain;
    getdns_return_t ret;

    if ((ret = getdns_dict_get_list(result_dict, "validation_chain", &validation_chain)) !=
        GETDNS_RETURN_GOOD)
        Py_RETURN_NONE;
    else
        return glist_to_plist(validation_chain);
}


#if GETDNS_NUMERIC_VERSION < 0x00090000
PyObject *
get_call_debugging(struct getdns_dict *result_dict)
#else
PyObject *
get_call_reporting(struct getdns_dict *result_dict)
#endif
{
#if GETDNS_NUMERIC_VERSION < 0x00090000
    struct getdns_list *call_debugging;
#else
    struct getdns_list *call_reporting;
#endif
    getdns_return_t ret;


#if GETDNS_NUMERIC_VERSION < 0x00090000
    if ((ret = getdns_dict_get_list(result_dict, "call_debugging", &call_debugging)) !=
#else
    if ((ret = getdns_dict_get_list(result_dict, "call_reporting", &call_reporting)) !=
#endif
        GETDNS_RETURN_GOOD)
        Py_RETURN_NONE;
    else
#if GETDNS_NUMERIC_VERSION < 0x00090000
        return glist_to_plist(call_debugging);
#else
        return glist_to_plist(call_reporting);
#endif
}

struct getdns_dict *
extensions_to_getdnsdict(PyDictObject *pydict)
{
    struct getdns_dict *newdict = 0;
    Py_ssize_t pos = 0, optiondictpos = 0, optionlistpos = 0;
    PyObject *key, *value;
    char *tmpoptionlistkey;
    struct getdns_list *optionslist = 0;         /* for options list */
    int optionlistsize;                   /* how many options in options list */
    int i;                                /* loop counter */
    PyObject *optionitem;
    PyObject *optiondictkey, *optiondictvalue; /* for processing option list dicts */
    struct getdns_bindata *option_data;
    struct getdns_dict *tmpoptions_list_dict; /* a dict to hold add_opt_parameters[options] stuff */

    if ((!pydict) || (!PyDict_Check(pydict)))  {
        PyErr_SetString(getdns_error, "Expected dict, didn't get one");
        return NULL;
    }
    newdict = getdns_dict_create(); /* this is what we'll return */

    while (PyDict_Next((PyObject *)pydict, &pos, &key, &value))  { /* these options take TRUE or FALSE args */
        char *tmp_key;
        int  tmp_int;

#if PY_MAJOR_VERSION >= 3
        tmp_key = PyBytes_AsString(PyUnicode_AsEncodedString(PyObject_Str(key), "ascii", NULL));
#else
        tmp_key = PyString_AsString(PyObject_Str(key));
#endif
        if ( (!strncmp(tmp_key, "dnssec_return_status", strlen("dnssec_return_status")))  ||
             (!strncmp(tmp_key, "dnssec_return_all_statuses", strlen("dnssec_return_all_statuses"))) ||
             (!strncmp(tmp_key, "dnssec_return_only_secure", strlen("dnssec_return_only_secure")))  ||
             (!strncmp(tmp_key, "dnssec_return_validation_chain", strlen("dnssec_return_validation_chain")))  ||
             (!strncmp(tmp_key, "return_both_v4_and_v6", strlen("return_both_v4_and_v6")))  ||
             (!strncmp(tmp_key, "return_api_information", strlen("return_api_information")))  ||
#if GETDNS_NUMERIC_VERSION < 0x00090000
             (!strncmp(tmp_key, "return_call_debugging", strlen("return_call_debugging")))  ||
#else
             (!strncmp(tmp_key, "return_call_reporting", strlen("return_call_reporting")))  ||
#endif
             (!strncmp(tmp_key, "add_warning_for_bad_dns", strlen("add_warning_for_bad_dns"))) )  {
#if PY_MAJOR_VERSION >= 3
            if (!PyLong_Check(value))  {
#else
            if (!PyInt_Check(value))  {
#endif
                PyErr_SetString(getdns_error, GETDNS_RETURN_EXTENSION_MISFORMAT_TEXT);
                return NULL;
            }
#if PY_MAJOR_VERSION >= 3
            if ( !((PyLong_AsLong(value) == GETDNS_EXTENSION_TRUE) || (PyLong_AsLong(value) == GETDNS_EXTENSION_FALSE)) )  {
#else
            if ( !((PyInt_AsLong(value) == GETDNS_EXTENSION_TRUE) || (PyInt_AsLong(value) == GETDNS_EXTENSION_FALSE)) )  {
#endif
                PyErr_SetString(getdns_error, GETDNS_RETURN_EXTENSION_MISFORMAT_TEXT);
                return NULL;
            }
#if PY_MAJOR_VERSION >= 3
            tmp_int = (int)PyLong_AsLong(value);
#else
            tmp_int = (int)PyInt_AsLong(value);
#endif
            (void)getdns_dict_set_int(newdict, tmp_key, tmp_int);
        } else if (!strncmp(tmp_key, "specify_class", strlen("specify_class")))  { /* takes integer */
#if PY_MAJOR_VERSION >= 3
            if (!PyLong_Check(value))  {
#else
            if (!PyInt_Check(value))  {
#endif
                PyErr_SetString(getdns_error, GETDNS_RETURN_EXTENSION_MISFORMAT_TEXT);
                return NULL;
            }
#if PY_MAJOR_VERSION >= 3
            tmp_int = (int)PyLong_AsLong(value);
#else
            tmp_int = (int)PyInt_AsLong(value);
#endif
            (void)getdns_dict_set_int(newdict, tmp_key, tmp_int);

/*
 *  dns OPT resource record setup
 *
 *    extensions['add_opt_parameters'][option_name]
 */


        } else if (!strncmp(tmp_key, "add_opt_parameters", strlen("add_opt_parameters")))  { /* this is a dict */
            PyObject *in_optdict; /* points at dictionary passed in */
            struct getdns_dict *out_optdict = 0;
            Py_ssize_t opt_pos = 0;
            PyObject *opt_key, *opt_value;
            char *tmp_opt_key;
            int optint;

            in_optdict = value;
            if (!PyDict_Check(in_optdict))  {
                PyErr_SetString(getdns_error, "Expected dict, didn't get one");
                return NULL;
            }
            out_optdict = getdns_dict_create();
            while (PyDict_Next((PyObject *)in_optdict, &opt_pos, &opt_key, &opt_value))  {
#if PY_MAJOR_VERSION >= 3
                tmp_opt_key = PyBytes_AsString(PyUnicode_AsEncodedString(opt_key, "ascii", NULL));
#else
                tmp_opt_key = PyString_AsString(opt_key);
#endif
                if ( (!strncmp(tmp_opt_key, "maximum_udp_payload_size", strlen("maximum_udp_payload_size")))  ||
                     (!strncmp(tmp_opt_key, "extended_rcode", strlen("extended_rcode"))) ||
                     (!strncmp(tmp_opt_key, "version", strlen("version"))) ||
                     (!strncmp(tmp_opt_key, "do_bit", strlen("do_bit"))) )  {
#if PY_MAJOR_VERSION >= 3
                    if (!PyLong_Check(opt_value))  {
#else
                    if (!PyInt_Check(opt_value))  {
#endif
                        PyErr_SetString(getdns_error, GETDNS_RETURN_EXTENSION_MISFORMAT_TEXT);
                        return NULL;
                    }
#if PY_MAJOR_VERSION >= 3
                    optint = (int)PyLong_AsLong(opt_value);
#else
                    optint = (int)PyInt_AsLong(opt_value);
#endif
                    (void)getdns_dict_set_int(out_optdict, tmp_opt_key, optint);
                }  else if (!strncmp(tmp_opt_key, "options", strlen("options")))  { /* options */
/*
 * options with arbitrary opt code
 *
 *    add_opt_parameters is a dict containing
 *      options is a list containing
 *        dicts for each option containing
 *          option_code (int)
 *          option_data (bindata)
 *    
 */

                    if (!PyList_Check(opt_value))  {
                        PyErr_SetString(getdns_error, GETDNS_RETURN_EXTENSION_MISFORMAT_TEXT);
                        return NULL;
                    }
                    optionslist = getdns_list_create();

                    optionlistsize = (int)PyList_Size(opt_value);

                    for ( i = 0 ; i < optionlistsize ; i++)  {
                        tmpoptions_list_dict = getdns_dict_create();
                        optionitem = PyList_GetItem(opt_value, i);
                        if (!PyDict_Check(optionitem))  {
                            PyErr_SetString(getdns_error, GETDNS_RETURN_EXTENSION_MISFORMAT_TEXT);
                            return NULL;
                        }
                        /* optionitem should be a dict with keys option_code and option_data */
                        while (PyDict_Next(optionitem, &optiondictpos, &optiondictkey, &optiondictvalue))  {
#if PY_MAJOR_VERSION >= 3
                            tmpoptionlistkey = PyBytes_AsString(PyUnicode_AsEncodedString(PyObject_Str(optiondictkey),
                                                                                          "ascii", NULL)); /* XXX */
#else
                            tmpoptionlistkey = PyString_AsString(PyObject_Str(optiondictkey));
#endif
                            if  (!strncmp(tmpoptionlistkey, "option_code", strlen("option_code")))  {
#if PY_MAJOR_VERSION >= 3
                                if (!PyLong_Check(optiondictvalue))  {
#else
                                if (!PyInt_Check(optiondictvalue))  {
#endif
                                    PyErr_SetString(getdns_error, GETDNS_RETURN_EXTENSION_MISFORMAT_TEXT);
                                    return NULL;
                                }
#if PY_MAJOR_VERSION >= 3
                                getdns_dict_set_int(tmpoptions_list_dict, "option_code", (uint32_t)PyLong_AsLong(optiondictvalue));
#else
                                getdns_dict_set_int(tmpoptions_list_dict, "option_code", (uint32_t)PyInt_AsLong(optiondictvalue));
#endif
                            }  else if (!strncmp(tmpoptionlistkey, "option_data", strlen("option_data")))  {
                                option_data = (struct getdns_bindata *)malloc(sizeof(struct getdns_bindata));
                                option_data->size = PyObject_Length(optiondictvalue);
#if PY_MAJOR_VERSION >= 3
                                option_data->data = (uint8_t *)PyBytes_AS_STRING(optiondictvalue);
#else
                                option_data->data = (uint8_t *)PyString_AS_STRING(optiondictvalue); 
#endif

                                getdns_dict_set_bindata(tmpoptions_list_dict, "option_data", option_data);
                            } else  {
                                PyErr_SetString(getdns_error, GETDNS_RETURN_EXTENSION_MISFORMAT_TEXT);
                                return NULL;
                            }
                            getdns_list_set_dict(optionslist, optionlistpos, tmpoptions_list_dict);
                        }
                    } /* for i ... optionlistsize */
                    getdns_dict_set_list(out_optdict, "options", optionslist);
                }     /* for options */
                getdns_dict_set_dict(newdict, "add_opt_parameters", out_optdict);
            } /* while PyDict_Next(tmp_optdict ... ) */
        } else {
            PyErr_SetString(getdns_error, GETDNS_RETURN_NO_SUCH_EXTENSION_TEXT);
            return NULL;
        }
    }
    return newdict;
}


/*
 * turn a Python address dictionary into a getdns data structure (inc. validation)
 */


getdns_dict *
    getdnsify_addressdict(PyObject *pydict)
{
    getdns_dict *addr_dict;
    getdns_bindata addr_data;
    getdns_bindata addr_type;
    PyObject *str;
    unsigned char buf[sizeof(struct in6_addr)];
    int domain;
    getdns_bindata tls_auth_name;
    getdns_bindata scope_id;
    getdns_bindata tsig_name;
    getdns_bindata tsig_alg;
    getdns_bindata tsig_secret;
    uint32_t tls_port, port;
    getdns_return_t ret;
    getdns_list *tls_pubkey_pinset;

    if (!PyDict_Check(pydict))  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return NULL;
    }

    /* XXX rewrite this so it's more general */

    /* dict members supported:
     *  address_data
     *  address_type
     *  tls_auth_name
     *  scope_id
     *  port
     *  tls_port
     *  tsig_name
     *  tsig_secret
     *  tsig_algorithm
     *  tls_pubkey_pinset
     */

    addr_dict = getdns_dict_create();
    if ((str = PyDict_GetItemString(pydict, "address_type")) == NULL)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return NULL;
    }
#if PY_MAJOR_VERSION >= 3
    if (!PyUnicode_Check(str))  {
#else
    if (!PyString_Check(str))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return NULL;
    }
#if PY_MAJOR_VERSION >= 3
    addr_type.data = (uint8_t *)strdup(PyBytes_AsString(PyUnicode_AsEncodedString(str, "ascii", NULL)));
#else
    addr_type.data = (uint8_t *)strdup(PyString_AsString(str));
#endif
    addr_type.size = strlen((char *)addr_type.data);
    if (strlen((char *)addr_type.data) != 4)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_WRONG_TYPE_REQUESTED_TEXT);
        return NULL;
    }
    if (!strncasecmp((char *)addr_type.data, "IPv4", 4))
        domain = AF_INET;
    else if (!strncasecmp((char *)addr_type.data, "IPv6", 4))
        domain = AF_INET6;
    else  {
        PyErr_SetString(getdns_error,  GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return NULL;
    }
    getdns_dict_set_bindata(addr_dict, "address_type", &addr_type);

    if ((str = PyDict_GetItemString(pydict, "address_data")) == NULL)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return NULL;
    }
#if PY_MAJOR_VERSION >= 3
    if (!PyUnicode_Check(str))  {
#else
    if (!PyString_Check(str))  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return NULL;
    }
#if PY_MAJOR_VERSION >= 3
    if (inet_pton(domain, PyBytes_AsString(PyUnicode_AsEncodedString(str, "ascii", NULL)), buf) <= 0)  {
#else
    if (inet_pton(domain, PyString_AsString(str), buf) <= 0)  {
#endif
        PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
        return NULL;
    }
    addr_data.data = (uint8_t *)buf;
    addr_data.size = (domain == AF_INET ? 4 : 16);
    getdns_dict_set_bindata(addr_dict, "address_data", &addr_data);

    if ((str = PyDict_GetItemString(pydict, "tls_auth_name")) != NULL)  {
#if PY_MAJOR_VERSION >= 3
        tls_auth_name.data = (uint8_t *)strdup(PyBytes_AsString(PyUnicode_AsEncodedString(str, "ascii", NULL)));
#else
        tls_auth_name.data = (uint8_t *)strdup(PyString_AsString(str));
#endif
        tls_auth_name.size = (size_t)strlen((char *)tls_auth_name.data);
        getdns_dict_set_bindata(addr_dict, "tls_auth_name", &tls_auth_name);
    }

    if ((str = PyDict_GetItemString(pydict, "scope_id")) != NULL)  {
#if PY_MAJOR_VERSION >= 3
        scope_id.data = (uint8_t *)strdup(PyBytes_AsString(PyUnicode_AsEncodedString(str, "ascii", NULL)));
#else
        scope_id.data = (uint8_t *)strdup(PyString_AsString(str));
#endif
        scope_id.size = (size_t)strlen((char *)scope_id.data);
        getdns_dict_set_bindata(addr_dict, "scope_id", &scope_id);
    }

    if ((str = PyDict_GetItemString(pydict, "tsig_name")) != NULL)  {
#if PY_MAJOR_VERSION >= 3
        tsig_name.data = (uint8_t *)strdup(PyBytes_AsString(PyUnicode_AsEncodedString(str, "ascii", NULL)));
#else
        tsig_name.data = (uint8_t *)strdup(PyBytes_AsString(str));
#endif
        tsig_name.size = (size_t)strlen((char *)tsig_name.data);
        if ((ret = getdns_dict_set_bindata(addr_dict, "tsig_name", &tsig_name)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, "bad tsig name");
            return NULL;
        }
    }

    if ((str = PyDict_GetItemString(pydict, "tsig_algorithm")) != NULL)  {
#if PY_MAJOR_VERSION >= 3
        tsig_alg.data = (uint8_t *)strdup(PyBytes_AsString(PyUnicode_AsEncodedString(str, "ascii", NULL)));
#else
        tsig_alg.data = (uint8_t *)strdup(PyBytes_AsString(str));
#endif
        tsig_alg.size = (size_t)strlen((char *)tsig_alg.data);
        if ((ret = getdns_dict_set_bindata(addr_dict, "tsig_algorithm", &tsig_alg)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, "bad tsig algorithm");
            return NULL;
        }
    }

    if ((str = PyDict_GetItemString(pydict, "tsig_secret")) != NULL)  {
        tsig_secret.size = PyByteArray_Size(str);
#if PY_MAJOR_VERSION >= 3
        tsig_secret.data = (uint8_t *)strdup(PyBytes_AS_STRING(str));
#else
        tsig_secret.data = (uint8_t *)strdup(PyBytes_AsString(str));
#endif
        if ((ret = getdns_dict_set_bindata(addr_dict, "tsig_secret", &tsig_secret)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, "bad tsig secret");
            return NULL;
        }
    }

    if ((str = PyDict_GetItemString(pydict, "tls_pubkey_pinset")) != NULL)  {
        Py_ssize_t pinset_len;
        int  i;
        PyObject *py_item;
        char *str_item;
        getdns_dict *pubkey_pin = 0;

        if (!PyList_Check(str))  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return NULL;
        }
        pinset_len = PyList_Size(str);
        if (pinset_len == 0)    {
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return NULL;
        }
        tls_pubkey_pinset = getdns_list_create();
        for ( i = 0 ; i < (int)pinset_len ; i++ )  {
            py_item = PyList_GetItem(str, (Py_ssize_t)i);
#if PY_MAJOR_VERSION >= 3
            str_item = PyBytes_AsString(PyUnicode_AsEncodedString(py_item, "ascii", NULL));
#else
            str_item = PyString_AsString(py_item);
#endif
            pubkey_pin = getdns_pubkey_pin_create_from_string(0, str_item);
            if (pubkey_pin == NULL)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
                return NULL;
            }
            if ((ret = getdns_list_set_dict(tls_pubkey_pinset, i, pubkey_pin)) != GETDNS_RETURN_GOOD)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
                return NULL;
            }
        }
        if (pubkey_pin)
            getdns_dict_destroy(pubkey_pin);
        getdns_dict_set_list(addr_dict, "tls_pubkey_pinset", tls_pubkey_pinset);
    }

    if ((str = PyDict_GetItemString(pydict, "port")) != NULL)  {
#if PY_MAJOR_VERSION >= 3
        if (!PyLong_Check(str))  {
#else
        if (!PyInt_Check(str))  {
#endif
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return NULL;
        }
#if PY_MAJOR_VERSION >= 3
        port = (uint32_t)PyLong_AsLong(str);
#else
        port = (uint32_t)PyInt_AsLong(str);
#endif
        getdns_dict_set_int(addr_dict, "port", port);
    }

    if ((str = PyDict_GetItemString(pydict, "tls_port")) != NULL)  {
#if PY_MAJOR_VERSION >= 3
        if (!PyLong_Check(str))  {
#else
        if (!PyInt_Check(str))  {
#endif
            PyErr_SetString(getdns_error, GETDNS_RETURN_INVALID_PARAMETER_TEXT);
            return NULL;
        }
#if PY_MAJOR_VERSION >= 3
        tls_port = (uint32_t)PyLong_AsLong(str);
#else
        tls_port = (uint32_t)PyInt_AsLong(str);
#endif
        getdns_dict_set_int(addr_dict, "tls_port", tls_port);
    }
    return addr_dict;
}


PyObject *
pythonify_address_list(getdns_list *list)
{
    size_t length;
    getdns_return_t ret;
    int i;
    PyObject *py_list;
    getdns_data_type type;
    getdns_dict *a_item;
    PyObject *py_item;
    getdns_bindata *a_address_data;
    getdns_bindata *a_address_type;
    int domain;
    char paddr_buf[256];

    if ((ret = getdns_list_get_length(list, &length)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return NULL;
    }
    py_list = PyList_New(0);
    for ( i = 0 ; i < (int)length ; i++ )  {
        if ((ret = getdns_list_get_data_type(list, i, &type)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        if (type != t_dict)  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
        if ((ret = getdns_list_get_dict(list, (size_t)i, &a_item)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        if ((ret = getdns_dict_get_bindata(a_item, "address_type", &a_address_type)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        if ((ret = getdns_dict_get_bindata(a_item, "address_data", &a_address_data)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        if (!strncasecmp((char *)a_address_type->data, "IPv4", 4))
            domain = AF_INET;
        else if (!strncasecmp((char *)a_address_type->data, "IPv6", 4))
            domain = AF_INET6;
        else  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
        py_item = PyDict_New();
        PyDict_SetItemString(py_item, "address_data",
#if PY_MAJOR_VERSION >= 3
                             PyUnicode_FromString(inet_ntop(domain, (void *)a_address_data->data,
                                                           (char *)paddr_buf, 256)));
#else
                             PyString_FromString(inet_ntop(domain, (void *)a_address_data->data,
                                                           (char *)paddr_buf, 256)));
#endif
        PyDict_SetItemString(py_item, "address_type",
#if PY_MAJOR_VERSION >= 3
                             PyUnicode_FromString((domain == AF_INET ? "IPv4" : "IPv6")));
#else
                             PyString_FromString((domain == AF_INET ? "IPv4" : "IPv6")));
#endif
        PyList_Append(py_list, py_item);
    }
    return py_list;
}




PyObject *
glist_to_plist(struct getdns_list *list)
{
    PyObject *py_list;
    size_t  count;
    getdns_return_t ret;
    int  i;
    getdns_data_type type;
    struct getdns_dict *dict_item;
    struct getdns_list *list_item;
    PyObject *py_dict, *py_locallist, *py_bindata, *py_int;
    uint32_t localint;
    getdns_bindata *data;

    if (!list)  {
        PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
        return NULL;
    }
        
    if ((ret = getdns_list_get_length(list, &count)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return NULL;
    }
    py_list = PyList_New(0);
    for ( i = 0 ; i < count ; i++ )  {
        (void)getdns_list_get_data_type(list, i, &type);
        switch (type)  {
        case t_dict:
            if ((ret = getdns_list_get_dict(list, i, &dict_item)) != GETDNS_RETURN_GOOD)  {
                PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
                return NULL;
            }
            if ((py_dict = gdict_to_pdict(dict_item)) == NULL)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
                return NULL;
            }
            if (PyList_Append(py_list, py_dict) == -1)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
                return NULL;
            }
            break;

        case t_list:
            if ((ret = getdns_list_get_list(list, i, &list_item)) != GETDNS_RETURN_GOOD)  {
                PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
                return NULL;
            }
            if ((py_locallist = glist_to_plist(list_item)) == NULL)  {
                PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
                return NULL;
            }
            if (PyList_Append(py_list, py_locallist) == -1)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
                return NULL;
            }
            break;

        case t_int:
            if ((ret = getdns_list_get_int(list, i, &localint)) != GETDNS_RETURN_GOOD)  {
                PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
                return NULL;
            }
#if PY_MAJOR_VERSION >= 3
            py_int = PyLong_FromLong((long)localint);
#else
            py_int = PyInt_FromLong((long)localint);
#endif
            if (PyList_Append(py_list, py_int) == -1)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
                return NULL;
            }
            break;

        case t_bindata:
            if ((ret = getdns_list_get_bindata(list, i, &data)) != GETDNS_RETURN_GOOD)  {
                PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
                return NULL;
            }
            if ((py_bindata = convertBinData(data, "")) == 0)  {
                return NULL;
            }
            if (PyList_Append(py_list, py_bindata) == -1)  {
                return NULL;
            }
            break;

        default:
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
    }
    return py_list;
}



PyObject *
gdict_to_pdict(struct getdns_dict *dict)
{
    PyObject *py_dict;
    getdns_list *keys;
    size_t n_keys;
    getdns_return_t ret;
    int i;
    getdns_bindata *key_name;
    getdns_data_type type;
    getdns_list *list_item;
    getdns_dict *dict_item;
    uint32_t int_item;
    getdns_bindata *bindata_item;
    PyObject *py_localdict;
    PyObject *py_locallist;
    PyObject *py_localint;
    PyObject *py_localbindata;

    if ((ret = getdns_dict_get_names(dict, &keys)) != GETDNS_RETURN_GOOD)  {
        PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
        return NULL;
    }
    py_dict = PyDict_New();
    (void)getdns_list_get_length(keys, &n_keys);
    for (i = 0 ; i < (int)n_keys ; i++ )  {
        if ((ret = getdns_list_get_bindata(keys, (size_t)i, &key_name)) != GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        if (strnlen((char *)key_name->data, 256) == 256)  { /* too long, something's wrong */
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
        if ((ret = getdns_dict_get_data_type(dict, (char *)key_name->data, &type)) !=
            GETDNS_RETURN_GOOD)  {
            PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
            return NULL;
        }
        switch (type)  {
        case t_dict:
            if ((ret = getdns_dict_get_dict(dict, (char *)key_name->data, &dict_item)) !=
                GETDNS_RETURN_GOOD)  {
                PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
                return NULL;
            }
            if ((py_localdict = gdict_to_pdict(dict_item)) == NULL)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
                return NULL;
            }
            if (PyDict_SetItemString(py_dict, (char *)key_name->data, py_localdict) != 0)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
                return NULL;
            }
            break;

        case t_list:
            if ((ret = getdns_dict_get_list(dict, (char *)key_name->data, &list_item)) !=
                GETDNS_RETURN_GOOD)  {
                PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
                return NULL;
            }
            if ((py_locallist = glist_to_plist(list_item)) == NULL)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
                return NULL;
            }
            if (PyDict_SetItemString(py_dict, (char *)key_name->data, py_locallist) != 0)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
                return NULL;
            }
            break;

        case t_int:
            if ((ret = getdns_dict_get_int(dict, (char *)key_name->data, &int_item)) !=
                GETDNS_RETURN_GOOD)  {
                PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
                return NULL;
            }
#if PY_MAJOR_VERSION >= 3
            py_localint = PyLong_FromLong((long)int_item);
#else
            py_localint = PyInt_FromLong((long)int_item);
#endif
            if (PyDict_SetItemString(py_dict, (char *)key_name->data, py_localint) == -1)  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
                return NULL;
            }
            break;

        case t_bindata:
            if ((ret = getdns_dict_get_bindata(dict, (char *)key_name->data, &bindata_item))
                != GETDNS_RETURN_GOOD)  {
                PyErr_SetString(getdns_error, getdns_get_errorstr_by_id(ret));
                return NULL;
            }
            if ((bindata_item == 0) || (bindata_item->data == 0) || bindata_item->size == 0)  {
                break;
            }
            if ((py_localbindata = convertBinData(bindata_item, (char *)key_name->data)) == 0)  {
                return NULL;
            }
            if (PyDict_SetItemString(py_dict, (char *)key_name->data, py_localbindata) == -1)  {
                return NULL;
            }
            break;

        default:
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
    }
    return py_dict;
}


/*
 * Error checking helper
 */
void error_exit(char* msg, getdns_return_t ret)
{
    char error_str[512];
    if (ret != GETDNS_RETURN_GOOD)  {
        sprintf(error_str, "%s: %d", msg, ret);
        printf("ERROR: %s: %d", msg, ret);
        PyErr_SetString(getdns_error, error_str);
    }
}



// Code to display the entire response.
// answer_type
// canonical_name
// just_address_answers
// replies_full
// replies_tree

// Taken from getdns source to do label checking

static int
priv_getdns_bindata_is_dname(struct getdns_bindata *bindata)
{
    size_t i = 0, n_labels = 0;
    while (i < bindata->size) {
        i += ((size_t)bindata->data[i]) + 1;
        n_labels++;
    }
    return i == bindata->size && n_labels > 1 &&
        bindata->data[bindata->size - 1] == 0;
}

// Convert bindata into a good representational string or
// into a buffer. Handles dname, printable, ".",
// and an ip address if it is under a known key

PyObject *
convertBinData(getdns_bindata* data,
                    const char* key) 
{
    size_t i; 


    // the root
    if (data->size == 1 && data->data[0] == 0) {
        PyObject *a_string;

#if PY_MAJOR_VERSION >= 3
        if ((a_string = PyUnicode_FromString(".")) == NULL)  {
#else
        if ((a_string = PyString_FromString(".")) == NULL)  {
#endif
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
        return(a_string);
    }

    int printable = 1;
    for (i = 0; i < data->size; ++i) {
        if (!isprint(data->data[i])) {
            if (data->data[i] == 0 &&
                i == data->size - 1) {
                break;
            }
            printable = 0;
            break;
        }
    }
    // basic string?
    if (printable == 1) {
        PyObject *a_string;

#if PY_MAJOR_VERSION >= 3
        if ((a_string = PyUnicode_FromStringAndSize((char *)data->data, (Py_ssize_t)(data->size))) == NULL)  {
#else
        if ((a_string = PyString_FromStringAndSize((char *)data->data, (Py_ssize_t)(data->size))) == NULL)  {
#endif
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
        return(a_string);
    }


    // dname
    if (priv_getdns_bindata_is_dname(data)) {
        char* dname = NULL;
        PyObject *dname_string;

        if (getdns_convert_dns_name_to_fqdn(data, &dname)
            == GETDNS_RETURN_GOOD) {
#if PY_MAJOR_VERSION >= 3
            if ((dname_string = PyUnicode_FromString(dname)) != NULL)  {
#else
            if ((dname_string = PyString_FromString(dname)) != NULL)  {
#endif
                return(dname_string);
            }  else  {
                PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
                return NULL;
            }
        } else {
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
    } else if (key != NULL && (strcmp(key, "address_data") == 0))  { /* XXX */
               
#if 0
        (strcmp(key, "ipv4_address") == 0 ||
         strcmp(key, "ipv6_address") == 0)) {
#endif
        char* ipStr = getdns_display_ip_address(data);
        if (ipStr) {
            PyObject *addr_string;
#if PY_MAJOR_VERSION >= 3
            if ((addr_string = PyUnicode_FromString(ipStr)) == NULL)  {
#else
            if ((addr_string = PyString_FromString(ipStr)) == NULL)  {
#endif
                PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
                return NULL;
            }
            return(addr_string);
        }
    }  else  {                  /* none of the above, treat it like a blob */
        uint8_t *blob = (uint8_t *)malloc(data->size);
        
        memcpy(blob, data->data, data->size);
#if PY_MAJOR_VERSION >= 3                       
        return (PyMemoryView_FromMemory((char *)blob, (Py_ssize_t)data->size, PyBUF_READ));
#else
        return (PyBuffer_FromMemory(blob, (Py_ssize_t)data->size));
#endif
    }
    return NULL;                /* should never get here .. */
}

PyObject *getdns_dict_to_ip_string(getdns_dict* dict);
PyObject *convertToList(struct getdns_list* list);

PyObject*
convertToDict(struct getdns_dict* dict) {

    PyObject *resultsdict1;
    
    if (!dict) {
        return 0;
    }

    if ((resultsdict1 = PyDict_New()) == NULL)  {
        error_exit("Unable to allocate response dict", 0);
        return NULL;
    }

    // try it as an IP
    PyObject *ipdict = getdns_dict_to_ip_string(dict);
    if (ipdict) {
        return ipdict;
    }

    getdns_list* names;
    getdns_dict_get_names(dict, &names);
    size_t len = 0, i = 0;
    getdns_list_get_length(names, &len);
    for (i = 0; i < len; ++i) {
        getdns_bindata* nameBin;
        getdns_list_get_bindata(names, i, &nameBin);
        getdns_data_type type;
        getdns_dict_get_data_type(dict, (char*)nameBin->data, &type);

        switch (type) {
            case t_bindata:
            {
                getdns_bindata* data = NULL;
                getdns_dict_get_bindata(dict, (char*)nameBin->data, &data);
                PyObject* res = convertBinData(data, (char*)nameBin->data);
#if PY_MAJOR_VERSION >= 3
                PyDict_SetItem(resultsdict1, PyUnicode_FromStringAndSize((char *)nameBin->data, 
                                                                         (Py_ssize_t)nameBin->size), res);
#else
                PyDict_SetItem(resultsdict1, PyString_FromStringAndSize((char *)nameBin->data,
                                                                 (Py_ssize_t)nameBin->size), res);
#endif
                break;
            }
            case t_int:
            {
                uint32_t res = 0;
                getdns_dict_get_int(dict, (char*)nameBin->data, &res);
                PyObject* rl1 = Py_BuildValue("i", res);
                PyObject *res1 = Py_BuildValue("O", rl1);
#if PY_MAJOR_VERSION >= 3
                PyDict_SetItem(resultsdict1, PyUnicode_FromStringAndSize((char *)nameBin->data,
                                                                         (Py_ssize_t)nameBin->size), res1);
#else
                PyDict_SetItem(resultsdict1, PyString_FromStringAndSize((char *)nameBin->data,
                                                                        (Py_ssize_t)nameBin->size), res1);
#endif
                break;
            }
            case t_dict:
            {
                getdns_dict* subdict = NULL;
                getdns_dict_get_dict(dict, (char*)nameBin->data, &subdict);
                PyObject *rl1 = convertToDict(subdict);
                PyObject *res1 = Py_BuildValue("O", rl1);
#if PY_MAJOR_VERSION >= 3
                PyDict_SetItem(resultsdict1, PyUnicode_FromStringAndSize((char *)nameBin->data,
                                                                         (Py_ssize_t)nameBin->size), res1);
#else
                PyDict_SetItem(resultsdict1, PyString_FromStringAndSize((char *)nameBin->data,
                                                                        (Py_ssize_t)nameBin->size), res1);
#endif
                break;
            }
            case t_list:
            {
                getdns_list* list = NULL;
                getdns_dict_get_list(dict, (char*)nameBin->data, &list);
                PyObject *rl1 = convertToList(list);
                PyObject *res1 = Py_BuildValue("O", rl1);
#if PY_MAJOR_VERSION >= 3
                PyObject *key = PyUnicode_FromStringAndSize((char *)nameBin->data,
                                                            (Py_ssize_t)nameBin->size);
#else
                PyObject *key = PyString_FromStringAndSize((char *)nameBin->data,
                                                           (Py_ssize_t)nameBin->size);
#endif
                PyDict_SetItem(resultsdict1, key, res1);
                break;
            }
            default:
                break;
        }
    }
    getdns_list_destroy(names);
    return resultsdict1;
}



PyObject* 
convertToList(struct getdns_list* list) {


    if (!list) {
        return 0;
    }

    PyObject* resultslist1;
    if ((resultslist1 = PyList_New(0)) == NULL)  {
        error_exit("Unable to allocate response list", 0);
        return NULL;
    }

    size_t len, i;
    getdns_list_get_length(list, &len);
    for (i = 0; i < len; ++i) {
        getdns_data_type type;
        getdns_list_get_data_type(list, i, &type);
        switch (type) {
            case t_bindata:
            {
                getdns_bindata* data = NULL;
                getdns_list_get_bindata(list, i, &data);
                PyObject* res = convertBinData(data, NULL);
                if (res) {
                    PyList_Append(resultslist1, res);
                } else {

                    PyObject* res1 = Py_BuildValue("s", "empty");
                    PyList_Append(resultslist1, res1);
                }
                break;
            }
            case t_int:
            {
                uint32_t res = 0;
                getdns_list_get_int(list, i, &res);
                PyObject* res1 = Py_BuildValue("i", res); 
                PyList_Append(resultslist1, res1);
                break;
            }
            case t_dict:
            {
                getdns_dict* dict = NULL;
                getdns_list_get_dict(list, i, &dict);
                PyObject *rl1 = convertToDict(dict);
                PyList_Append(resultslist1, rl1);
                break;
            }
            case t_list:
            {
                getdns_list* sublist = NULL;
                getdns_list_get_list(list, i, &sublist);
                PyObject* rl1 = convertToList(sublist);
                PyObject *res1 = Py_BuildValue("O", rl1);
                PyList_Append(resultslist1, res1);
                break;
            }
            default:
                break;
        }
    }

    return resultslist1;
}

// potential helper to get the ip string of a dict

PyObject * 
getdns_dict_to_ip_string(getdns_dict* dict) {
    getdns_bindata *addr;
    getdns_bindata *type;
    getdns_return_t r;
    PyObject *addr_dict;
    char *addr_string;
    PyObject *pyaddr_string;

    if (!dict) {
        return NULL;
    }
    r = getdns_dict_get_bindata(dict, "address_type", &type);
    if (r != GETDNS_RETURN_GOOD) {
        return NULL;
    }
    if (type->size == 5 &&
        (strcmp("IPv4", (char*) type->data) == 0 ||
         strcmp("IPv6", (char*) type->data) == 0)) {
        r = getdns_dict_get_bindata(dict, "address_data", &addr);
        if (r != GETDNS_RETURN_GOOD) {
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
        if ((addr_dict = PyDict_New()) == NULL)  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
#if PY_MAJOR_VERSION >= 3
        if (PyDict_SetItemString(addr_dict, "address_type", PyUnicode_FromStringAndSize((char *)type->data,
                                                                                        (Py_ssize_t)type->size)) != 0)  {
#else
        if (PyDict_SetItemString(addr_dict, "address_type", PyString_FromStringAndSize((char *)type->data,
                                                                                       (Py_ssize_t)type->size)) != 0)  {
#endif
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
        addr_string = getdns_display_ip_address(addr);
#if PY_MAJOR_VERSION >= 3
        if ((pyaddr_string = PyUnicode_FromString(addr_string)) == NULL)  {
#else
        if ((pyaddr_string = PyString_FromString(addr_string)) == NULL)  {
#endif
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
        if (PyDict_SetItemString(addr_dict, "address_data", pyaddr_string) != 0)  {
            PyErr_SetString(getdns_error, GETDNS_RETURN_GENERIC_ERROR_TEXT);
            return NULL;
        }
    }
    return NULL;
}


