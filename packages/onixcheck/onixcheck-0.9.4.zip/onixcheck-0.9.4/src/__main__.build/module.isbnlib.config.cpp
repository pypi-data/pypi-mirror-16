/* Generated code for Python source for module 'isbnlib.config'
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

/* The _module_isbnlib$config is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_isbnlib$config;
PyDictObject *moduledict_isbnlib$config;

/* The module constants used, if any. */
extern PyObject *const_str_plain_value;
extern PyObject *const_str_plain_SOCKETS_TIMEOUT;
extern PyObject *const_str_plain_serial;
extern PyObject *const_int_neg_1;
extern PyObject *const_str_plain_apikey;
static PyObject *const_str_plain_setdefaulttimeout;
static PyObject *const_str_plain_set_option;
extern PyObject *const_dict_empty;
static PyObject *const_tuple_str_plain_service_str_plain_apikey_tuple;
static PyObject *const_str_plain_add_apikey;
extern PyObject *const_str_plain_THREADS_TIMEOUT;
extern PyObject *const_int_pos_11;
extern PyObject *const_int_pos_12;
static PyObject *const_tuple_str_plain_seconds_tuple;
extern PyObject *const_tuple_empty;
extern PyObject *const_str_plain_config;
static PyObject *const_str_digest_1167046ab7085d09e291eada067a5b5b;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_options;
extern PyObject *const_str_plain_service;
static PyObject *const_str_digest_ea14b0cea78c9e39492ba3ee9f4192fd;
extern PyObject *const_str_plain___file__;
static PyObject *const_tuple_str_plain_option_str_plain_value_tuple;
extern PyObject *const_str_plain_option;
static PyObject *const_dict_e81b60d1971243a5d60e42de048f63ad;
static PyObject *const_str_digest_ed379592c0ee16903df0280cb2b478c6;
static PyObject *const_str_digest_855a3d82209716a249681ffa9d987b19;
extern PyObject *const_str_plain_apikeys;
static PyObject *const_str_plain_setsocketstimeout;
extern PyObject *const_str_plain_seconds;
static PyObject *const_str_digest_e7672a03781410df4f2650300962745c;
static PyObject *const_str_digest_c7504a2743a0dcdf1ca969dfd28806e7;
extern PyObject *const_str_plain_VIAS_MERGE;
static PyObject *const_str_plain_setthreadstimeout;
static PyObject *const_str_digest_be080082a3164e2ae98890789303f635;
extern PyObject *const_str_plain_socket;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_plain_setdefaulttimeout = UNSTREAM_STRING( &constant_bin[ 527745 ], 17, 1 );
    const_str_plain_set_option = UNSTREAM_STRING( &constant_bin[ 527762 ], 10, 1 );
    const_tuple_str_plain_service_str_plain_apikey_tuple = PyTuple_New( 2 );
    PyTuple_SET_ITEM( const_tuple_str_plain_service_str_plain_apikey_tuple, 0, const_str_plain_service ); Py_INCREF( const_str_plain_service );
    PyTuple_SET_ITEM( const_tuple_str_plain_service_str_plain_apikey_tuple, 1, const_str_plain_apikey ); Py_INCREF( const_str_plain_apikey );
    const_str_plain_add_apikey = UNSTREAM_STRING( &constant_bin[ 527772 ], 10, 1 );
    const_tuple_str_plain_seconds_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_seconds_tuple, 0, const_str_plain_seconds ); Py_INCREF( const_str_plain_seconds );
    const_str_digest_1167046ab7085d09e291eada067a5b5b = UNSTREAM_STRING( &constant_bin[ 527782 ], 25, 0 );
    const_str_digest_ea14b0cea78c9e39492ba3ee9f4192fd = UNSTREAM_STRING( &constant_bin[ 527807 ], 46, 0 );
    const_tuple_str_plain_option_str_plain_value_tuple = PyTuple_New( 2 );
    PyTuple_SET_ITEM( const_tuple_str_plain_option_str_plain_value_tuple, 0, const_str_plain_option ); Py_INCREF( const_str_plain_option );
    PyTuple_SET_ITEM( const_tuple_str_plain_option_str_plain_value_tuple, 1, const_str_plain_value ); Py_INCREF( const_str_plain_value );
    const_dict_e81b60d1971243a5d60e42de048f63ad = _PyDict_NewPresized( 1 );
    PyDict_SetItem( const_dict_e81b60d1971243a5d60e42de048f63ad, const_str_plain_VIAS_MERGE, const_str_plain_serial );
    assert( PyDict_Size( const_dict_e81b60d1971243a5d60e42de048f63ad ) == 1 );
    const_str_digest_ed379592c0ee16903df0280cb2b478c6 = UNSTREAM_STRING( &constant_bin[ 527853 ], 66, 0 );
    const_str_digest_855a3d82209716a249681ffa9d987b19 = UNSTREAM_STRING( &constant_bin[ 527919 ], 24, 0 );
    const_str_plain_setsocketstimeout = UNSTREAM_STRING( &constant_bin[ 527943 ], 17, 1 );
    const_str_digest_e7672a03781410df4f2650300962745c = UNSTREAM_STRING( &constant_bin[ 527960 ], 14, 0 );
    const_str_digest_c7504a2743a0dcdf1ca969dfd28806e7 = UNSTREAM_STRING( &constant_bin[ 527974 ], 17, 0 );
    const_str_plain_setthreadstimeout = UNSTREAM_STRING( &constant_bin[ 527991 ], 17, 1 );
    const_str_digest_be080082a3164e2ae98890789303f635 = UNSTREAM_STRING( &constant_bin[ 528008 ], 46, 0 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_isbnlib$config( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_1388c1bb021198e5b02bbcf96cf5c368;
static PyCodeObject *codeobj_fb23a436b4abaebc42c3b077ac950c04;
static PyCodeObject *codeobj_713eb1b35d97cd1d1ad3761302b9d04e;
static PyCodeObject *codeobj_794e37299fc4bc5ff7c51a5440c1feeb;
static PyCodeObject *codeobj_ba1a236438689432de5ca29b85c25c65;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_c7504a2743a0dcdf1ca969dfd28806e7 );
    codeobj_1388c1bb021198e5b02bbcf96cf5c368 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_add_apikey, 35, const_tuple_str_plain_service_str_plain_apikey_tuple, 2, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_fb23a436b4abaebc42c3b077ac950c04 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_config, 1, const_tuple_empty, 0, CO_NOFREE );
    codeobj_713eb1b35d97cd1d1ad3761302b9d04e = MAKE_CODEOBJ( module_filename_obj, const_str_plain_set_option, 46, const_tuple_str_plain_option_str_plain_value_tuple, 2, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_794e37299fc4bc5ff7c51a5440c1feeb = MAKE_CODEOBJ( module_filename_obj, const_str_plain_setsocketstimeout, 14, const_tuple_str_plain_seconds_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_ba1a236438689432de5ca29b85c25c65 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_setthreadstimeout, 26, const_tuple_str_plain_seconds_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
}

// The module function declarations.
static PyObject *MAKE_FUNCTION_function_1_setsocketstimeout_of_isbnlib$config(  );


static PyObject *MAKE_FUNCTION_function_2_setthreadstimeout_of_isbnlib$config(  );


static PyObject *MAKE_FUNCTION_function_3_add_apikey_of_isbnlib$config(  );


static PyObject *MAKE_FUNCTION_function_4_set_option_of_isbnlib$config(  );


// The module function definitions.
static PyObject *impl_function_1_setsocketstimeout_of_isbnlib$config( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_seconds = python_pars[ 0 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    PyObject *tmp_source_name_1;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    tmp_assign_source_1 = par_seconds;

    UPDATE_STRING_DICT0( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_SOCKETS_TIMEOUT, tmp_assign_source_1 );
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_794e37299fc4bc5ff7c51a5440c1feeb, module_isbnlib$config );
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
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_socket );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_socket );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "socket" );
        exception_tb = NULL;

        exception_lineno = 19;
        goto frame_exception_exit_1;
    }

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_setdefaulttimeout );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 19;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_1 = GET_STRING_DICT_VALUE( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_SOCKETS_TIMEOUT );

    if (unlikely( tmp_args_element_name_1 == NULL ))
    {
        tmp_args_element_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_SOCKETS_TIMEOUT );
    }

    if ( tmp_args_element_name_1 == NULL )
    {
        Py_DECREF( tmp_called_name_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "SOCKETS_TIMEOUT" );
        exception_tb = NULL;

        exception_lineno = 19;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 19;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_return_value = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 19;
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
            if ( par_seconds )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_seconds,
                    par_seconds
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
    NUITKA_CANNOT_GET_HERE( function_1_setsocketstimeout_of_isbnlib$config );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_seconds );
    Py_DECREF( par_seconds );
    par_seconds = NULL;

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

    CHECK_OBJECT( (PyObject *)par_seconds );
    Py_DECREF( par_seconds );
    par_seconds = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_1_setsocketstimeout_of_isbnlib$config );
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


