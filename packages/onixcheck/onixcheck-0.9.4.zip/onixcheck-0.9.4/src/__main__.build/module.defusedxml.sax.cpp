/* Generated code for Python source for module 'defusedxml.sax'
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

/* The _module_defusedxml$sax is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_defusedxml$sax;
PyDictObject *moduledict_defusedxml$sax;

/* The module constants used, if any. */
extern PyObject *const_str_plain_forbid_dtd;
extern PyObject *const_str_plain_string;
static PyObject *const_str_plain__ErrorHandler;
extern PyObject *const_str_digest_b221566cfc22cd32d3072a27784bd7c3;
extern PyObject *const_str_plain_parser_list;
extern PyObject *const_str_plain_setErrorHandler;
extern PyObject *const_int_0;
static PyObject *const_str_digest_11e1a239f7df9c6b9f5530933f13d781;
extern PyObject *const_dict_empty;
static PyObject *const_str_plain__InputSource;
extern PyObject *const_tuple_str_plain_InputSource_tuple;
extern PyObject *const_str_plain_absolute_import;
extern PyObject *const_str_plain_parse;
static PyObject *const_str_digest_9221faca58cf379305dd3576242d9789;
extern PyObject *const_tuple_str_plain_BytesIO_tuple;
extern PyObject *const_tuple_empty;
extern PyObject *const_str_plain_forbid_entities;
extern PyObject *const_str_plain_InputSource;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_parseString;
extern PyObject *const_tuple_str_plain_expatreader_tuple;
extern PyObject *const_str_plain_make_parser;
extern PyObject *const_str_plain_setContentHandler;
extern PyObject *const_str_plain___file__;
extern PyObject *const_str_plain___origin__;
extern PyObject *const_str_plain_io;
extern PyObject *const_str_plain_parser;
static PyObject *const_tuple_ef036272094fed18af040facbd049694_tuple;
extern PyObject *const_str_plain_setByteStream;
extern PyObject *const_int_pos_1;
extern PyObject *const_str_empty;
static PyObject *const_tuple_5f6fdd0d148944765feb1510191d0f25_tuple;
extern PyObject *const_str_plain_errorHandler;
static PyObject *const_str_digest_21c47637add2892ce9bef3fdf89a7018;
static PyObject *const_tuple_str_plain_parser_list_tuple;
extern PyObject *const_str_plain_inpsrc;
extern PyObject *const_str_plain_BytesIO;
extern PyObject *const_str_plain_create_parser;
extern PyObject *const_str_plain_forbid_external;
static PyObject *const_tuple_str_plain_ErrorHandler_tuple;
extern PyObject *const_str_plain_print_function;
extern PyObject *const_str_plain_source;
extern PyObject *const_str_plain_ErrorHandler;
extern PyObject *const_str_plain_expatreader;
extern PyObject *const_str_plain_sax;
extern PyObject *const_str_plain_handler;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_plain__ErrorHandler = UNSTREAM_STRING( &constant_bin[ 221292 ], 13, 1 );
    const_str_digest_11e1a239f7df9c6b9f5530933f13d781 = UNSTREAM_STRING( &constant_bin[ 221305 ], 14, 0 );
    const_str_plain__InputSource = UNSTREAM_STRING( &constant_bin[ 221319 ], 12, 1 );
    const_str_digest_9221faca58cf379305dd3576242d9789 = UNSTREAM_STRING( &constant_bin[ 221331 ], 17, 0 );
    const_tuple_ef036272094fed18af040facbd049694_tuple = PyTuple_New( 7 );
    PyTuple_SET_ITEM( const_tuple_ef036272094fed18af040facbd049694_tuple, 0, const_str_plain_source ); Py_INCREF( const_str_plain_source );
    PyTuple_SET_ITEM( const_tuple_ef036272094fed18af040facbd049694_tuple, 1, const_str_plain_handler ); Py_INCREF( const_str_plain_handler );
    PyTuple_SET_ITEM( const_tuple_ef036272094fed18af040facbd049694_tuple, 2, const_str_plain_errorHandler ); Py_INCREF( const_str_plain_errorHandler );
    PyTuple_SET_ITEM( const_tuple_ef036272094fed18af040facbd049694_tuple, 3, const_str_plain_forbid_dtd ); Py_INCREF( const_str_plain_forbid_dtd );
    PyTuple_SET_ITEM( const_tuple_ef036272094fed18af040facbd049694_tuple, 4, const_str_plain_forbid_entities ); Py_INCREF( const_str_plain_forbid_entities );
    PyTuple_SET_ITEM( const_tuple_ef036272094fed18af040facbd049694_tuple, 5, const_str_plain_forbid_external ); Py_INCREF( const_str_plain_forbid_external );
    PyTuple_SET_ITEM( const_tuple_ef036272094fed18af040facbd049694_tuple, 6, const_str_plain_parser ); Py_INCREF( const_str_plain_parser );
    const_tuple_5f6fdd0d148944765feb1510191d0f25_tuple = PyTuple_New( 9 );
    PyTuple_SET_ITEM( const_tuple_5f6fdd0d148944765feb1510191d0f25_tuple, 0, const_str_plain_string ); Py_INCREF( const_str_plain_string );
    PyTuple_SET_ITEM( const_tuple_5f6fdd0d148944765feb1510191d0f25_tuple, 1, const_str_plain_handler ); Py_INCREF( const_str_plain_handler );
    PyTuple_SET_ITEM( const_tuple_5f6fdd0d148944765feb1510191d0f25_tuple, 2, const_str_plain_errorHandler ); Py_INCREF( const_str_plain_errorHandler );
    PyTuple_SET_ITEM( const_tuple_5f6fdd0d148944765feb1510191d0f25_tuple, 3, const_str_plain_forbid_dtd ); Py_INCREF( const_str_plain_forbid_dtd );
    PyTuple_SET_ITEM( const_tuple_5f6fdd0d148944765feb1510191d0f25_tuple, 4, const_str_plain_forbid_entities ); Py_INCREF( const_str_plain_forbid_entities );
    PyTuple_SET_ITEM( const_tuple_5f6fdd0d148944765feb1510191d0f25_tuple, 5, const_str_plain_forbid_external ); Py_INCREF( const_str_plain_forbid_external );
    PyTuple_SET_ITEM( const_tuple_5f6fdd0d148944765feb1510191d0f25_tuple, 6, const_str_plain_BytesIO ); Py_INCREF( const_str_plain_BytesIO );
    PyTuple_SET_ITEM( const_tuple_5f6fdd0d148944765feb1510191d0f25_tuple, 7, const_str_plain_parser ); Py_INCREF( const_str_plain_parser );
    PyTuple_SET_ITEM( const_tuple_5f6fdd0d148944765feb1510191d0f25_tuple, 8, const_str_plain_inpsrc ); Py_INCREF( const_str_plain_inpsrc );
    const_str_digest_21c47637add2892ce9bef3fdf89a7018 = UNSTREAM_STRING( &constant_bin[ 221348 ], 16, 0 );
    const_tuple_str_plain_parser_list_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_parser_list_tuple, 0, const_str_plain_parser_list ); Py_INCREF( const_str_plain_parser_list );
    const_tuple_str_plain_ErrorHandler_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_ErrorHandler_tuple, 0, const_str_plain_ErrorHandler ); Py_INCREF( const_str_plain_ErrorHandler );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_defusedxml$sax( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_32479c9cf8a3d37e048103a8e24f0331;
static PyCodeObject *codeobj_7f79f620d0429d5af3d62c8855b7b9f6;
static PyCodeObject *codeobj_4662b32e263e7cd5cd58d3786c061df0;
static PyCodeObject *codeobj_131a6811afec198dcd851a88ca609d85;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_9221faca58cf379305dd3576242d9789 );
    codeobj_32479c9cf8a3d37e048103a8e24f0331 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_make_parser, 46, const_tuple_str_plain_parser_list_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_PRINT_FUNCTION );
    codeobj_7f79f620d0429d5af3d62c8855b7b9f6 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_parse, 17, const_tuple_ef036272094fed18af040facbd049694_tuple, 6, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_PRINT_FUNCTION );
    codeobj_4662b32e263e7cd5cd58d3786c061df0 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_parseString, 28, const_tuple_5f6fdd0d148944765feb1510191d0f25_tuple, 6, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_PRINT_FUNCTION );
    codeobj_131a6811afec198dcd851a88ca609d85 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_sax, 1, const_tuple_empty, 0, CO_NOFREE | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_PRINT_FUNCTION );
}

