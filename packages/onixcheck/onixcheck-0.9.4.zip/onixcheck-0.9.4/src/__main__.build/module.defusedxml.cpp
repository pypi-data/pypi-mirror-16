/* Generated code for Python source for module 'defusedxml'
 * created by Nuitka version 0.5.21.1
 *
 * This code is in part copyright 2016 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.hpp"

#include "__helpers.hpp"

/* The _module_defusedxml is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_defusedxml;
PyDictObject *moduledict_defusedxml;

/* The module constants used, if any. */
extern PyObject *const_str_plain_defusedxml;
static PyObject *const_tuple_str_plain_minidom_tuple;
extern PyObject *const_str_plain_EntitiesForbidden;
static PyObject *const_str_digest_911922ba64bbf1ffc2f6bc469b8dcf7c;
extern PyObject *const_str_empty;
extern PyObject *const_str_plain_stdlib_mod;
static PyObject *const_str_digest_e511ce2b59cdfa80bd47f4ea0ed3af19;
static PyObject *const_tuple_str_plain_ElementTree_tuple;
extern PyObject *const_dict_empty;
extern PyObject *const_str_plain_pulldom;
extern PyObject *const_str_plain_DefusedXmlException;
static PyObject *const_tuple_str_plain_xmlrpc_tuple;
extern PyObject *const_str_plain_absolute_import;
extern PyObject *const_str_plain_sax;
static PyObject *const_tuple_str_plain_sax_tuple;
static PyObject *const_str_digest_0127e46389ddf931f646f7560f89d11f;
extern PyObject *const_str_plain__apply_defusing;
extern PyObject *const_tuple_str_plain_expatbuilder_tuple;
extern PyObject *const_str_plain_xmlrpc;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_expatbuilder;
extern PyObject *const_str_plain_minidom;
extern PyObject *const_tuple_empty;
extern PyObject *const_tuple_str_plain_pulldom_tuple;
extern PyObject *const_str_plain_defused_mod;
extern PyObject *const_str_plain_common;
extern PyObject *const_str_plain_cElementTree;
extern PyObject *const_str_plain___file__;
extern PyObject *const_str_plain___version__;
static PyObject *const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple;
extern PyObject *const_int_pos_1;
static PyObject *const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple;
extern PyObject *const_str_plain_ElementTree;
extern PyObject *const_str_plain_NotSupportedError;
static PyObject *const_str_plain_defused;
static PyObject *const_str_plain_defuse_stdlib;
extern PyObject *const_str_plain___path__;
static PyObject *const_str_digest_fc916d355f843c8fad5108ad050f3c75;
extern PyObject *const_str_plain_DTDForbidden;
static PyObject *const_tuple_str_plain_cElementTree_tuple;
extern PyObject *const_str_plain_dirname;
extern PyObject *const_str_plain_monkey_patch;
extern PyObject *const_str_plain_ExternalReferenceForbidden;
extern PyObject *const_tuple_str_plain_expatreader_tuple;
extern PyObject *const_str_plain_print_function;
extern PyObject *const_str_plain_expatreader;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_tuple_str_plain_minidom_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_minidom_tuple, 0, const_str_plain_minidom ); Py_INCREF( const_str_plain_minidom );
    const_str_digest_911922ba64bbf1ffc2f6bc469b8dcf7c = UNSTREAM_STRING( &constant_bin[ 218761 ], 50, 0 );
    const_str_digest_e511ce2b59cdfa80bd47f4ea0ed3af19 = UNSTREAM_STRING( &constant_bin[ 218811 ], 108, 0 );
    const_tuple_str_plain_ElementTree_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_ElementTree_tuple, 0, const_str_plain_ElementTree ); Py_INCREF( const_str_plain_ElementTree );
    const_tuple_str_plain_xmlrpc_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_xmlrpc_tuple, 0, const_str_plain_xmlrpc ); Py_INCREF( const_str_plain_xmlrpc );
    const_tuple_str_plain_sax_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_sax_tuple, 0, const_str_plain_sax ); Py_INCREF( const_str_plain_sax );
    const_str_digest_0127e46389ddf931f646f7560f89d11f = UNSTREAM_STRING( &constant_bin[ 218919 ], 5, 0 );
    const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple = PyTuple_New( 11 );
    const_str_plain_defused = UNSTREAM_STRING( &constant_bin[ 218924 ], 7, 1 );
    PyTuple_SET_ITEM( const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple, 0, const_str_plain_defused ); Py_INCREF( const_str_plain_defused );
    PyTuple_SET_ITEM( const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple, 1, const_str_plain_cElementTree ); Py_INCREF( const_str_plain_cElementTree );
    PyTuple_SET_ITEM( const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple, 2, const_str_plain_ElementTree ); Py_INCREF( const_str_plain_ElementTree );
    PyTuple_SET_ITEM( const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple, 3, const_str_plain_minidom ); Py_INCREF( const_str_plain_minidom );
    PyTuple_SET_ITEM( const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple, 4, const_str_plain_pulldom ); Py_INCREF( const_str_plain_pulldom );
    PyTuple_SET_ITEM( const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple, 5, const_str_plain_sax ); Py_INCREF( const_str_plain_sax );
    PyTuple_SET_ITEM( const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple, 6, const_str_plain_expatbuilder ); Py_INCREF( const_str_plain_expatbuilder );
    PyTuple_SET_ITEM( const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple, 7, const_str_plain_expatreader ); Py_INCREF( const_str_plain_expatreader );
    PyTuple_SET_ITEM( const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple, 8, const_str_plain_xmlrpc ); Py_INCREF( const_str_plain_xmlrpc );
    PyTuple_SET_ITEM( const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple, 9, const_str_plain_defused_mod ); Py_INCREF( const_str_plain_defused_mod );
    PyTuple_SET_ITEM( const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple, 10, const_str_plain_stdlib_mod ); Py_INCREF( const_str_plain_stdlib_mod );
    const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple = PyTuple_New( 6 );
    PyTuple_SET_ITEM( const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple, 0, const_str_plain_DefusedXmlException ); Py_INCREF( const_str_plain_DefusedXmlException );
    PyTuple_SET_ITEM( const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple, 1, const_str_plain_DTDForbidden ); Py_INCREF( const_str_plain_DTDForbidden );
    PyTuple_SET_ITEM( const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple, 2, const_str_plain_EntitiesForbidden ); Py_INCREF( const_str_plain_EntitiesForbidden );
    PyTuple_SET_ITEM( const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple, 3, const_str_plain_ExternalReferenceForbidden ); Py_INCREF( const_str_plain_ExternalReferenceForbidden );
    PyTuple_SET_ITEM( const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple, 4, const_str_plain_NotSupportedError ); Py_INCREF( const_str_plain_NotSupportedError );
    PyTuple_SET_ITEM( const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple, 5, const_str_plain__apply_defusing ); Py_INCREF( const_str_plain__apply_defusing );
    const_str_plain_defuse_stdlib = UNSTREAM_STRING( &constant_bin[ 218931 ], 13, 1 );
    const_str_digest_fc916d355f843c8fad5108ad050f3c75 = UNSTREAM_STRING( &constant_bin[ 218944 ], 22, 0 );
    const_tuple_str_plain_cElementTree_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_cElementTree_tuple, 0, const_str_plain_cElementTree ); Py_INCREF( const_str_plain_cElementTree );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_defusedxml( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_73747dc4dbea8441e08338a54b583edc;
static PyCodeObject *codeobj_ef4d69cb25300a5d946649d342683981;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_fc916d355f843c8fad5108ad050f3c75 );
    codeobj_73747dc4dbea8441e08338a54b583edc = MAKE_CODEOBJ( module_filename_obj, const_str_plain_defuse_stdlib, 14, const_tuple_b9b0d363697c4a7e70f1ba131faa332b_tuple, 0, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_PRINT_FUNCTION );
    codeobj_ef4d69cb25300a5d946649d342683981 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_defusedxml, 1, const_tuple_empty, 0, CO_NOFREE | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_PRINT_FUNCTION );
}

