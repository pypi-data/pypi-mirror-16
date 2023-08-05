/* Generated code for Python source for module 'defusedxml.pulldom'
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

/* The _module_defusedxml$pulldom is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_defusedxml$pulldom;
PyDictObject *moduledict_defusedxml$pulldom;

/* The module constants used, if any. */
extern PyObject *const_str_plain_forbid_dtd;
extern PyObject *const_str_digest_ca8102e928c8c9d3d46859f5f9518ed8;
extern PyObject *const_str_plain_string;
extern PyObject *const_tuple_str_plain_parseString_tuple;
static PyObject *const_str_digest_5093870bf554b260d37d6b0e0bfbc00e;
static PyObject *const_str_plain__parseString;
extern PyObject *const_tuple_none_false_true_true_tuple;
extern PyObject *const_tuple_empty;
extern PyObject *const_dict_empty;
extern PyObject *const_str_plain_pulldom;
extern PyObject *const_str_plain_absolute_import;
extern PyObject *const_str_plain_parse;
extern PyObject *const_str_plain_sax;
extern PyObject *const_str_plain_make_parser;
extern PyObject *const_str_plain_forbid_entities;
extern PyObject *const_str_plain__parse;
static PyObject *const_tuple_str_plain_make_parser_tuple;
static PyObject *const_str_digest_608c0e8034f5755cebb7f326fbc6c185;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_parseString;
extern PyObject *const_int_0;
extern PyObject *const_tuple_none_none_false_true_true_tuple;
extern PyObject *const_tuple_str_plain_parse_tuple;
extern PyObject *const_str_plain___file__;
extern PyObject *const_str_plain___origin__;
extern PyObject *const_str_plain_parser;
static PyObject *const_tuple_d9f994044d161e4110f9cc0762af03f2_tuple;
extern PyObject *const_int_pos_1;
static PyObject *const_str_digest_4dde434bd2c5c7a4395d42c157f28b0b;
extern PyObject *const_str_plain_stream_or_string;
extern PyObject *const_str_plain_forbid_external;
extern PyObject *const_str_plain_print_function;
extern PyObject *const_str_plain_bufsize;
extern PyObject *const_tuple_ad156ecd6a482ca6ef2bca0bda398c70_tuple;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_digest_5093870bf554b260d37d6b0e0bfbc00e = UNSTREAM_STRING( &constant_bin[ 221217 ], 21, 0 );
    const_str_plain__parseString = UNSTREAM_STRING( &constant_bin[ 221238 ], 12, 1 );
    const_tuple_str_plain_make_parser_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_make_parser_tuple, 0, const_str_plain_make_parser ); Py_INCREF( const_str_plain_make_parser );
    const_str_digest_608c0e8034f5755cebb7f326fbc6c185 = UNSTREAM_STRING( &constant_bin[ 221250 ], 24, 0 );
    const_tuple_d9f994044d161e4110f9cc0762af03f2_tuple = PyTuple_New( 6 );
    PyTuple_SET_ITEM( const_tuple_d9f994044d161e4110f9cc0762af03f2_tuple, 0, const_str_plain_stream_or_string ); Py_INCREF( const_str_plain_stream_or_string );
    PyTuple_SET_ITEM( const_tuple_d9f994044d161e4110f9cc0762af03f2_tuple, 1, const_str_plain_parser ); Py_INCREF( const_str_plain_parser );
    PyTuple_SET_ITEM( const_tuple_d9f994044d161e4110f9cc0762af03f2_tuple, 2, const_str_plain_bufsize ); Py_INCREF( const_str_plain_bufsize );
    PyTuple_SET_ITEM( const_tuple_d9f994044d161e4110f9cc0762af03f2_tuple, 3, const_str_plain_forbid_dtd ); Py_INCREF( const_str_plain_forbid_dtd );
    PyTuple_SET_ITEM( const_tuple_d9f994044d161e4110f9cc0762af03f2_tuple, 4, const_str_plain_forbid_entities ); Py_INCREF( const_str_plain_forbid_entities );
    PyTuple_SET_ITEM( const_tuple_d9f994044d161e4110f9cc0762af03f2_tuple, 5, const_str_plain_forbid_external ); Py_INCREF( const_str_plain_forbid_external );
    const_str_digest_4dde434bd2c5c7a4395d42c157f28b0b = UNSTREAM_STRING( &constant_bin[ 221274 ], 18, 0 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_defusedxml$pulldom( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_48d56bcf0c17ec2b52df601d51ace1b9;
static PyCodeObject *codeobj_5cba7bc1bb6d9aa0a3f3feae1c9a58fc;
static PyCodeObject *codeobj_211a572e59643220d848b1c173563fc4;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_5093870bf554b260d37d6b0e0bfbc00e );
    codeobj_48d56bcf0c17ec2b52df601d51ace1b9 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_parse, 17, const_tuple_d9f994044d161e4110f9cc0762af03f2_tuple, 6, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_PRINT_FUNCTION );
    codeobj_5cba7bc1bb6d9aa0a3f3feae1c9a58fc = MAKE_CODEOBJ( module_filename_obj, const_str_plain_parseString, 27, const_tuple_ad156ecd6a482ca6ef2bca0bda398c70_tuple, 5, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_PRINT_FUNCTION );
    codeobj_211a572e59643220d848b1c173563fc4 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_pulldom, 1, const_tuple_empty, 0, CO_NOFREE | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_PRINT_FUNCTION );
}