static PyObject *impl_function_2_setthreadstimeout_of_isbnlib$config( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_seconds = python_pars[ 0 ];
    PyObject *tmp_assign_source_1;
    PyObject *tmp_return_value;
    tmp_return_value = NULL;

    // Actual function code.
    tmp_assign_source_1 = par_seconds;

    UPDATE_STRING_DICT0( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_THREADS_TIMEOUT, tmp_assign_source_1 );
    // Tried code:
    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_2_setthreadstimeout_of_isbnlib$config );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_seconds );
    Py_DECREF( par_seconds );
    par_seconds = NULL;

    goto function_return_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_2_setthreadstimeout_of_isbnlib$config );
    return NULL;

    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}


static PyObject *impl_function_3_add_apikey_of_isbnlib$config( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_service = python_pars[ 0 ];
    PyObject *par_apikey = python_pars[ 1 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_ass_subscribed_1;
    PyObject *tmp_ass_subscript_1;
    PyObject *tmp_ass_subvalue_1;
    PyObject *tmp_frame_locals;
    bool tmp_result;
    PyObject *tmp_return_value;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_1388c1bb021198e5b02bbcf96cf5c368, module_isbnlib$config );
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
    tmp_ass_subvalue_1 = par_apikey;

    tmp_ass_subscribed_1 = GET_STRING_DICT_VALUE( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_apikeys );

    if (unlikely( tmp_ass_subscribed_1 == NULL ))
    {
        tmp_ass_subscribed_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_apikeys );
    }

    if ( tmp_ass_subscribed_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "apikeys" );
        exception_tb = NULL;

        exception_lineno = 40;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscript_1 = par_service;

    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_1, tmp_ass_subscript_1, tmp_ass_subvalue_1 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 40;
        goto frame_exception_exit_1;
    }

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
            if ( par_service )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_service,
                    par_service
                );

                assert( res == 0 );
            }

            if ( par_apikey )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_apikey,
                    par_apikey
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
    NUITKA_CANNOT_GET_HERE( function_3_add_apikey_of_isbnlib$config );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_service );
    Py_DECREF( par_service );
    par_service = NULL;

    CHECK_OBJECT( (PyObject *)par_apikey );
    Py_DECREF( par_apikey );
    par_apikey = NULL;

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

    CHECK_OBJECT( (PyObject *)par_service );
    Py_DECREF( par_service );
    par_service = NULL;

    CHECK_OBJECT( (PyObject *)par_apikey );
    Py_DECREF( par_apikey );
    par_apikey = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_3_add_apikey_of_isbnlib$config );
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