// The module function declarations.
static PyObject *MAKE_FUNCTION_function_1_defuse_stdlib_of_defusedxml(  );


// The module function definitions.
static PyObject *impl_function_1_defuse_stdlib_of_defusedxml( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *var_defused = NULL;
    PyObject *var_cElementTree = NULL;
    PyObject *var_ElementTree = NULL;
    PyObject *var_minidom = NULL;
    PyObject *var_pulldom = NULL;
    PyObject *var_sax = NULL;
    PyObject *var_expatbuilder = NULL;
    PyObject *var_expatreader = NULL;
    PyObject *var_xmlrpc = NULL;
    PyObject *var_defused_mod = NULL;
    PyObject *var_stdlib_mod = NULL;
    PyObject *tmp_for_loop_1__for_iterator = NULL;
    PyObject *tmp_for_loop_1__iter_value = NULL;
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *exception_keeper_type_2;
    PyObject *exception_keeper_value_2;
    PyTracebackObject *exception_keeper_tb_2;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_2;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_assign_source_5;
    PyObject *tmp_assign_source_6;
    PyObject *tmp_assign_source_7;
    PyObject *tmp_assign_source_8;
    PyObject *tmp_assign_source_9;
    PyObject *tmp_assign_source_10;
    PyObject *tmp_assign_source_11;
    PyObject *tmp_assign_source_12;
    PyObject *tmp_assign_source_13;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_dictset_dict;
    PyObject *tmp_dictset_key;
    PyObject *tmp_dictset_value;
    PyObject *tmp_frame_locals;
    PyObject *tmp_import_globals_1;
    PyObject *tmp_import_globals_2;
    PyObject *tmp_import_globals_3;
    PyObject *tmp_import_globals_4;
    PyObject *tmp_import_globals_5;
    PyObject *tmp_import_globals_6;
    PyObject *tmp_import_globals_7;
    PyObject *tmp_import_globals_8;
    PyObject *tmp_import_locals_1;
    PyObject *tmp_import_locals_2;
    PyObject *tmp_import_locals_3;
    PyObject *tmp_import_locals_4;
    PyObject *tmp_import_locals_5;
    PyObject *tmp_import_locals_6;
    PyObject *tmp_import_locals_7;
    PyObject *tmp_import_locals_8;
    PyObject *tmp_import_name_from_1;
    PyObject *tmp_import_name_from_2;
    PyObject *tmp_import_name_from_3;
    PyObject *tmp_import_name_from_4;
    PyObject *tmp_import_name_from_5;
    PyObject *tmp_import_name_from_6;
    PyObject *tmp_import_name_from_7;
    PyObject *tmp_import_name_from_8;
    PyObject *tmp_iter_arg_1;
    PyObject *tmp_next_source_1;
    int tmp_res;
    PyObject *tmp_return_value;
    PyObject *tmp_source_name_1;
    PyObject *tmp_tuple_element_1;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    tmp_assign_source_1 = PyDict_New();
    assert( var_defused == NULL );
    var_defused = tmp_assign_source_1;

    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_73747dc4dbea8441e08338a54b583edc, module_defusedxml );
    frame_function = cache_frame_function;

    // Push the new frame as the currently active one.
    pushFrameStack( frame_function );

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    Py_INCREF( frame_function );
    assert( Py_REFCNT( frame_function ) == 2 ); // Frame stack

#if PYTHON_VERSION >= 340
    frame_function->f_executing += 1;