// The module function declarations.
static PyObject *MAKE_FUNCTION_function_1_parse_of_defusedxml$pulldom( PyObject *defaults );


static PyObject *MAKE_FUNCTION_function_2_parseString_of_defusedxml$pulldom( PyObject *defaults );


// The module function definitions.
static PyObject *impl_function_1_parse_of_defusedxml$pulldom( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_stream_or_string = python_pars[ 0 ];
    PyObject *par_parser = python_pars[ 1 ];
    PyObject *par_bufsize = python_pars[ 2 ];
    PyObject *par_forbid_dtd = python_pars[ 3 ];
    PyObject *par_forbid_entities = python_pars[ 4 ];
    PyObject *par_forbid_external = python_pars[ 5 ];
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
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_frame_locals;
    bool tmp_is_1;
    bool tmp_result;
    PyObject *tmp_return_value;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_48d56bcf0c17ec2b52df601d51ace1b9, module_defusedxml$pulldom );
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
    tmp_compare_left_1 = par_parser;

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
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain_make_parser );

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

        exception_lineno = 20;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 20;
    tmp_assign_source_1 = CALL_FUNCTION_NO_ARGS( tmp_called_name_1 );
    if ( tmp_assign_source_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 20;
        goto frame_exception_exit_1;
    }
    {
        PyObject *old = par_parser;
        assert( old != NULL );
        par_parser = tmp_assign_source_1;
        Py_DECREF( old );
    }

    tmp_assattr_name_1 = par_forbid_dtd;

    tmp_assattr_target_1 = par_parser;

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_1, const_str_plain_forbid_dtd, tmp_assattr_name_1 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 21;
        goto frame_exception_exit_1;
    }
    tmp_assattr_name_2 = par_forbid_entities;

    tmp_assattr_target_2 = par_parser;

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_2, const_str_plain_forbid_entities, tmp_assattr_name_2 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 22;
        goto frame_exception_exit_1;
    }
    tmp_assattr_name_3 = par_forbid_external;

    tmp_assattr_target_3 = par_parser;

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_3, const_str_plain_forbid_external, tmp_assattr_name_3 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 23;
        goto frame_exception_exit_1;
    }
    branch_no_1:;
    tmp_called_name_2 = GET_STRING_DICT_VALUE( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain__parse );

    if (unlikely( tmp_called_name_2 == NULL ))
    {
        tmp_called_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__parse );
    }

    if ( tmp_called_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "_parse" );
        exception_tb = NULL;

        exception_lineno = 24;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = par_stream_or_string;

    tmp_args_element_name_2 = par_parser;

    tmp_args_element_name_3 = par_bufsize;

    frame_function->f_lineno = 24;
    {
        PyObject *call_args[] = { tmp_args_element_name_1, tmp_args_element_name_2, tmp_args_element_name_3 };
        tmp_return_value = CALL_FUNCTION_WITH_ARGS3( tmp_called_name_2, call_args );
    }

    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 24;
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
            if ( par_stream_or_string )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_stream_or_string,
                    par_stream_or_string
                );

                assert( res == 0 );
            }

            if ( par_parser )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_parser,
                    par_parser
                );

                assert( res == 0 );
            }

            if ( par_bufsize )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_bufsize,
                    par_bufsize
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
    NUITKA_CANNOT_GET_HERE( function_1_parse_of_defusedxml$pulldom );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_stream_or_string );
    Py_DECREF( par_stream_or_string );
    par_stream_or_string = NULL;

    CHECK_OBJECT( (PyObject *)par_parser );
    Py_DECREF( par_parser );
    par_parser = NULL;

    CHECK_OBJECT( (PyObject *)par_bufsize );
    Py_DECREF( par_bufsize );
    par_bufsize = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_dtd );
    Py_DECREF( par_forbid_dtd );
    par_forbid_dtd = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_entities );
    Py_DECREF( par_forbid_entities );
    par_forbid_entities = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_external );
    Py_DECREF( par_forbid_external );
    par_forbid_external = NULL;

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

    CHECK_OBJECT( (PyObject *)par_stream_or_string );
    Py_DECREF( par_stream_or_string );
    par_stream_or_string = NULL;

    Py_XDECREF( par_parser );
    par_parser = NULL;

    CHECK_OBJECT( (PyObject *)par_bufsize );
    Py_DECREF( par_bufsize );
    par_bufsize = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_dtd );
    Py_DECREF( par_forbid_dtd );
    par_forbid_dtd = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_entities );
    Py_DECREF( par_forbid_entities );
    par_forbid_entities = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_external );
    Py_DECREF( par_forbid_external );
    par_forbid_external = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_1_parse_of_defusedxml$pulldom );
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