// The module function declarations.
static PyObject *MAKE_FUNCTION_function_1_parse_of_defusedxml$sax( PyObject *defaults );


static PyObject *MAKE_FUNCTION_function_2_parseString_of_defusedxml$sax( PyObject *defaults );


static PyObject *MAKE_FUNCTION_function_3_make_parser_of_defusedxml$sax( PyObject *defaults );


// The module function definitions.
static PyObject *impl_function_1_parse_of_defusedxml$sax( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_source = python_pars[ 0 ];
    PyObject *par_handler = python_pars[ 1 ];
    PyObject *par_errorHandler = python_pars[ 2 ];
    PyObject *par_forbid_dtd = python_pars[ 3 ];
    PyObject *par_forbid_entities = python_pars[ 4 ];
    PyObject *par_forbid_external = python_pars[ 5 ];
    PyObject *var_parser = NULL;
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_args_element_name_3;
    PyObject *tmp_assattr_name_1;
    PyObject *tmp_assattr_name_2;
    PyObject *tmp_assattr_name_3;
    PyObject *tmp_assattr_target_1;
    PyObject *tmp_assattr_target_2;
    PyObject *tmp_assattr_target_3;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_called_name_4;
    PyObject *tmp_frame_locals;
    bool tmp_result;
    PyObject *tmp_return_value;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_7f79f620d0429d5af3d62c8855b7b9f6, module_defusedxml$sax );
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
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain_make_parser );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_make_parser );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "make_parser" );
        exception_tb = NULL;

        exception_lineno = 19;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 19;
    tmp_assign_source_1 = CALL_FUNCTION_NO_ARGS( tmp_called_name_1 );
    if ( tmp_assign_source_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 19;
        goto frame_exception_exit_1;
    }
    assert( var_parser == NULL );
    var_parser = tmp_assign_source_1;

    tmp_source_name_1 = var_parser;

    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_setContentHandler );
    if ( tmp_called_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 20;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_1 = par_handler;

    frame_function->f_lineno = 20;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_2, call_args );
    }

    Py_DECREF( tmp_called_name_2 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 20;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_source_name_2 = var_parser;

    tmp_called_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_setErrorHandler );
    if ( tmp_called_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 21;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_2 = par_errorHandler;

    frame_function->f_lineno = 21;
    {
        PyObject *call_args[] = { tmp_args_element_name_2 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_3, call_args );
    }

    Py_DECREF( tmp_called_name_3 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 21;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_assattr_name_1 = par_forbid_dtd;

    tmp_assattr_target_1 = var_parser;

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_1, const_str_plain_forbid_dtd, tmp_assattr_name_1 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 22;
        goto frame_exception_exit_1;
    }
    tmp_assattr_name_2 = par_forbid_entities;

    tmp_assattr_target_2 = var_parser;

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_2, const_str_plain_forbid_entities, tmp_assattr_name_2 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 23;
        goto frame_exception_exit_1;
    }
    tmp_assattr_name_3 = par_forbid_external;

    tmp_assattr_target_3 = var_parser;

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_3, const_str_plain_forbid_external, tmp_assattr_name_3 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 24;
        goto frame_exception_exit_1;
    }
    tmp_source_name_3 = var_parser;

    tmp_called_name_4 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_parse );
    if ( tmp_called_name_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 25;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_3 = par_source;

    frame_function->f_lineno = 25;
    {
        PyObject *call_args[] = { tmp_args_element_name_3 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_4, call_args );
    }

    Py_DECREF( tmp_called_name_4 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 25;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );

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
            if ( par_source )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_source,
                    par_source
                );

                assert( res == 0 );
            }

            if ( par_handler )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_handler,
                    par_handler
                );

                assert( res == 0 );
            }

            if ( par_errorHandler )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_errorHandler,
                    par_errorHandler
                );

                assert( res == 0 );
            }

            if ( par_forbid_dtd )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_forbid_dtd,
                    par_forbid_dtd
                );

                assert( res == 0 );
            }

            if ( par_forbid_entities )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_forbid_entities,
                    par_forbid_entities
                );

                assert( res == 0 );
            }

            if ( par_forbid_external )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_forbid_external,
                    par_forbid_external
                );

                assert( res == 0 );
            }

            if ( var_parser )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_parser,
                    var_parser
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

    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_1_parse_of_defusedxml$sax );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_source );
    Py_DECREF( par_source );
    par_source = NULL;

    CHECK_OBJECT( (PyObject *)par_handler );
    Py_DECREF( par_handler );
    par_handler = NULL;

    CHECK_OBJECT( (PyObject *)par_errorHandler );
    Py_DECREF( par_errorHandler );
    par_errorHandler = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_dtd );
    Py_DECREF( par_forbid_dtd );
    par_forbid_dtd = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_entities );
    Py_DECREF( par_forbid_entities );
    par_forbid_entities = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_external );
    Py_DECREF( par_forbid_external );
    par_forbid_external = NULL;

    CHECK_OBJECT( (PyObject *)var_parser );
    Py_DECREF( var_parser );
    var_parser = NULL;

    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    CHECK_OBJECT( (PyObject *)par_source );
    Py_DECREF( par_source );
    par_source = NULL;

    CHECK_OBJECT( (PyObject *)par_handler );
    Py_DECREF( par_handler );
    par_handler = NULL;

    CHECK_OBJECT( (PyObject *)par_errorHandler );
    Py_DECREF( par_errorHandler );
    par_errorHandler = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_dtd );
    Py_DECREF( par_forbid_dtd );
    par_forbid_dtd = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_entities );
    Py_DECREF( par_forbid_entities );
    par_forbid_entities = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_external );
    Py_DECREF( par_forbid_external );
    par_forbid_external = NULL;

    Py_XDECREF( var_parser );
    var_parser = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_1_parse_of_defusedxml$sax );
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