#endif

    // Framed code:
    tmp_import_globals_1 = ((PyModuleObject *)module_defusedxml)->md_dict;
    tmp_import_locals_1 = PyDict_New();
    if ( var_defused )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_defused,
            var_defused
        );

        assert( res == 0 );
    }

    if ( var_cElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_cElementTree,
            var_cElementTree
        );

        assert( res == 0 );
    }

    if ( var_ElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_ElementTree,
            var_ElementTree
        );

        assert( res == 0 );
    }

    if ( var_minidom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_minidom,
            var_minidom
        );

        assert( res == 0 );
    }

    if ( var_pulldom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_pulldom,
            var_pulldom
        );

        assert( res == 0 );
    }

    if ( var_sax )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_sax,
            var_sax
        );

        assert( res == 0 );
    }

    if ( var_expatbuilder )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_expatbuilder,
            var_expatbuilder
        );

        assert( res == 0 );
    }

    if ( var_expatreader )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_expatreader,
            var_expatreader
        );

        assert( res == 0 );
    }

    if ( var_xmlrpc )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_xmlrpc,
            var_xmlrpc
        );

        assert( res == 0 );
    }

    if ( var_defused_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_defused_mod,
            var_defused_mod
        );

        assert( res == 0 );
    }

    if ( var_stdlib_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_stdlib_mod,
            var_stdlib_mod
        );

        assert( res == 0 );
    }

    frame_function->f_lineno = 21;
    tmp_import_name_from_1 = IMPORT_MODULE( const_str_empty, tmp_import_globals_1, tmp_import_locals_1, const_tuple_str_plain_cElementTree_tuple, const_int_pos_1 );
    Py_DECREF( tmp_import_locals_1 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 21;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_2 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_cElementTree );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 21;
        goto frame_exception_exit_1;
    }
    assert( var_cElementTree == NULL );
    var_cElementTree = tmp_assign_source_2;

    tmp_import_globals_2 = ((PyModuleObject *)module_defusedxml)->md_dict;
    tmp_import_locals_2 = PyDict_New();
    if ( var_defused )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_2,
            const_str_plain_defused,
            var_defused
        );

        assert( res == 0 );
    }

    if ( var_cElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_2,
            const_str_plain_cElementTree,
            var_cElementTree
        );

        assert( res == 0 );
    }

    if ( var_ElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_2,
            const_str_plain_ElementTree,
            var_ElementTree
        );

        assert( res == 0 );
    }

    if ( var_minidom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_2,
            const_str_plain_minidom,
            var_minidom
        );

        assert( res == 0 );
    }

    if ( var_pulldom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_2,
            const_str_plain_pulldom,
            var_pulldom
        );

        assert( res == 0 );
    }

    if ( var_sax )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_2,
            const_str_plain_sax,
            var_sax
        );

        assert( res == 0 );
    }

    if ( var_expatbuilder )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_2,
            const_str_plain_expatbuilder,
            var_expatbuilder
        );

        assert( res == 0 );
    }

    if ( var_expatreader )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_2,
            const_str_plain_expatreader,
            var_expatreader
        );

        assert( res == 0 );
    }

    if ( var_xmlrpc )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_2,
            const_str_plain_xmlrpc,
            var_xmlrpc
        );

        assert( res == 0 );
    }

    if ( var_defused_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_2,
            const_str_plain_defused_mod,
            var_defused_mod
        );

        assert( res == 0 );
    }

    if ( var_stdlib_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_2,
            const_str_plain_stdlib_mod,
            var_stdlib_mod
        );

        assert( res == 0 );
    }

    frame_function->f_lineno = 22;
    tmp_import_name_from_2 = IMPORT_MODULE( const_str_empty, tmp_import_globals_2, tmp_import_locals_2, const_tuple_str_plain_ElementTree_tuple, const_int_pos_1 );
    Py_DECREF( tmp_import_locals_2 );
    if ( tmp_import_name_from_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 22;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_3 = IMPORT_NAME( tmp_import_name_from_2, const_str_plain_ElementTree );
    Py_DECREF( tmp_import_name_from_2 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 22;
        goto frame_exception_exit_1;
    }
    assert( var_ElementTree == NULL );
    var_ElementTree = tmp_assign_source_3;

    tmp_import_globals_3 = ((PyModuleObject *)module_defusedxml)->md_dict;
    tmp_import_locals_3 = PyDict_New();
    if ( var_defused )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_3,
            const_str_plain_defused,
            var_defused
        );

        assert( res == 0 );
    }

    if ( var_cElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_3,
            const_str_plain_cElementTree,
            var_cElementTree
        );

        assert( res == 0 );
    }

    if ( var_ElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_3,
            const_str_plain_ElementTree,
            var_ElementTree
        );

        assert( res == 0 );
    }

    if ( var_minidom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_3,
            const_str_plain_minidom,
            var_minidom
        );

        assert( res == 0 );
    }

    if ( var_pulldom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_3,
            const_str_plain_pulldom,
            var_pulldom
        );

        assert( res == 0 );
    }

    if ( var_sax )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_3,
            const_str_plain_sax,
            var_sax
        );

        assert( res == 0 );
    }

    if ( var_expatbuilder )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_3,
            const_str_plain_expatbuilder,
            var_expatbuilder
        );

        assert( res == 0 );
    }

    if ( var_expatreader )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_3,
            const_str_plain_expatreader,
            var_expatreader
        );

        assert( res == 0 );
    }

    if ( var_xmlrpc )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_3,
            const_str_plain_xmlrpc,
            var_xmlrpc
        );

        assert( res == 0 );
    }

    if ( var_defused_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_3,
            const_str_plain_defused_mod,
            var_defused_mod
        );

        assert( res == 0 );
    }

    if ( var_stdlib_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_3,
            const_str_plain_stdlib_mod,
            var_stdlib_mod
        );

        assert( res == 0 );
    }

    frame_function->f_lineno = 23;
    tmp_import_name_from_3 = IMPORT_MODULE( const_str_empty, tmp_import_globals_3, tmp_import_locals_3, const_tuple_str_plain_minidom_tuple, const_int_pos_1 );
    Py_DECREF( tmp_import_locals_3 );
    if ( tmp_import_name_from_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 23;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_4 = IMPORT_NAME( tmp_import_name_from_3, const_str_plain_minidom );
    Py_DECREF( tmp_import_name_from_3 );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 23;
        goto frame_exception_exit_1;
    }
    assert( var_minidom == NULL );
    var_minidom = tmp_assign_source_4;

    tmp_import_globals_4 = ((PyModuleObject *)module_defusedxml)->md_dict;
    tmp_import_locals_4 = PyDict_New();
    if ( var_defused )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_4,
            const_str_plain_defused,
            var_defused
        );

        assert( res == 0 );
    }

    if ( var_cElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_4,
            const_str_plain_cElementTree,
            var_cElementTree
        );

        assert( res == 0 );
    }

    if ( var_ElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_4,
            const_str_plain_ElementTree,
            var_ElementTree
        );

        assert( res == 0 );
    }

    if ( var_minidom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_4,
            const_str_plain_minidom,
            var_minidom
        );

        assert( res == 0 );
    }

    if ( var_pulldom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_4,
            const_str_plain_pulldom,
            var_pulldom
        );

        assert( res == 0 );
    }

    if ( var_sax )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_4,
            const_str_plain_sax,
            var_sax
        );

        assert( res == 0 );
    }

    if ( var_expatbuilder )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_4,
            const_str_plain_expatbuilder,
            var_expatbuilder
        );

        assert( res == 0 );
    }

    if ( var_expatreader )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_4,
            const_str_plain_expatreader,
            var_expatreader
        );

        assert( res == 0 );
    }

    if ( var_xmlrpc )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_4,
            const_str_plain_xmlrpc,
            var_xmlrpc
        );

        assert( res == 0 );
    }

    if ( var_defused_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_4,
            const_str_plain_defused_mod,
            var_defused_mod
        );

        assert( res == 0 );
    }

    if ( var_stdlib_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_4,
            const_str_plain_stdlib_mod,
            var_stdlib_mod
        );

        assert( res == 0 );
    }

    frame_function->f_lineno = 24;
    tmp_import_name_from_4 = IMPORT_MODULE( const_str_empty, tmp_import_globals_4, tmp_import_locals_4, const_tuple_str_plain_pulldom_tuple, const_int_pos_1 );
    Py_DECREF( tmp_import_locals_4 );
    if ( tmp_import_name_from_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 24;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_5 = IMPORT_NAME( tmp_import_name_from_4, const_str_plain_pulldom );
    Py_DECREF( tmp_import_name_from_4 );
    if ( tmp_assign_source_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 24;
        goto frame_exception_exit_1;
    }
    assert( var_pulldom == NULL );
    var_pulldom = tmp_assign_source_5;

    tmp_import_globals_5 = ((PyModuleObject *)module_defusedxml)->md_dict;
    tmp_import_locals_5 = PyDict_New();
    if ( var_defused )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_5,
            const_str_plain_defused,
            var_defused
        );

        assert( res == 0 );
    }

    if ( var_cElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_5,
            const_str_plain_cElementTree,
            var_cElementTree
        );

        assert( res == 0 );
    }

    if ( var_ElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_5,
            const_str_plain_ElementTree,
            var_ElementTree
        );

        assert( res == 0 );
    }

    if ( var_minidom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_5,
            const_str_plain_minidom,
            var_minidom
        );

        assert( res == 0 );
    }

    if ( var_pulldom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_5,
            const_str_plain_pulldom,
            var_pulldom
        );

        assert( res == 0 );
    }

    if ( var_sax )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_5,
            const_str_plain_sax,
            var_sax
        );

        assert( res == 0 );
    }

    if ( var_expatbuilder )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_5,
            const_str_plain_expatbuilder,
            var_expatbuilder
        );

        assert( res == 0 );
    }

    if ( var_expatreader )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_5,
            const_str_plain_expatreader,
            var_expatreader
        );

        assert( res == 0 );
    }

    if ( var_xmlrpc )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_5,
            const_str_plain_xmlrpc,
            var_xmlrpc
        );

        assert( res == 0 );
    }

    if ( var_defused_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_5,
            const_str_plain_defused_mod,
            var_defused_mod
        );

        assert( res == 0 );
    }

    if ( var_stdlib_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_5,
            const_str_plain_stdlib_mod,
            var_stdlib_mod
        );

        assert( res == 0 );
    }

    frame_function->f_lineno = 25;
    tmp_import_name_from_5 = IMPORT_MODULE( const_str_empty, tmp_import_globals_5, tmp_import_locals_5, const_tuple_str_plain_sax_tuple, const_int_pos_1 );
    Py_DECREF( tmp_import_locals_5 );
    if ( tmp_import_name_from_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 25;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_6 = IMPORT_NAME( tmp_import_name_from_5, const_str_plain_sax );
    Py_DECREF( tmp_import_name_from_5 );
    if ( tmp_assign_source_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 25;
        goto frame_exception_exit_1;
    }
    assert( var_sax == NULL );
    var_sax = tmp_assign_source_6;

    tmp_import_globals_6 = ((PyModuleObject *)module_defusedxml)->md_dict;
    tmp_import_locals_6 = PyDict_New();
    if ( var_defused )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_6,
            const_str_plain_defused,
            var_defused
        );

        assert( res == 0 );
    }

    if ( var_cElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_6,
            const_str_plain_cElementTree,
            var_cElementTree
        );

        assert( res == 0 );
    }

    if ( var_ElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_6,
            const_str_plain_ElementTree,
            var_ElementTree
        );

        assert( res == 0 );
    }

    if ( var_minidom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_6,
            const_str_plain_minidom,
            var_minidom
        );

        assert( res == 0 );
    }

    if ( var_pulldom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_6,
            const_str_plain_pulldom,
            var_pulldom
        );

        assert( res == 0 );
    }

    if ( var_sax )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_6,
            const_str_plain_sax,
            var_sax
        );

        assert( res == 0 );
    }

    if ( var_expatbuilder )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_6,
            const_str_plain_expatbuilder,
            var_expatbuilder
        );

        assert( res == 0 );
    }

    if ( var_expatreader )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_6,
            const_str_plain_expatreader,
            var_expatreader
        );

        assert( res == 0 );
    }

    if ( var_xmlrpc )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_6,
            const_str_plain_xmlrpc,
            var_xmlrpc
        );

        assert( res == 0 );
    }

    if ( var_defused_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_6,
            const_str_plain_defused_mod,
            var_defused_mod
        );

        assert( res == 0 );
    }

    if ( var_stdlib_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_6,
            const_str_plain_stdlib_mod,
            var_stdlib_mod
        );

        assert( res == 0 );
    }

    frame_function->f_lineno = 26;
    tmp_import_name_from_6 = IMPORT_MODULE( const_str_empty, tmp_import_globals_6, tmp_import_locals_6, const_tuple_str_plain_expatbuilder_tuple, const_int_pos_1 );
    Py_DECREF( tmp_import_locals_6 );
    if ( tmp_import_name_from_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 26;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_7 = IMPORT_NAME( tmp_import_name_from_6, const_str_plain_expatbuilder );
    Py_DECREF( tmp_import_name_from_6 );
    if ( tmp_assign_source_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 26;
        goto frame_exception_exit_1;
    }
    assert( var_expatbuilder == NULL );
    var_expatbuilder = tmp_assign_source_7;

    tmp_import_globals_7 = ((PyModuleObject *)module_defusedxml)->md_dict;
    tmp_import_locals_7 = PyDict_New();
    if ( var_defused )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_7,
            const_str_plain_defused,
            var_defused
        );

        assert( res == 0 );
    }

    if ( var_cElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_7,
            const_str_plain_cElementTree,
            var_cElementTree
        );

        assert( res == 0 );
    }

    if ( var_ElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_7,
            const_str_plain_ElementTree,
            var_ElementTree
        );

        assert( res == 0 );
    }

    if ( var_minidom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_7,
            const_str_plain_minidom,
            var_minidom
        );

        assert( res == 0 );
    }

    if ( var_pulldom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_7,
            const_str_plain_pulldom,
            var_pulldom
        );

        assert( res == 0 );
    }

    if ( var_sax )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_7,
            const_str_plain_sax,
            var_sax
        );

        assert( res == 0 );
    }

    if ( var_expatbuilder )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_7,
            const_str_plain_expatbuilder,
            var_expatbuilder
        );

        assert( res == 0 );
    }

    if ( var_expatreader )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_7,
            const_str_plain_expatreader,
            var_expatreader
        );

        assert( res == 0 );
    }

    if ( var_xmlrpc )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_7,
            const_str_plain_xmlrpc,
            var_xmlrpc
        );

        assert( res == 0 );
    }

    if ( var_defused_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_7,
            const_str_plain_defused_mod,
            var_defused_mod
        );

        assert( res == 0 );
    }

    if ( var_stdlib_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_7,
            const_str_plain_stdlib_mod,
            var_stdlib_mod
        );

        assert( res == 0 );
    }

    frame_function->f_lineno = 27;
    tmp_import_name_from_7 = IMPORT_MODULE( const_str_empty, tmp_import_globals_7, tmp_import_locals_7, const_tuple_str_plain_expatreader_tuple, const_int_pos_1 );
    Py_DECREF( tmp_import_locals_7 );
    if ( tmp_import_name_from_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 27;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_8 = IMPORT_NAME( tmp_import_name_from_7, const_str_plain_expatreader );
    Py_DECREF( tmp_import_name_from_7 );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 27;
        goto frame_exception_exit_1;
    }
    assert( var_expatreader == NULL );
    var_expatreader = tmp_assign_source_8;

    tmp_import_globals_8 = ((PyModuleObject *)module_defusedxml)->md_dict;
    tmp_import_locals_8 = PyDict_New();
    if ( var_defused )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_8,
            const_str_plain_defused,
            var_defused
        );

        assert( res == 0 );
    }

    if ( var_cElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_8,
            const_str_plain_cElementTree,
            var_cElementTree
        );

        assert( res == 0 );
    }

    if ( var_ElementTree )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_8,
            const_str_plain_ElementTree,
            var_ElementTree
        );

        assert( res == 0 );
    }

    if ( var_minidom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_8,
            const_str_plain_minidom,
            var_minidom
        );

        assert( res == 0 );
    }

    if ( var_pulldom )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_8,
            const_str_plain_pulldom,
            var_pulldom
        );

        assert( res == 0 );
    }

    if ( var_sax )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_8,
            const_str_plain_sax,
            var_sax
        );

        assert( res == 0 );
    }

    if ( var_expatbuilder )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_8,
            const_str_plain_expatbuilder,
            var_expatbuilder
        );

        assert( res == 0 );
    }

    if ( var_expatreader )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_8,
            const_str_plain_expatreader,
            var_expatreader
        );

        assert( res == 0 );
    }

    if ( var_xmlrpc )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_8,
            const_str_plain_xmlrpc,
            var_xmlrpc
        );

        assert( res == 0 );
    }

    if ( var_defused_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_8,
            const_str_plain_defused_mod,
            var_defused_mod
        );

        assert( res == 0 );
    }

    if ( var_stdlib_mod )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_8,
            const_str_plain_stdlib_mod,
            var_stdlib_mod
        );

        assert( res == 0 );
    }

    frame_function->f_lineno = 28;
    tmp_import_name_from_8 = IMPORT_MODULE( const_str_empty, tmp_import_globals_8, tmp_import_locals_8, const_tuple_str_plain_xmlrpc_tuple, const_int_pos_1 );
    Py_DECREF( tmp_import_locals_8 );
    if ( tmp_import_name_from_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 28;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_9 = IMPORT_NAME( tmp_import_name_from_8, const_str_plain_xmlrpc );
    Py_DECREF( tmp_import_name_from_8 );
    if ( tmp_assign_source_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 28;
        goto frame_exception_exit_1;
    }
    assert( var_xmlrpc == NULL );
    var_xmlrpc = tmp_assign_source_9;

    tmp_source_name_1 = var_xmlrpc;

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_monkey_patch );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    frame_function->f_lineno = 30;
    tmp_unused = CALL_FUNCTION_NO_ARGS( tmp_called_name_1 );
    Py_DECREF( tmp_called_name_1 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_dictset_value = Py_None;
    tmp_dictset_dict = var_defused;

    tmp_dictset_key = var_xmlrpc;

    tmp_res = PyDict_SetItem( tmp_dictset_dict, tmp_dictset_key, tmp_dictset_value );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 31;
        goto frame_exception_exit_1;
    }
    tmp_iter_arg_1 = PyTuple_New( 7 );
    tmp_tuple_element_1 = var_cElementTree;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_iter_arg_1, 0, tmp_tuple_element_1 );
    tmp_tuple_element_1 = var_ElementTree;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_iter_arg_1, 1, tmp_tuple_element_1 );
    tmp_tuple_element_1 = var_minidom;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_iter_arg_1, 2, tmp_tuple_element_1 );
    tmp_tuple_element_1 = var_pulldom;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_iter_arg_1, 3, tmp_tuple_element_1 );
    tmp_tuple_element_1 = var_sax;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_iter_arg_1, 4, tmp_tuple_element_1 );
    tmp_tuple_element_1 = var_expatbuilder;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_iter_arg_1, 5, tmp_tuple_element_1 );
    tmp_tuple_element_1 = var_expatreader;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_iter_arg_1, 6, tmp_tuple_element_1 );
    tmp_assign_source_10 = MAKE_ITERATOR( tmp_iter_arg_1 );
    Py_DECREF( tmp_iter_arg_1 );
    assert( tmp_assign_source_10 != NULL );
    assert( tmp_for_loop_1__for_iterator == NULL );
    tmp_for_loop_1__for_iterator = tmp_assign_source_10;

    // Tried code:
    loop_start_1:;
    tmp_next_source_1 = tmp_for_loop_1__for_iterator;

    tmp_assign_source_11 = ITERATOR_NEXT( tmp_next_source_1 );
    if ( tmp_assign_source_11 == NULL )
    {
        if ( CHECK_AND_CLEAR_STOP_ITERATION_OCCURRED() )
        {

            goto loop_end_1;
        }
        else
        {

            FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
            frame_function->f_lineno = 33;
            goto try_except_handler_2;
        }
    }

    {
        PyObject *old = tmp_for_loop_1__iter_value;
        tmp_for_loop_1__iter_value = tmp_assign_source_11;
        Py_XDECREF( old );
    }

    tmp_assign_source_12 = tmp_for_loop_1__iter_value;

    {
        PyObject *old = var_defused_mod;
        var_defused_mod = tmp_assign_source_12;
        Py_INCREF( var_defused_mod );
        Py_XDECREF( old );
    }

    tmp_called_name_2 = GET_STRING_DICT_VALUE( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain__apply_defusing );

    if (unlikely( tmp_called_name_2 == NULL ))
    {
        tmp_called_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__apply_defusing );
    }

    if ( tmp_called_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "_apply_defusing" );
        exception_tb = NULL;

        exception_lineno = 35;
        goto try_except_handler_2;
    }

    tmp_args_element_name_1 = var_defused_mod;

    frame_function->f_lineno = 35;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_assign_source_13 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_2, call_args );
    }

    if ( tmp_assign_source_13 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 35;
        goto try_except_handler_2;
    }
    {
        PyObject *old = var_stdlib_mod;
        var_stdlib_mod = tmp_assign_source_13;
        Py_XDECREF( old );
    }

    tmp_dictset_value = var_stdlib_mod;

    tmp_dictset_dict = var_defused;

    tmp_dictset_key = var_defused_mod;

    tmp_res = PyDict_SetItem( tmp_dictset_dict, tmp_dictset_key, tmp_dictset_value );
    if ( tmp_res != 0 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 36;
        goto try_except_handler_2;
    }
    if ( CONSIDER_THREADING() == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 33;
        goto try_except_handler_2;
    }
    goto loop_start_1;
    loop_end_1:;
    goto try_end_1;
    // Exception handler code:
    try_except_handler_2:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    Py_XDECREF( tmp_for_loop_1__iter_value );
    tmp_for_loop_1__iter_value = NULL;

    CHECK_OBJECT( (PyObject *)tmp_for_loop_1__for_iterator );
    Py_DECREF( tmp_for_loop_1__for_iterator );
    tmp_for_loop_1__for_iterator = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto frame_exception_exit_1;
    // End of try:
    try_end_1:;