static PyObject *impl_function_2_parseString_of_defusedxml$pulldom( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_string = python_pars[ 0 ];
    PyObject *par_parser = python_pars[ 1 ];
    PyObject *par_forbid_dtd = python_pars[ 2 ];
    PyObject *par_forbid_entities = python_pars[ 3 ];
    PyObject *par_forbid_external = python_pars[ 4 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_assattr_name_1;
    PyObject *tmp_assattr_name_2;
    PyObject *tmp_assattr_name_3;
    PyObject *tmp_assattr_target_1;
    PyObject *tmp_assattr_target_2;
    PyObject *tmp_assattr_target_3;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_frame_locals;
    bool tmp_is_1;
    bool tmp_result;
    PyObject *tmp_return_value;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_5cba7bc1bb6d9aa0a3f3feae1c9a58fc, module_defusedxml$pulldom );
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
    tmp_compare_left_1 = par_parser;

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
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain_make_parser );

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

        exception_lineno = 30;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 30;
    tmp_assign_source_1 = CALL_FUNCTION_NO_ARGS( tmp_called_name_1 );
    if ( tmp_assign_source_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    {
        PyObject *old = par_parser;
        assert( old != NULL );
        par_parser = tmp_assign_source_1;
        Py_DECREF( old );
    }

    tmp_assattr_name_1 = par_forbid_dtd;

    tmp_assattr_target_1 = par_parser;

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_1, const_str_plain_forbid_dtd, tmp_assattr_name_1 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 31;
        goto frame_exception_exit_1;
    }
    tmp_assattr_name_2 = par_forbid_entities;

    tmp_assattr_target_2 = par_parser;

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_2, const_str_plain_forbid_entities, tmp_assattr_name_2 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 32;
        goto frame_exception_exit_1;
    }
    tmp_assattr_name_3 = par_forbid_external;

    tmp_assattr_target_3 = par_parser;

    tmp_result = SET_ATTRIBUTE( tmp_assattr_target_3, const_str_plain_forbid_external, tmp_assattr_name_3 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 33;
        goto frame_exception_exit_1;
    }
    branch_no_1:;
    tmp_called_name_2 = GET_STRING_DICT_VALUE( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain__parseString );

    if (unlikely( tmp_called_name_2 == NULL ))
    {
        tmp_called_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__parseString );
    }

    if ( tmp_called_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "_parseString" );
        exception_tb = NULL;

        exception_lineno = 34;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = par_string;

    tmp_args_element_name_2 = par_parser;

    frame_function->f_lineno = 34;
    {
        PyObject *call_args[] = { tmp_args_element_name_1, tmp_args_element_name_2 };
        tmp_return_value = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_2, call_args );
    }

    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
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
            if ( par_string )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_string,
                    par_string
                );

                assert( res == 0 );
            }

            if ( par_parser )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_parser,
                    par_parser
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
    NUITKA_CANNOT_GET_HERE( function_2_parseString_of_defusedxml$pulldom );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_string );
    Py_DECREF( par_string );
    par_string = NULL;

    CHECK_OBJECT( (PyObject *)par_parser );
    Py_DECREF( par_parser );
    par_parser = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_dtd );
    Py_DECREF( par_forbid_dtd );
    par_forbid_dtd = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_entities );
    Py_DECREF( par_forbid_entities );
    par_forbid_entities = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_external );
    Py_DECREF( par_forbid_external );
    par_forbid_external = NULL;

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

    Py_XDECREF( par_parser );
    par_parser = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_dtd );
    Py_DECREF( par_forbid_dtd );
    par_forbid_dtd = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_entities );
    Py_DECREF( par_forbid_entities );
    par_forbid_entities = NULL;

    CHECK_OBJECT( (PyObject *)par_forbid_external );
    Py_DECREF( par_forbid_external );
    par_forbid_external = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_2_parseString_of_defusedxml$pulldom );
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