static PyObject *impl_function_4_set_option_of_isbnlib$config( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_option = python_pars[ 0 ];
    PyObject *par_value = python_pars[ 1 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_ass_subscribed_1;
    PyObject *tmp_ass_subscript_1;
    PyObject *tmp_ass_subvalue_1;
    PyObject *tmp_frame_locals;
    bool tmp_result;
    PyObject *tmp_return_value;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_713eb1b35d97cd1d1ad3761302b9d04e, module_isbnlib$config );
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
    tmp_ass_subvalue_1 = par_value;

    tmp_ass_subscribed_1 = GET_STRING_DICT_VALUE( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_options );

    if (unlikely( tmp_ass_subscribed_1 == NULL ))
    {
        tmp_ass_subscribed_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_options );
    }

    if ( tmp_ass_subscribed_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "options" );
        exception_tb = NULL;

        exception_lineno = 48;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscript_1 = par_option;

    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_1, tmp_ass_subscript_1, tmp_ass_subvalue_1 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 48;
        goto frame_exception_exit_1;
    }

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
            if ( par_option )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_option,
                    par_option
                );

                assert( res == 0 );
            }

            if ( par_value )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_value,
                    par_value
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
    NUITKA_CANNOT_GET_HERE( function_4_set_option_of_isbnlib$config );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_option );
    Py_DECREF( par_option );
    par_option = NULL;

    CHECK_OBJECT( (PyObject *)par_value );
    Py_DECREF( par_value );
    par_value = NULL;

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

    CHECK_OBJECT( (PyObject *)par_option );
    Py_DECREF( par_option );
    par_option = NULL;

    CHECK_OBJECT( (PyObject *)par_value );
    Py_DECREF( par_value );
    par_value = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_4_set_option_of_isbnlib$config );
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