#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    // Put the previous frame back on top.
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto frame_no_exception_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif

    {
        bool needs_detach = false;

        if ( exception_tb == NULL )
        {
            exception_tb = MAKE_TRACEBACK( frame_function, exception_lineno );
            needs_detach = true;
        }
        else if ( exception_lineno != -1 )
        {
            PyTracebackObject *traceback_new = MAKE_TRACEBACK( frame_function, exception_lineno );
            traceback_new->tb_next = exception_tb;
            exception_tb = traceback_new;

            needs_detach = true;
        }

        if (needs_detach)
        {

            tmp_frame_locals = PyDict_New();
            if ( var_defused )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_defused,
                    var_defused
                );

                assert( res == 0 );
            }

            if ( var_cElementTree )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_cElementTree,
                    var_cElementTree
                );

                assert( res == 0 );
            }

            if ( var_ElementTree )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_ElementTree,
                    var_ElementTree
                );

                assert( res == 0 );
            }

            if ( var_minidom )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_minidom,
                    var_minidom
                );

                assert( res == 0 );
            }

            if ( var_pulldom )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_pulldom,
                    var_pulldom
                );

                assert( res == 0 );
            }

            if ( var_sax )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_sax,
                    var_sax
                );

                assert( res == 0 );
            }

            if ( var_expatbuilder )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_expatbuilder,
                    var_expatbuilder
                );

                assert( res == 0 );
            }

            if ( var_expatreader )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_expatreader,
                    var_expatreader
                );

                assert( res == 0 );
            }

            if ( var_xmlrpc )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_xmlrpc,
                    var_xmlrpc
                );

                assert( res == 0 );
            }

            if ( var_defused_mod )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_defused_mod,
                    var_defused_mod
                );

                assert( res == 0 );
            }

            if ( var_stdlib_mod )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_stdlib_mod,
                    var_stdlib_mod
                );

                assert( res == 0 );
            }



            detachFrame( exception_tb, tmp_frame_locals );
        }
    }

    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;

    Py_XDECREF( tmp_for_loop_1__iter_value );
    tmp_for_loop_1__iter_value = NULL;

    CHECK_OBJECT( (PyObject *)tmp_for_loop_1__for_iterator );
    Py_DECREF( tmp_for_loop_1__for_iterator );
    tmp_for_loop_1__for_iterator = NULL;

    tmp_return_value = var_defused;

    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_1_defuse_stdlib_of_defusedxml );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)var_defused );
    Py_DECREF( var_defused );
    var_defused = NULL;

    CHECK_OBJECT( (PyObject *)var_cElementTree );
    Py_DECREF( var_cElementTree );
    var_cElementTree = NULL;

    CHECK_OBJECT( (PyObject *)var_ElementTree );
    Py_DECREF( var_ElementTree );
    var_ElementTree = NULL;

    CHECK_OBJECT( (PyObject *)var_minidom );
    Py_DECREF( var_minidom );
    var_minidom = NULL;

    CHECK_OBJECT( (PyObject *)var_pulldom );
    Py_DECREF( var_pulldom );
    var_pulldom = NULL;

    CHECK_OBJECT( (PyObject *)var_sax );
    Py_DECREF( var_sax );
    var_sax = NULL;

    CHECK_OBJECT( (PyObject *)var_expatbuilder );
    Py_DECREF( var_expatbuilder );
    var_expatbuilder = NULL;

    CHECK_OBJECT( (PyObject *)var_expatreader );
    Py_DECREF( var_expatreader );
    var_expatreader = NULL;

    CHECK_OBJECT( (PyObject *)var_xmlrpc );
    Py_DECREF( var_xmlrpc );
    var_xmlrpc = NULL;

    Py_XDECREF( var_defused_mod );
    var_defused_mod = NULL;

    Py_XDECREF( var_stdlib_mod );
    var_stdlib_mod = NULL;

    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_2 = exception_type;
    exception_keeper_value_2 = exception_value;
    exception_keeper_tb_2 = exception_tb;
    exception_keeper_lineno_2 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    CHECK_OBJECT( (PyObject *)var_defused );
    Py_DECREF( var_defused );
    var_defused = NULL;

    Py_XDECREF( var_cElementTree );
    var_cElementTree = NULL;

    Py_XDECREF( var_ElementTree );
    var_ElementTree = NULL;

    Py_XDECREF( var_minidom );
    var_minidom = NULL;

    Py_XDECREF( var_pulldom );
    var_pulldom = NULL;

    Py_XDECREF( var_sax );
    var_sax = NULL;

    Py_XDECREF( var_expatbuilder );
    var_expatbuilder = NULL;

    Py_XDECREF( var_expatreader );
    var_expatreader = NULL;

    Py_XDECREF( var_xmlrpc );
    var_xmlrpc = NULL;

    Py_XDECREF( var_defused_mod );
    var_defused_mod = NULL;

    Py_XDECREF( var_stdlib_mod );
    var_stdlib_mod = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_2;
    exception_value = exception_keeper_value_2;
    exception_tb = exception_keeper_tb_2;
    exception_lineno = exception_keeper_lineno_2;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_1_defuse_stdlib_of_defusedxml );
    return NULL;