static PyObject *impl_function_2_parseString_of_defusedxml$sax( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_string = python_pars[ 0 ];
    PyObject *par_handler = python_pars[ 1 ];
    PyObject *par_errorHandler = python_pars[ 2 ];
    PyObject *par_forbid_dtd = python_pars[ 3 ];
    PyObject *par_forbid_entities = python_pars[ 4 ];
    PyObject *par_forbid_external = python_pars[ 5 ];
    PyObject *var_BytesIO = NULL;
    PyObject *var_parser = NULL;
    PyObject *var_inpsrc = NULL;
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_args_element_name_3;
    PyObject *tmp_args_element_name_4;
    PyObject *tmp_args_element_name_5;
    PyObject *tmp_assattr_name_1;
    PyObject *tmp_assattr_name_2;
    PyObject *tmp_assattr_name_3;
    PyObject *tmp_assattr_target_1;
    PyObject *tmp_assattr_target_2;
    PyObject *tmp_assattr_target_3;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_called_name_4;
    PyObject *tmp_called_name_5;
    PyObject *tmp_called_name_6;
    PyObject *tmp_called_name_7;
    PyObject *tmp_called_name_8;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_import_globals_1;
    PyObject *tmp_import_locals_1;
    PyObject *tmp_import_name_from_1;
    bool tmp_is_1;
    bool tmp_result;
    PyObject *tmp_return_value;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    PyObject *tmp_source_name_4;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_4662b32e263e7cd5cd58d3786c061df0, module_defusedxml$sax );
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
    tmp_import_globals_1 = ((PyModuleObject *)module_defusedxml$sax)->md_dict;
    tmp_import_locals_1 = PyDict_New();
    if ( par_string )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_string,
            par_string
        );

        assert( res == 0 );
    }

    if ( par_handler )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_handler,
            par_handler
        );

        assert( res == 0 );
    }

    if ( par_errorHandler )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_errorHandler,
            par_errorHandler
        );

        assert( res == 0 );
    }

    if ( par_forbid_dtd )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_forbid_dtd,
            par_forbid_dtd
        );

        assert( res == 0 );
    }

    if ( par_forbid_entities )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_forbid_entities,
            par_forbid_entities
        );

        assert( res == 0 );
    }

    if ( par_forbid_external )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_forbid_external,
            par_forbid_external
        );

        assert( res == 0 );
    }

    if ( var_BytesIO )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_BytesIO,
            var_BytesIO
        );

        assert( res == 0 );
    }

    if ( var_parser )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_parser,
            var_parser
        );

        assert( res == 0 );
    }

    if ( var_inpsrc )
    {
        int res = PyDict_SetItem(
            tmp_import_locals_1,
            const_str_plain_inpsrc,
            var_inpsrc
        );

        assert( res == 0 );
    }

    frame_function->f_lineno = 31;
    tmp_import_name_from_1 = IMPORT_MODULE( const_str_plain_io, tmp_import_globals_1, tmp_import_locals_1, const_tuple_str_plain_BytesIO_tuple, const_int_0 );
    Py_DECREF( tmp_import_locals_1 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 31;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_1 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_BytesIO );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 31;
        goto frame_exception_exit_1;
    }
    assert( var_BytesIO == NULL );
    var_BytesIO = tmp_assign_source_1;

    tmp_compare_left_1 = par_errorHandler;

    tmp_compare_right_1 = Py_None;
    tmp_is_1 = ( tmp_compare_left_1 == tmp_compare_right_1 );
    if ( tmp_is_1 )
    {
        goto branch_yes_1;
    }
    else
    {
        goto branch_no_1;
    }
    branch_yes_1:;
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain__ErrorHandler );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__ErrorHandler );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "_ErrorHandler" );
        exception_tb = NULL;

        exception_lineno = 34;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 34;
    tmp_assign_source_2 = CALL_FUNCTION_NO_ARGS( tmp_called_name_1 );
    if ( tmp_assign_source_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    {
        PyObject *old = par_errorHandler;
        assert( old != NULL );
        par_errorHandler = tmp_assign_source_2;
        Py_DECREF( old );
    }

    branch_no_1:;
    tmp_called_name_2 = GET_STRING_DICT_VALUE( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain_make_parser );

    if (unlikely( tmp_called_name_2 == NULL ))
    {
        tmp_called_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_make_parser );
    }

    if ( tmp_called_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "make_parser" );
        exception_tb = NULL;

        exception_lineno = 35;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 35;
    tmp_assign_source_3 = CALL_FUNCTION_NO_ARGS( tmp_called_name_2 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 35;
        goto frame_exception_exit_1;
    }
    assert( var_parser == NULL );
    var_parser = tmp_assign_source_3;

    tmp_source_name_1 = var_parser;

    tmp_called_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_setContentHandler );
    if ( tmp_called_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 36;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_1 = par_handler;

    frame_function->f_lineno = 36;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_3, call_args );
    }

    Py_DECREF( tmp_called_name_3 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 36;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_source_name_2 = var_parser;

    tmp_called_name_4 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_setErrorHandler );
    if ( tmp_called_name_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 37;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_2 = par_errorHandler;

    frame_function->f_lineno = 37;
    {
        PyObject *call_args[] = { tmp_args_element_name_2 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_4, call_args );
    }

    Py_DECREF( tmp_called_name_4 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 37;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_assattr_name_1 = par_forbid_dtd;

    tmp_assattr_target_1 = var_parser;

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_1, const_str_plain_forbid_dtd, tmp_assattr_name_1 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 38;
        goto frame_exception_exit_1;
    }
    tmp_assattr_name_2 = par_forbid_entities;

    tmp_assattr_target_2 = var_parser;

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_2, const_str_plain_forbid_entities, tmp_assattr_name_2 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 39;
        goto frame_exception_exit_1;
    }
    tmp_assattr_name_3 = par_forbid_external;

    tmp_assattr_target_3 = var_parser;

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_3, const_str_plain_forbid_external, tmp_assattr_name_3 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 40;
        goto frame_exception_exit_1;
    }
    tmp_called_name_5 = GET_STRING_DICT_VALUE( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain__InputSource );

    if (unlikely( tmp_called_name_5 == NULL ))
    {
        tmp_called_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__InputSource );
    }

    if ( tmp_called_name_5 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "_InputSource" );
        exception_tb = NULL;

        exception_lineno = 42;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 42;
    tmp_assign_source_4 = CALL_FUNCTION_NO_ARGS( tmp_called_name_5 );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 42;
        goto frame_exception_exit_1;
    }
    assert( var_inpsrc == NULL );
    var_inpsrc = tmp_assign_source_4;

    tmp_source_name_3 = var_inpsrc;

    tmp_called_name_6 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_setByteStream );
    if ( tmp_called_name_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 43;
        goto frame_exception_exit_1;
    }
    tmp_called_name_7 = var_BytesIO;

    tmp_args_element_name_4 = par_string;

    frame_function->f_lineno = 43;
    {
        PyObject *call_args[] = { tmp_args_element_name_4 };
        tmp_args_element_name_3 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_7, call_args );
    }

    if ( tmp_args_element_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_6 );

        exception_lineno = 43;
        goto frame_exception_exit_1;
    }
    frame_function->f_lineno = 43;
    {
        PyObject *call_args[] = { tmp_args_element_name_3 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_6, call_args );
    }

    Py_DECREF( tmp_called_name_6 );
    Py_DECREF( tmp_args_element_name_3 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 43;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_source_name_4 = var_parser;

    tmp_called_name_8 = LOOKUP_ATTRIBUTE( tmp_source_name_4, const_str_plain_parse );
    if ( tmp_called_name_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 44;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_5 = var_inpsrc;

    frame_function->f_lineno = 44;
    {
        PyObject *call_args[] = { tmp_args_element_name_5 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_8, call_args );
    }

    Py_DECREF( tmp_called_name_8 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 44;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );

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
            if ( par_string )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_string,
                    par_string
                );

                assert( res == 0 );
            }

            if ( par_handler )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_handler,
                    par_handler
                );

                assert( res == 0 );
            }

            if ( par_errorHandler )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_errorHandler,
                    par_errorHandler
                );

                assert( res == 0 );
            }

            if ( par_forbid_dtd )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_forbid_dtd,
                    par_forbid_dtd
                );

                assert( res == 0 );
            }

            if ( par_forbid_entities )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_forbid_entities,
                    par_forbid_entities
                );

                assert( res == 0 );
            }

            if ( par_forbid_external )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_forbid_external,
                    par_forbid_external
                );

                assert( res == 0 );
            }

            if ( var_BytesIO )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_BytesIO,
                    var_BytesIO
                );

                assert( res == 0 );
            }

            if ( var_parser )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_parser,
                    var_parser
                );

                assert( res == 0 );
            }

            if ( var_inpsrc )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_inpsrc,
                    var_inpsrc
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

    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_2_parseString_of_defusedxml$sax );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_string );
    Py_DECREF( par_string );
    par_string = NULL;

    CHECK_OBJECT( (PyObject *)par_handler );
    Py_DECREF( par_handler );
    par_handler = NULL;

    CHECK_OBJECT( (PyObject *)par_errorHandler );
    Py_DECREF( par_errorHandler );
    par_errorHandler = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_dtd );
    Py_DECREF( par_forbid_dtd );
    par_forbid_dtd = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_entities );
    Py_DECREF( par_forbid_entities );
    par_forbid_entities = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_external );
    Py_DECREF( par_forbid_external );
    par_forbid_external = NULL;

    CHECK_OBJECT( (PyObject *)var_BytesIO );
    Py_DECREF( var_BytesIO );
    var_BytesIO = NULL;

    CHECK_OBJECT( (PyObject *)var_parser );
    Py_DECREF( var_parser );
    var_parser = NULL;

    CHECK_OBJECT( (PyObject *)var_inpsrc );
    Py_DECREF( var_inpsrc );
    var_inpsrc = NULL;

    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    CHECK_OBJECT( (PyObject *)par_string );
    Py_DECREF( par_string );
    par_string = NULL;

    CHECK_OBJECT( (PyObject *)par_handler );
    Py_DECREF( par_handler );
    par_handler = NULL;

    Py_XDECREF( par_errorHandler );
    par_errorHandler = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_dtd );
    Py_DECREF( par_forbid_dtd );
    par_forbid_dtd = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_entities );
    Py_DECREF( par_forbid_entities );
    par_forbid_entities = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_external );
    Py_DECREF( par_forbid_external );
    par_forbid_external = NULL;

    Py_XDECREF( var_BytesIO );
    var_BytesIO = NULL;

    Py_XDECREF( var_parser );
    var_parser = NULL;

    Py_XDECREF( var_inpsrc );
    var_inpsrc = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_2_parseString_of_defusedxml$sax );
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