static PyObject *MAKE_FUNCTION_function_1_setsocketstimeout_of_isbnlib$config(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_1_setsocketstimeout_of_isbnlib$config,
        const_str_plain_setsocketstimeout,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_794e37299fc4bc5ff7c51a5440c1feeb,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_isbnlib$config,
        const_str_digest_be080082a3164e2ae98890789303f635
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_2_setthreadstimeout_of_isbnlib$config(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_2_setthreadstimeout_of_isbnlib$config,
        const_str_plain_setthreadstimeout,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_ba1a236438689432de5ca29b85c25c65,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_isbnlib$config,
        const_str_digest_ea14b0cea78c9e39492ba3ee9f4192fd
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_3_add_apikey_of_isbnlib$config(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_3_add_apikey_of_isbnlib$config,
        const_str_plain_add_apikey,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_1388c1bb021198e5b02bbcf96cf5c368,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_isbnlib$config,
        const_str_digest_ed379592c0ee16903df0280cb2b478c6
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_4_set_option_of_isbnlib$config(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_4_set_option_of_isbnlib$config,
        const_str_plain_set_option,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_713eb1b35d97cd1d1ad3761302b9d04e,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_isbnlib$config,
        const_str_digest_1167046ab7085d09e291eada067a5b5b
    );

    return result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_isbnlib$config =
{
    PyModuleDef_HEAD_INIT,
    "isbnlib.config",   /* m_name */
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

MOD_INIT_DECL( isbnlib$config )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_isbnlib$config );
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

    // puts( "in initisbnlib$config" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_isbnlib$config = Py_InitModule4(
        "isbnlib.config",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_isbnlib$config = PyModule_Create( &mdef_isbnlib$config );
#endif

    moduledict_isbnlib$config = (PyDictObject *)((PyModuleObject *)module_isbnlib$config)->md_dict;

    CHECK_OBJECT( module_isbnlib$config );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_digest_e7672a03781410df4f2650300962745c, module_isbnlib$config );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_isbnlib$config );

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
    PyObject *tmp_called_name_1;
    PyObject *tmp_import_globals_1;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = const_str_digest_855a3d82209716a249681ffa9d987b19;
    UPDATE_STRING_DICT0( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_fb23a436b4abaebc42c3b077ac950c04, module_isbnlib$config );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    tmp_import_globals_1 = ((PyModuleObject *)module_isbnlib$config)->md_dict;
    frame_module->f_lineno = 7;
    tmp_assign_source_3 = IMPORT_MODULE( const_str_plain_socket, tmp_import_globals_1, tmp_import_globals_1, Py_None, const_int_neg_1 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 7;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_socket, tmp_assign_source_3 );
    tmp_assign_source_4 = const_int_pos_12;
    UPDATE_STRING_DICT0( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_SOCKETS_TIMEOUT, tmp_assign_source_4 );
    tmp_assign_source_5 = const_int_pos_11;
    UPDATE_STRING_DICT0( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_THREADS_TIMEOUT, tmp_assign_source_5 );
    tmp_assign_source_6 = MAKE_FUNCTION_function_1_setsocketstimeout_of_isbnlib$config(  );
    UPDATE_STRING_DICT1( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_setsocketstimeout, tmp_assign_source_6 );
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_setsocketstimeout );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_setsocketstimeout );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "setsocketstimeout" );
        exception_tb = NULL;

        exception_lineno = 22;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = GET_STRING_DICT_VALUE( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_SOCKETS_TIMEOUT );

    if (unlikely( tmp_args_element_name_1 == NULL ))
    {
        tmp_args_element_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_SOCKETS_TIMEOUT );
    }

    if ( tmp_args_element_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "SOCKETS_TIMEOUT" );
        exception_tb = NULL;

        exception_lineno = 22;
        goto frame_exception_exit_1;
    }

    frame_module->f_lineno = 22;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 22;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );

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
    tmp_assign_source_7 = MAKE_FUNCTION_function_2_setthreadstimeout_of_isbnlib$config(  );
    UPDATE_STRING_DICT1( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_setthreadstimeout, tmp_assign_source_7 );
    tmp_assign_source_8 = PyDict_New();
    UPDATE_STRING_DICT1( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_apikeys, tmp_assign_source_8 );
    tmp_assign_source_9 = MAKE_FUNCTION_function_3_add_apikey_of_isbnlib$config(  );
    UPDATE_STRING_DICT1( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_add_apikey, tmp_assign_source_9 );
    tmp_assign_source_10 = PyDict_Copy( const_dict_e81b60d1971243a5d60e42de048f63ad );
    UPDATE_STRING_DICT1( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_options, tmp_assign_source_10 );
    tmp_assign_source_11 = MAKE_FUNCTION_function_4_set_option_of_isbnlib$config(  );
    UPDATE_STRING_DICT1( moduledict_isbnlib$config, (Nuitka_StringObject *)const_str_plain_set_option, tmp_assign_source_11 );

    return MOD_RETURN_VALUE( module_isbnlib$config );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