function_exception_exit:
    assert( exception_type );
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );

    return NULL;
    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}



static PyObject *MAKE_FUNCTION_function_1_defuse_stdlib_of_defusedxml(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_1_defuse_stdlib_of_defusedxml,
        const_str_plain_defuse_stdlib,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_73747dc4dbea8441e08338a54b583edc,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_defusedxml,
        const_str_digest_e511ce2b59cdfa80bd47f4ea0ed3af19
    );

    return result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_defusedxml =
{
    PyModuleDef_HEAD_INIT,
    "defusedxml",   /* m_name */
    NULL,                /* m_doc */
    -1,                  /* m_size */
    NULL,                /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#endif

#if PYTHON_VERSION >= 300
extern PyObject *metapath_based_loader;
#endif

// The exported interface to CPython. On import of the module, this function
// gets called. It has to have an exact function name, in cases it's a shared
// library export. This is hidden behind the MOD_INIT_DECL.

MOD_INIT_DECL( defusedxml )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_defusedxml );
    }
    else
    {
        _init_done = true;
    }
#endif

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    // Initialize the compiled types of Nuitka.
    PyType_Ready( &Nuitka_Generator_Type );
    PyType_Ready( &Nuitka_Function_Type );
    PyType_Ready( &Nuitka_Method_Type );
    PyType_Ready( &Nuitka_Frame_Type );