static PyObject *MAKE_FUNCTION_function_1_parse_of_defusedxml$pulldom( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_1_parse_of_defusedxml$pulldom,
        const_str_plain_parse,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_48d56bcf0c17ec2b52df601d51ace1b9,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_defusedxml$pulldom,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_2_parseString_of_defusedxml$pulldom( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_2_parseString_of_defusedxml$pulldom,
        const_str_plain_parseString,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_5cba7bc1bb6d9aa0a3f3feae1c9a58fc,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_defusedxml$pulldom,
        Py_None
    );

    return result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_defusedxml$pulldom =
{
    PyModuleDef_HEAD_INIT,
    "defusedxml.pulldom",   /* m_name */
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

MOD_INIT_DECL( defusedxml$pulldom )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_defusedxml$pulldom );
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

    // puts( "in initdefusedxml$pulldom" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_defusedxml$pulldom = Py_InitModule4(
        "defusedxml.pulldom",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_defusedxml$pulldom = PyModule_Create( &mdef_defusedxml$pulldom );
#endif

    moduledict_defusedxml$pulldom = (PyDictObject *)((PyModuleObject *)module_defusedxml$pulldom)->md_dict;

    CHECK_OBJECT( module_defusedxml$pulldom );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_digest_4dde434bd2c5c7a4395d42c157f28b0b, module_defusedxml$pulldom );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_defusedxml$pulldom );

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
    PyObject *tmp_defaults_1;
    PyObject *tmp_defaults_2;
    PyObject *tmp_import_globals_1;
    PyObject *tmp_import_globals_2;
    PyObject *tmp_import_globals_3;
    PyObject *tmp_import_name_from_1;
    PyObject *tmp_import_name_from_2;
    PyObject *tmp_import_name_from_3;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = const_str_digest_608c0e8034f5755cebb7f326fbc6c185;
    UPDATE_STRING_DICT0( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_assign_source_3 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "print_function");
    UPDATE_STRING_DICT0( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain_print_function, tmp_assign_source_3 );
    tmp_assign_source_4 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "absolute_import");
    UPDATE_STRING_DICT0( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain_absolute_import, tmp_assign_source_4 );
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_211a572e59643220d848b1c173563fc4, module_defusedxml$pulldom );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    tmp_import_globals_1 = ((PyModuleObject *)module_defusedxml$pulldom)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_1 = IMPORT_MODULE( const_str_digest_ca8102e928c8c9d3d46859f5f9518ed8, tmp_import_globals_1, tmp_import_globals_1, const_tuple_str_plain_parse_tuple, const_int_0 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_5 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_parse );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain__parse, tmp_assign_source_5 );
    tmp_import_globals_2 = ((PyModuleObject *)module_defusedxml$pulldom)->md_dict;
    frame_module->f_lineno = 11;
    tmp_import_name_from_2 = IMPORT_MODULE( const_str_digest_ca8102e928c8c9d3d46859f5f9518ed8, tmp_import_globals_2, tmp_import_globals_2, const_tuple_str_plain_parseString_tuple, const_int_0 );
    if ( tmp_import_name_from_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 11;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_6 = IMPORT_NAME( tmp_import_name_from_2, const_str_plain_parseString );
    Py_DECREF( tmp_import_name_from_2 );
    if ( tmp_assign_source_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 11;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain__parseString, tmp_assign_source_6 );
    tmp_import_globals_3 = ((PyModuleObject *)module_defusedxml$pulldom)->md_dict;
    frame_module->f_lineno = 12;
    tmp_import_name_from_3 = IMPORT_MODULE( const_str_plain_sax, tmp_import_globals_3, tmp_import_globals_3, const_tuple_str_plain_make_parser_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 12;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_7 = IMPORT_NAME( tmp_import_name_from_3, const_str_plain_make_parser );
    Py_DECREF( tmp_import_name_from_3 );
    if ( tmp_assign_source_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 12;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain_make_parser, tmp_assign_source_7 );

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
    tmp_assign_source_8 = const_str_digest_ca8102e928c8c9d3d46859f5f9518ed8;
    UPDATE_STRING_DICT0( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain___origin__, tmp_assign_source_8 );
    tmp_defaults_1 = const_tuple_none_none_false_true_true_tuple;
    tmp_assign_source_9 = MAKE_FUNCTION_function_1_parse_of_defusedxml$pulldom( INCREASE_REFCOUNT( tmp_defaults_1 ) );
    UPDATE_STRING_DICT1( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain_parse, tmp_assign_source_9 );
    tmp_defaults_2 = const_tuple_none_false_true_true_tuple;
    tmp_assign_source_10 = MAKE_FUNCTION_function_2_parseString_of_defusedxml$pulldom( INCREASE_REFCOUNT( tmp_defaults_2 ) );
    UPDATE_STRING_DICT1( moduledict_defusedxml$pulldom, (Nuitka_StringObject *)const_str_plain_parseString, tmp_assign_source_10 );

    return MOD_RETURN_VALUE( module_defusedxml$pulldom );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