static PyObject *impl_function_3_make_parser_of_defusedxml$sax( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_parser_list = python_pars[ 0 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    PyObject *tmp_source_name_1;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_32479c9cf8a3d37e048103a8e24f0331, module_defusedxml$sax );
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
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain_expatreader );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_expatreader );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "expatreader" );
        exception_tb = NULL;

        exception_lineno = 47;
        goto frame_exception_exit_1;
    }

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_create_parser );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 47;
        goto frame_exception_exit_1;
    }
    frame_function->f_lineno = 47;
    tmp_return_value = CALL_FUNCTION_NO_ARGS( tmp_called_name_1 );
    Py_DECREF( tmp_called_name_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 47;
        goto frame_exception_exit_1;
    }
    goto frame_return_exit_1;

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

    frame_return_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto try_return_handler_1;

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
            if ( par_parser_list )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_parser_list,
                    par_parser_list
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

    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_3_make_parser_of_defusedxml$sax );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_parser_list );
    Py_DECREF( par_parser_list );
    par_parser_list = NULL;

    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    CHECK_OBJECT( (PyObject *)par_parser_list );
    Py_DECREF( par_parser_list );
    par_parser_list = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_3_make_parser_of_defusedxml$sax );
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



static PyObject *MAKE_FUNCTION_function_1_parse_of_defusedxml$sax( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_1_parse_of_defusedxml$sax,
        const_str_plain_parse,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_7f79f620d0429d5af3d62c8855b7b9f6,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_defusedxml$sax,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_2_parseString_of_defusedxml$sax( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_2_parseString_of_defusedxml$sax,
        const_str_plain_parseString,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_4662b32e263e7cd5cd58d3786c061df0,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_defusedxml$sax,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_3_make_parser_of_defusedxml$sax( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_3_make_parser_of_defusedxml$sax,
        const_str_plain_make_parser,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_32479c9cf8a3d37e048103a8e24f0331,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_defusedxml$sax,
        Py_None
    );

    return result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_defusedxml$sax =
{
    PyModuleDef_HEAD_INIT,
    "defusedxml.sax",   /* m_name */
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

MOD_INIT_DECL( defusedxml$sax )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_defusedxml$sax );
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

    // puts( "in initdefusedxml$sax" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_defusedxml$sax = Py_InitModule4(
        "defusedxml.sax",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_defusedxml$sax = PyModule_Create( &mdef_defusedxml$sax );
#endif

    moduledict_defusedxml$sax = (PyDictObject *)((PyModuleObject *)module_defusedxml$sax)->md_dict;

    CHECK_OBJECT( module_defusedxml$sax );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_digest_11e1a239f7df9c6b9f5530933f13d781, module_defusedxml$sax );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_defusedxml$sax );

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
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_defaults_1;
    PyObject *tmp_defaults_2;
    PyObject *tmp_defaults_3;
    PyObject *tmp_import_globals_1;
    PyObject *tmp_import_globals_2;
    PyObject *tmp_import_globals_3;
    PyObject *tmp_import_name_from_1;
    PyObject *tmp_import_name_from_2;
    PyObject *tmp_import_name_from_3;
    PyObject *tmp_tuple_element_1;
    PyObject *tmp_tuple_element_2;
    PyObject *tmp_tuple_element_3;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = const_str_digest_21c47637add2892ce9bef3fdf89a7018;
    UPDATE_STRING_DICT0( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_assign_source_3 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "print_function");
    UPDATE_STRING_DICT0( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain_print_function, tmp_assign_source_3 );
    tmp_assign_source_4 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "absolute_import");
    UPDATE_STRING_DICT0( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain_absolute_import, tmp_assign_source_4 );
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_131a6811afec198dcd851a88ca609d85, module_defusedxml$sax );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    tmp_import_globals_1 = ((PyModuleObject *)module_defusedxml$sax)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_1 = IMPORT_MODULE( const_str_digest_b221566cfc22cd32d3072a27784bd7c3, tmp_import_globals_1, tmp_import_globals_1, const_tuple_str_plain_InputSource_tuple, const_int_0 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_5 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_InputSource );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain__InputSource, tmp_assign_source_5 );
    tmp_import_globals_2 = ((PyModuleObject *)module_defusedxml$sax)->md_dict;
    frame_module->f_lineno = 11;
    tmp_import_name_from_2 = IMPORT_MODULE( const_str_digest_b221566cfc22cd32d3072a27784bd7c3, tmp_import_globals_2, tmp_import_globals_2, const_tuple_str_plain_ErrorHandler_tuple, const_int_0 );
    if ( tmp_import_name_from_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 11;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_6 = IMPORT_NAME( tmp_import_name_from_2, const_str_plain_ErrorHandler );
    Py_DECREF( tmp_import_name_from_2 );
    if ( tmp_assign_source_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 11;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain__ErrorHandler, tmp_assign_source_6 );
    tmp_import_globals_3 = ((PyModuleObject *)module_defusedxml$sax)->md_dict;
    frame_module->f_lineno = 13;
    tmp_import_name_from_3 = IMPORT_MODULE( const_str_empty, tmp_import_globals_3, tmp_import_globals_3, const_tuple_str_plain_expatreader_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 13;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_7 = IMPORT_NAME( tmp_import_name_from_3, const_str_plain_expatreader );
    Py_DECREF( tmp_import_name_from_3 );
    if ( tmp_assign_source_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 13;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain_expatreader, tmp_assign_source_7 );
    tmp_assign_source_8 = const_str_digest_b221566cfc22cd32d3072a27784bd7c3;
    UPDATE_STRING_DICT0( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain___origin__, tmp_assign_source_8 );
    tmp_defaults_1 = PyTuple_New( 4 );
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain__ErrorHandler );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__ErrorHandler );
    }

    if ( tmp_called_name_1 == NULL )
    {
        Py_DECREF( tmp_defaults_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "_ErrorHandler" );
        exception_tb = NULL;

        exception_lineno = 17;
        goto frame_exception_exit_1;
    }

    frame_module->f_lineno = 17;
    tmp_tuple_element_1 = CALL_FUNCTION_NO_ARGS( tmp_called_name_1 );
    if ( tmp_tuple_element_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_defaults_1 );

        exception_lineno = 17;
        goto frame_exception_exit_1;
    }
    PyTuple_SET_ITEM( tmp_defaults_1, 0, tmp_tuple_element_1 );
    tmp_tuple_element_1 = Py_False;
    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_defaults_1, 1, tmp_tuple_element_1 );
    tmp_tuple_element_1 = Py_True;
    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_defaults_1, 2, tmp_tuple_element_1 );
    tmp_tuple_element_1 = Py_True;
    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_defaults_1, 3, tmp_tuple_element_1 );
    tmp_assign_source_9 = MAKE_FUNCTION_function_1_parse_of_defusedxml$sax( tmp_defaults_1 );
    UPDATE_STRING_DICT1( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain_parse, tmp_assign_source_9 );
    tmp_defaults_2 = PyTuple_New( 4 );
    tmp_called_name_2 = GET_STRING_DICT_VALUE( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain__ErrorHandler );

    if (unlikely( tmp_called_name_2 == NULL ))
    {
        tmp_called_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__ErrorHandler );
    }

    if ( tmp_called_name_2 == NULL )
    {
        Py_DECREF( tmp_defaults_2 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "_ErrorHandler" );
        exception_tb = NULL;

        exception_lineno = 28;
        goto frame_exception_exit_1;
    }

    frame_module->f_lineno = 28;
    tmp_tuple_element_2 = CALL_FUNCTION_NO_ARGS( tmp_called_name_2 );
    if ( tmp_tuple_element_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_defaults_2 );

        exception_lineno = 28;
        goto frame_exception_exit_1;
    }
    PyTuple_SET_ITEM( tmp_defaults_2, 0, tmp_tuple_element_2 );
    tmp_tuple_element_2 = Py_False;
    Py_INCREF( tmp_tuple_element_2 );
    PyTuple_SET_ITEM( tmp_defaults_2, 1, tmp_tuple_element_2 );
    tmp_tuple_element_2 = Py_True;
    Py_INCREF( tmp_tuple_element_2 );
    PyTuple_SET_ITEM( tmp_defaults_2, 2, tmp_tuple_element_2 );
    tmp_tuple_element_2 = Py_True;
    Py_INCREF( tmp_tuple_element_2 );
    PyTuple_SET_ITEM( tmp_defaults_2, 3, tmp_tuple_element_2 );
    tmp_assign_source_10 = MAKE_FUNCTION_function_2_parseString_of_defusedxml$sax( tmp_defaults_2 );
    UPDATE_STRING_DICT1( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain_parseString, tmp_assign_source_10 );

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
    tmp_defaults_3 = PyTuple_New( 1 );
    tmp_tuple_element_3 = PyList_New( 0 );
    PyTuple_SET_ITEM( tmp_defaults_3, 0, tmp_tuple_element_3 );
    tmp_assign_source_11 = MAKE_FUNCTION_function_3_make_parser_of_defusedxml$sax( tmp_defaults_3 );
    UPDATE_STRING_DICT1( moduledict_defusedxml$sax, (Nuitka_StringObject *)const_str_plain_make_parser, tmp_assign_source_11 );

    return MOD_RETURN_VALUE( module_defusedxml$sax );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