#if PYTHON_VERSION >= 350
    PyType_Ready( &Nuitka_Coroutine_Type );
    PyType_Ready( &Nuitka_CoroutineWrapper_Type );
#endif

#if PYTHON_VERSION < 300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

    // Enable meta path based loader if not already done.
    setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 300
    patchInspectModule();
#endif

#endif

    createModuleConstants();
    createModuleCodeObjects();

    // puts( "in initdefusedxml" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_defusedxml = Py_InitModule4(
        "defusedxml",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_defusedxml = PyModule_Create( &mdef_defusedxml );
#endif

    moduledict_defusedxml = (PyDictObject *)((PyModuleObject *)module_defusedxml)->md_dict;

    CHECK_OBJECT( module_defusedxml );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_plain_defusedxml, module_defusedxml );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_defusedxml );

    if ( PyDict_GetItem( module_dict, const_str_plain___builtins__ ) == NULL )
    {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then.
#if !defined(_NUITKA_EXE) || !0
        value = PyModule_GetDict( value );
#endif

#ifndef __NUITKA_NO_ASSERT__
        int res =
#endif
            PyDict_SetItem( module_dict, const_str_plain___builtins__, value );

        assert( res == 0 );
    }

#if PYTHON_VERSION >= 330
    PyDict_SetItem( module_dict, const_str_plain___loader__, metapath_based_loader );
#endif

    // Temp variables if any
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_assign_source_5;
    PyObject *tmp_assign_source_6;
    PyObject *tmp_assign_source_7;
    PyObject *tmp_assign_source_8;
    PyObject *tmp_assign_source_9;
    PyObject *tmp_assign_source_10;
    PyObject *tmp_assign_source_11;
    PyObject *tmp_assign_source_12;
    PyObject *tmp_assign_source_13;
    PyObject *tmp_called_name_1;
    PyObject *tmp_import_globals_1;
    PyObject *tmp_import_globals_2;
    PyObject *tmp_import_globals_3;
    PyObject *tmp_import_globals_4;
    PyObject *tmp_import_globals_5;
    PyObject *tmp_import_globals_6;
    PyObject *tmp_import_name_from_1;
    PyObject *tmp_import_name_from_2;
    PyObject *tmp_import_name_from_3;
    PyObject *tmp_import_name_from_4;
    PyObject *tmp_import_name_from_5;
    PyObject *tmp_import_name_from_6;
    PyObject *tmp_list_element_1;
    PyObject *tmp_source_name_1;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = const_str_digest_911922ba64bbf1ffc2f6bc469b8dcf7c;
    UPDATE_STRING_DICT0( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_ef4d69cb25300a5d946649d342683981, module_defusedxml );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    tmp_assign_source_3 = PyList_New( 1 );
    tmp_source_name_1 = PyObject_GetAttrString(PyImport_ImportModule("os"), "path");
    if ( tmp_source_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_3 );


        goto frame_exception_exit_1;
    }
    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_dirname );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_3 );


        goto frame_exception_exit_1;
    }
    tmp_args_element_name_1 = module_filename_obj;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_list_element_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    if ( tmp_list_element_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_3 );


        goto frame_exception_exit_1;
    }
    PyList_SET_ITEM( tmp_assign_source_3, 0, tmp_list_element_1 );
    UPDATE_STRING_DICT1( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain___path__, tmp_assign_source_3 );
    tmp_assign_source_4 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "print_function");
    UPDATE_STRING_DICT0( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain_print_function, tmp_assign_source_4 );
    tmp_assign_source_5 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "absolute_import");
    UPDATE_STRING_DICT0( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain_absolute_import, tmp_assign_source_5 );
    tmp_import_globals_1 = ((PyModuleObject *)module_defusedxml)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_1 = IMPORT_MODULE( const_str_plain_common, tmp_import_globals_1, tmp_import_globals_1, const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_6 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_DefusedXmlException );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain_DefusedXmlException, tmp_assign_source_6 );
    tmp_import_globals_2 = ((PyModuleObject *)module_defusedxml)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_2 = IMPORT_MODULE( const_str_plain_common, tmp_import_globals_2, tmp_import_globals_2, const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_7 = IMPORT_NAME( tmp_import_name_from_2, const_str_plain_DTDForbidden );
    Py_DECREF( tmp_import_name_from_2 );
    if ( tmp_assign_source_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain_DTDForbidden, tmp_assign_source_7 );
    tmp_import_globals_3 = ((PyModuleObject *)module_defusedxml)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_3 = IMPORT_MODULE( const_str_plain_common, tmp_import_globals_3, tmp_import_globals_3, const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_8 = IMPORT_NAME( tmp_import_name_from_3, const_str_plain_EntitiesForbidden );
    Py_DECREF( tmp_import_name_from_3 );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain_EntitiesForbidden, tmp_assign_source_8 );
    tmp_import_globals_4 = ((PyModuleObject *)module_defusedxml)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_4 = IMPORT_MODULE( const_str_plain_common, tmp_import_globals_4, tmp_import_globals_4, const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_9 = IMPORT_NAME( tmp_import_name_from_4, const_str_plain_ExternalReferenceForbidden );
    Py_DECREF( tmp_import_name_from_4 );
    if ( tmp_assign_source_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain_ExternalReferenceForbidden, tmp_assign_source_9 );
    tmp_import_globals_5 = ((PyModuleObject *)module_defusedxml)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_5 = IMPORT_MODULE( const_str_plain_common, tmp_import_globals_5, tmp_import_globals_5, const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_10 = IMPORT_NAME( tmp_import_name_from_5, const_str_plain_NotSupportedError );
    Py_DECREF( tmp_import_name_from_5 );
    if ( tmp_assign_source_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain_NotSupportedError, tmp_assign_source_10 );
    tmp_import_globals_6 = ((PyModuleObject *)module_defusedxml)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_6 = IMPORT_MODULE( const_str_plain_common, tmp_import_globals_6, tmp_import_globals_6, const_tuple_f29c767af38026b330b5b58ed5c73ee7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_11 = IMPORT_NAME( tmp_import_name_from_6, const_str_plain__apply_defusing );
    Py_DECREF( tmp_import_name_from_6 );
    if ( tmp_assign_source_11 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain__apply_defusing, tmp_assign_source_11 );

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION( frame_module );
#endif
    popFrameStack();

    assertFrameObject( frame_module );
    Py_DECREF( frame_module );

    goto frame_no_exception_1;
    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_module );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( frame_module, exception_lineno );
    }
    else if ( exception_tb->tb_frame != frame_module )
    {
        PyTracebackObject *traceback_new = MAKE_TRACEBACK( frame_module, exception_lineno );
        traceback_new->tb_next = exception_tb;
        exception_tb = traceback_new;
    }

    // Put the previous frame back on top.
    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_module->f_executing -= 1;
#endif
    Py_DECREF( frame_module );

    // Return the error.
    goto module_exception_exit;
    frame_no_exception_1:;
    tmp_assign_source_12 = MAKE_FUNCTION_function_1_defuse_stdlib_of_defusedxml(  );
    UPDATE_STRING_DICT1( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain_defuse_stdlib, tmp_assign_source_12 );
    tmp_assign_source_13 = const_str_digest_0127e46389ddf931f646f7560f89d11f;
    UPDATE_STRING_DICT0( moduledict_defusedxml, (Nuitka_StringObject *)const_str_plain___version__, tmp_assign_source_13 );

    return MOD_RETURN_VALUE( module_defusedxml );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
