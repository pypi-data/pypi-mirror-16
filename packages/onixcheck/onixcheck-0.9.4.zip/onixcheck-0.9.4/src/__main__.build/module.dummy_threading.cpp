/* Generated code for Python source for module 'dummy_threading'
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

/* The _module_dummy_threading is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_dummy_threading;
PyDictObject *moduledict_dummy_threading;

/* The module constants used, if any. */
static PyObject *const_str_digest_1dd7f7ca87eff28332ce2a2c8c8d2f55;
extern PyObject *const_tuple_str_plain___all___tuple;
static PyObject *const_str_plain_held__threading_local;
static PyObject *const_str_plain_holding_threading;
extern PyObject *const_str_chr_42;
static PyObject *const_str_plain__dummy_threading;
extern PyObject *const_int_neg_1;
extern PyObject *const_tuple_str_chr_42_tuple;
static PyObject *const_str_plain_holding_thread;
static PyObject *const_str_plain_held_thread;
extern PyObject *const_tuple_empty;
extern PyObject *const_str_plain_threading;
static PyObject *const_str_plain_sys_modules;
extern PyObject *const_str_plain___doc__;
static PyObject *const_str_plain_held_threading;
extern PyObject *const_str_plain___all__;
extern PyObject *const_str_plain_dummy_threading;
static PyObject *const_str_plain_holding__threading_local;
extern PyObject *const_str_plain_dummy_thread;
extern PyObject *const_str_plain___file__;
extern PyObject *const_tuple_str_plain_modules_tuple;
extern PyObject *const_str_plain_modules;
static PyObject *const_str_plain__dummy__threading_local;
extern PyObject *const_str_plain_sys;
static PyObject *const_str_digest_579dd2e3cca5c235e8c7ab7d766066b4;
extern PyObject *const_str_plain_thread;
extern PyObject *const_str_plain__threading_local;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_digest_1dd7f7ca87eff28332ce2a2c8c8d2f55 = UNSTREAM_STRING( &constant_bin[ 304461 ], 18, 0 );
    const_str_plain_held__threading_local = UNSTREAM_STRING( &constant_bin[ 333 ], 21, 1 );
    const_str_plain_holding_threading = UNSTREAM_STRING( &constant_bin[ 294 ], 17, 1 );
    const_str_plain__dummy_threading = UNSTREAM_STRING( &constant_bin[ 304479 ], 16, 1 );
    const_str_plain_holding_thread = UNSTREAM_STRING( &constant_bin[ 294 ], 14, 1 );
    const_str_plain_held_thread = UNSTREAM_STRING( &constant_bin[ 258 ], 11, 1 );
    const_str_plain_sys_modules = UNSTREAM_STRING( &constant_bin[ 525 ], 11, 1 );
    const_str_plain_held_threading = UNSTREAM_STRING( &constant_bin[ 258 ], 14, 1 );
    const_str_plain_holding__threading_local = UNSTREAM_STRING( &constant_bin[ 376 ], 24, 1 );
    const_str_plain__dummy__threading_local = UNSTREAM_STRING( &constant_bin[ 304495 ], 23, 1 );
    const_str_digest_579dd2e3cca5c235e8c7ab7d766066b4 = UNSTREAM_STRING( &constant_bin[ 304518 ], 352, 0 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_dummy_threading( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_75e35e85b22d4979bac1c9a252d2a1a1;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_1dd7f7ca87eff28332ce2a2c8c8d2f55 );
    codeobj_75e35e85b22d4979bac1c9a252d2a1a1 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_dummy_threading, 1, const_tuple_empty, 0, CO_NOFREE );
}

// The module function declarations.


// The module function definitions.



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_dummy_threading =
{
    PyModuleDef_HEAD_INIT,
    "dummy_threading",   /* m_name */
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

MOD_INIT_DECL( dummy_threading )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_dummy_threading );
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

    // puts( "in initdummy_threading" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_dummy_threading = Py_InitModule4(
        "dummy_threading",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_dummy_threading = PyModule_Create( &mdef_dummy_threading );
#endif

    moduledict_dummy_threading = (PyDictObject *)((PyModuleObject *)module_dummy_threading)->md_dict;

    CHECK_OBJECT( module_dummy_threading );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_plain_dummy_threading, module_dummy_threading );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_dummy_threading );

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
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_ass_subscribed_1;
    PyObject *tmp_ass_subscribed_2;
    PyObject *tmp_ass_subscribed_3;
    PyObject *tmp_ass_subscribed_4;
    PyObject *tmp_ass_subscribed_5;
    PyObject *tmp_ass_subscribed_6;
    PyObject *tmp_ass_subscribed_7;
    PyObject *tmp_ass_subscribed_8;
    PyObject *tmp_ass_subscribed_9;
    PyObject *tmp_ass_subscript_1;
    PyObject *tmp_ass_subscript_2;
    PyObject *tmp_ass_subscript_3;
    PyObject *tmp_ass_subscript_4;
    PyObject *tmp_ass_subscript_5;
    PyObject *tmp_ass_subscript_6;
    PyObject *tmp_ass_subscript_7;
    PyObject *tmp_ass_subscript_8;
    PyObject *tmp_ass_subscript_9;
    PyObject *tmp_ass_subvalue_1;
    PyObject *tmp_ass_subvalue_2;
    PyObject *tmp_ass_subvalue_3;
    PyObject *tmp_ass_subvalue_4;
    PyObject *tmp_ass_subvalue_5;
    PyObject *tmp_ass_subvalue_6;
    PyObject *tmp_ass_subvalue_7;
    PyObject *tmp_ass_subvalue_8;
    PyObject *tmp_ass_subvalue_9;
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
    PyObject *tmp_assign_source_14;
    PyObject *tmp_assign_source_15;
    int tmp_cmp_In_1;
    int tmp_cmp_In_2;
    int tmp_cmp_In_3;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_left_2;
    PyObject *tmp_compare_left_3;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_compare_right_2;
    PyObject *tmp_compare_right_3;
    int tmp_cond_truth_1;
    int tmp_cond_truth_2;
    int tmp_cond_truth_3;
    int tmp_cond_truth_4;
    int tmp_cond_truth_5;
    int tmp_cond_truth_6;
    PyObject *tmp_cond_value_1;
    PyObject *tmp_cond_value_2;
    PyObject *tmp_cond_value_3;
    PyObject *tmp_cond_value_4;
    PyObject *tmp_cond_value_5;
    PyObject *tmp_cond_value_6;
    PyObject *tmp_delsubscr_subscript_1;
    PyObject *tmp_delsubscr_subscript_2;
    PyObject *tmp_delsubscr_subscript_3;
    PyObject *tmp_delsubscr_subscript_4;
    PyObject *tmp_delsubscr_subscript_5;
    PyObject *tmp_delsubscr_subscript_6;
    PyObject *tmp_delsubscr_target_1;
    PyObject *tmp_delsubscr_target_2;
    PyObject *tmp_delsubscr_target_3;
    PyObject *tmp_delsubscr_target_4;
    PyObject *tmp_delsubscr_target_5;
    PyObject *tmp_delsubscr_target_6;
    PyObject *tmp_import_globals_1;
    PyObject *tmp_import_globals_2;
    PyObject *tmp_import_globals_3;
    PyObject *tmp_import_globals_4;
    PyObject *tmp_import_globals_5;
    PyObject *tmp_import_name_from_1;
    PyObject *tmp_import_name_from_2;
    int tmp_res;
    bool tmp_result;
    PyObject *tmp_star_imported_1;
    PyObject *tmp_subscribed_name_1;
    PyObject *tmp_subscribed_name_2;
    PyObject *tmp_subscribed_name_3;
    PyObject *tmp_subscribed_name_4;
    PyObject *tmp_subscribed_name_5;
    PyObject *tmp_subscribed_name_6;
    PyObject *tmp_subscript_name_1;
    PyObject *tmp_subscript_name_2;
    PyObject *tmp_subscript_name_3;
    PyObject *tmp_subscript_name_4;
    PyObject *tmp_subscript_name_5;
    PyObject *tmp_subscript_name_6;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = const_str_digest_579dd2e3cca5c235e8c7ab7d766066b4;
    UPDATE_STRING_DICT0( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_75e35e85b22d4979bac1c9a252d2a1a1, module_dummy_threading );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    tmp_import_globals_1 = ((PyModuleObject *)module_dummy_threading)->md_dict;
    frame_module->f_lineno = 9;
    tmp_import_name_from_1 = IMPORT_MODULE( const_str_plain_sys, tmp_import_globals_1, tmp_import_globals_1, const_tuple_str_plain_modules_tuple, const_int_neg_1 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 9;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_3 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_modules );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 9;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules, tmp_assign_source_3 );
    tmp_import_globals_2 = ((PyModuleObject *)module_dummy_threading)->md_dict;
    frame_module->f_lineno = 11;
    tmp_assign_source_4 = IMPORT_MODULE( const_str_plain_dummy_thread, tmp_import_globals_2, tmp_import_globals_2, Py_None, const_int_neg_1 );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 11;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_dummy_thread, tmp_assign_source_4 );
    tmp_assign_source_5 = Py_False;
    UPDATE_STRING_DICT0( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_holding_thread, tmp_assign_source_5 );
    tmp_assign_source_6 = Py_False;
    UPDATE_STRING_DICT0( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_holding_threading, tmp_assign_source_6 );
    tmp_assign_source_7 = Py_False;
    UPDATE_STRING_DICT0( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_holding__threading_local, tmp_assign_source_7 );
    // Tried code:
    tmp_compare_left_1 = const_str_plain_thread;
    tmp_compare_right_1 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_compare_right_1 == NULL ))
    {
        tmp_compare_right_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_compare_right_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 22;
        goto try_except_handler_1;
    }

    tmp_cmp_In_1 = PySequence_Contains( tmp_compare_right_1, tmp_compare_left_1 );
    assert( !(tmp_cmp_In_1 == -1) );
    if ( tmp_cmp_In_1 == 1 )
    {
        goto branch_yes_1;
    }
    else
    {
        goto branch_no_1;
    }
    branch_yes_1:;
    tmp_subscribed_name_1 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_subscribed_name_1 == NULL ))
    {
        tmp_subscribed_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_subscribed_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 23;
        goto try_except_handler_1;
    }

    tmp_subscript_name_1 = const_str_plain_thread;
    tmp_assign_source_8 = LOOKUP_SUBSCRIPT( tmp_subscribed_name_1, tmp_subscript_name_1 );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 23;
        goto try_except_handler_1;
    }
    UPDATE_STRING_DICT1( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_held_thread, tmp_assign_source_8 );
    tmp_assign_source_9 = Py_True;
    UPDATE_STRING_DICT0( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_holding_thread, tmp_assign_source_9 );
    branch_no_1:;
    tmp_subscribed_name_2 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_subscribed_name_2 == NULL ))
    {
        tmp_subscribed_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_subscribed_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 27;
        goto try_except_handler_1;
    }

    tmp_subscript_name_2 = const_str_plain_dummy_thread;
    tmp_ass_subvalue_1 = LOOKUP_SUBSCRIPT( tmp_subscribed_name_2, tmp_subscript_name_2 );
    if ( tmp_ass_subvalue_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 27;
        goto try_except_handler_1;
    }
    tmp_ass_subscribed_1 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_ass_subscribed_1 == NULL ))
    {
        tmp_ass_subscribed_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_ass_subscribed_1 == NULL )
    {
        Py_DECREF( tmp_ass_subvalue_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 27;
        goto try_except_handler_1;
    }

    tmp_ass_subscript_1 = const_str_plain_thread;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_1, tmp_ass_subscript_1, tmp_ass_subvalue_1 );
    Py_DECREF( tmp_ass_subvalue_1 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 27;
        goto try_except_handler_1;
    }
    tmp_compare_left_2 = const_str_plain_threading;
    tmp_compare_right_2 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_compare_right_2 == NULL ))
    {
        tmp_compare_right_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_compare_right_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 29;
        goto try_except_handler_1;
    }

    tmp_cmp_In_2 = PySequence_Contains( tmp_compare_right_2, tmp_compare_left_2 );
    assert( !(tmp_cmp_In_2 == -1) );
    if ( tmp_cmp_In_2 == 1 )
    {
        goto branch_yes_2;
    }
    else
    {
        goto branch_no_2;
    }
    branch_yes_2:;
    tmp_subscribed_name_3 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_subscribed_name_3 == NULL ))
    {
        tmp_subscribed_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_subscribed_name_3 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 33;
        goto try_except_handler_1;
    }

    tmp_subscript_name_3 = const_str_plain_threading;
    tmp_assign_source_10 = LOOKUP_SUBSCRIPT( tmp_subscribed_name_3, tmp_subscript_name_3 );
    if ( tmp_assign_source_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 33;
        goto try_except_handler_1;
    }
    UPDATE_STRING_DICT1( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_held_threading, tmp_assign_source_10 );
    tmp_assign_source_11 = Py_True;
    UPDATE_STRING_DICT0( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_holding_threading, tmp_assign_source_11 );
    tmp_delsubscr_target_1 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_delsubscr_target_1 == NULL ))
    {
        tmp_delsubscr_target_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_delsubscr_target_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 35;
        goto try_except_handler_1;
    }

    tmp_delsubscr_subscript_1 = const_str_plain_threading;
    tmp_result = DEL_SUBSCRIPT( tmp_delsubscr_target_1, tmp_delsubscr_subscript_1 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 35;
        goto try_except_handler_1;
    }
    branch_no_2:;
    tmp_compare_left_3 = const_str_plain__threading_local;
    tmp_compare_right_3 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_compare_right_3 == NULL ))
    {
        tmp_compare_right_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_compare_right_3 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 37;
        goto try_except_handler_1;
    }

    tmp_cmp_In_3 = PySequence_Contains( tmp_compare_right_3, tmp_compare_left_3 );
    assert( !(tmp_cmp_In_3 == -1) );
    if ( tmp_cmp_In_3 == 1 )
    {
        goto branch_yes_3;
    }
    else
    {
        goto branch_no_3;
    }
    branch_yes_3:;
    tmp_subscribed_name_4 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_subscribed_name_4 == NULL ))
    {
        tmp_subscribed_name_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_subscribed_name_4 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 41;
        goto try_except_handler_1;
    }

    tmp_subscript_name_4 = const_str_plain__threading_local;
    tmp_assign_source_12 = LOOKUP_SUBSCRIPT( tmp_subscribed_name_4, tmp_subscript_name_4 );
    if ( tmp_assign_source_12 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 41;
        goto try_except_handler_1;
    }
    UPDATE_STRING_DICT1( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_held__threading_local, tmp_assign_source_12 );
    tmp_assign_source_13 = Py_True;
    UPDATE_STRING_DICT0( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_holding__threading_local, tmp_assign_source_13 );
    tmp_delsubscr_target_2 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_delsubscr_target_2 == NULL ))
    {
        tmp_delsubscr_target_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_delsubscr_target_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 43;
        goto try_except_handler_1;
    }

    tmp_delsubscr_subscript_2 = const_str_plain__threading_local;
    tmp_result = DEL_SUBSCRIPT( tmp_delsubscr_target_2, tmp_delsubscr_subscript_2 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 43;
        goto try_except_handler_1;
    }
    branch_no_3:;
    tmp_import_globals_3 = ((PyModuleObject *)module_dummy_threading)->md_dict;
    frame_module->f_lineno = 45;
    tmp_assign_source_14 = IMPORT_MODULE( const_str_plain_threading, tmp_import_globals_3, tmp_import_globals_3, Py_None, const_int_neg_1 );
    if ( tmp_assign_source_14 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 45;
        goto try_except_handler_1;
    }
    UPDATE_STRING_DICT1( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_threading, tmp_assign_source_14 );
    tmp_subscribed_name_5 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_subscribed_name_5 == NULL ))
    {
        tmp_subscribed_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_subscribed_name_5 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 47;
        goto try_except_handler_1;
    }

    tmp_subscript_name_5 = const_str_plain_threading;
    tmp_ass_subvalue_2 = LOOKUP_SUBSCRIPT( tmp_subscribed_name_5, tmp_subscript_name_5 );
    if ( tmp_ass_subvalue_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 47;
        goto try_except_handler_1;
    }
    tmp_ass_subscribed_2 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_ass_subscribed_2 == NULL ))
    {
        tmp_ass_subscribed_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_ass_subscribed_2 == NULL )
    {
        Py_DECREF( tmp_ass_subvalue_2 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 47;
        goto try_except_handler_1;
    }

    tmp_ass_subscript_2 = const_str_plain__dummy_threading;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_2, tmp_ass_subscript_2, tmp_ass_subvalue_2 );
    Py_DECREF( tmp_ass_subvalue_2 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 47;
        goto try_except_handler_1;
    }
    tmp_delsubscr_target_3 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_delsubscr_target_3 == NULL ))
    {
        tmp_delsubscr_target_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_delsubscr_target_3 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 48;
        goto try_except_handler_1;
    }

    tmp_delsubscr_subscript_3 = const_str_plain_threading;
    tmp_result = DEL_SUBSCRIPT( tmp_delsubscr_target_3, tmp_delsubscr_subscript_3 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 48;
        goto try_except_handler_1;
    }
    tmp_subscribed_name_6 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_subscribed_name_6 == NULL ))
    {
        tmp_subscribed_name_6 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_subscribed_name_6 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 49;
        goto try_except_handler_1;
    }

    tmp_subscript_name_6 = const_str_plain__threading_local;
    tmp_ass_subvalue_3 = LOOKUP_SUBSCRIPT( tmp_subscribed_name_6, tmp_subscript_name_6 );
    if ( tmp_ass_subvalue_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 49;
        goto try_except_handler_1;
    }
    tmp_ass_subscribed_3 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_ass_subscribed_3 == NULL ))
    {
        tmp_ass_subscribed_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_ass_subscribed_3 == NULL )
    {
        Py_DECREF( tmp_ass_subvalue_3 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 49;
        goto try_except_handler_1;
    }

    tmp_ass_subscript_3 = const_str_plain__dummy__threading_local;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_3, tmp_ass_subscript_3, tmp_ass_subvalue_3 );
    Py_DECREF( tmp_ass_subvalue_3 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 49;
        goto try_except_handler_1;
    }
    tmp_delsubscr_target_4 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_delsubscr_target_4 == NULL ))
    {
        tmp_delsubscr_target_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_delsubscr_target_4 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 50;
        goto try_except_handler_1;
    }

    tmp_delsubscr_subscript_4 = const_str_plain__threading_local;
    tmp_result = DEL_SUBSCRIPT( tmp_delsubscr_target_4, tmp_delsubscr_subscript_4 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 50;
        goto try_except_handler_1;
    }
    tmp_import_globals_4 = ((PyModuleObject *)module_dummy_threading)->md_dict;
    frame_module->f_lineno = 51;
    tmp_star_imported_1 = IMPORT_MODULE( const_str_plain__dummy_threading, tmp_import_globals_4, tmp_import_globals_4, const_tuple_str_chr_42_tuple, const_int_neg_1 );
    if ( tmp_star_imported_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 51;
        goto try_except_handler_1;
    }
    tmp_result = IMPORT_MODULE_STAR( module_dummy_threading, true, tmp_star_imported_1 );
    Py_DECREF( tmp_star_imported_1 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 51;
        goto try_except_handler_1;
    }
    tmp_import_globals_5 = ((PyModuleObject *)module_dummy_threading)->md_dict;
    frame_module->f_lineno = 52;
    tmp_import_name_from_2 = IMPORT_MODULE( const_str_plain__dummy_threading, tmp_import_globals_5, tmp_import_globals_5, const_tuple_str_plain___all___tuple, const_int_neg_1 );
    if ( tmp_import_name_from_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 52;
        goto try_except_handler_1;
    }
    tmp_assign_source_15 = IMPORT_NAME( tmp_import_name_from_2, const_str_plain___all__ );
    Py_DECREF( tmp_import_name_from_2 );
    if ( tmp_assign_source_15 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 52;
        goto try_except_handler_1;
    }
    UPDATE_STRING_DICT1( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain___all__, tmp_assign_source_15 );
    goto try_end_1;
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

    tmp_cond_value_1 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_holding_threading );

    if (unlikely( tmp_cond_value_1 == NULL ))
    {
        tmp_cond_value_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_holding_threading );
    }

    if ( tmp_cond_value_1 == NULL )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "holding_threading" );
        exception_tb = NULL;

        exception_lineno = 57;
        goto frame_exception_exit_1;
    }

    tmp_cond_truth_1 = CHECK_IF_TRUE( tmp_cond_value_1 );
    if ( tmp_cond_truth_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );

        exception_lineno = 57;
        goto frame_exception_exit_1;
    }
    if ( tmp_cond_truth_1 == 1 )
    {
        goto branch_yes_4;
    }
    else
    {
        goto branch_no_4;
    }
    branch_yes_4:;
    tmp_ass_subvalue_4 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_held_threading );

    if (unlikely( tmp_ass_subvalue_4 == NULL ))
    {
        tmp_ass_subvalue_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_held_threading );
    }

    if ( tmp_ass_subvalue_4 == NULL )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "held_threading" );
        exception_tb = NULL;

        exception_lineno = 58;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscribed_4 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_ass_subscribed_4 == NULL ))
    {
        tmp_ass_subscribed_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_ass_subscribed_4 == NULL )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 58;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscript_4 = const_str_plain_threading;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_4, tmp_ass_subscript_4, tmp_ass_subvalue_4 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );

        exception_lineno = 58;
        goto frame_exception_exit_1;
    }
    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_held_threading );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 252 ], 36, 0 );
        exception_tb = NULL;

        exception_lineno = 59;
        goto frame_exception_exit_1;
    }

    branch_no_4:;
    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_holding_threading );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 288 ], 39, 0 );
        exception_tb = NULL;

        exception_lineno = 60;
        goto frame_exception_exit_1;
    }

    tmp_cond_value_2 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_holding__threading_local );

    if (unlikely( tmp_cond_value_2 == NULL ))
    {
        tmp_cond_value_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_holding__threading_local );
    }

    if ( tmp_cond_value_2 == NULL )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "holding__threading_local" );
        exception_tb = NULL;

        exception_lineno = 64;
        goto frame_exception_exit_1;
    }

    tmp_cond_truth_2 = CHECK_IF_TRUE( tmp_cond_value_2 );
    if ( tmp_cond_truth_2 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );

        exception_lineno = 64;
        goto frame_exception_exit_1;
    }
    if ( tmp_cond_truth_2 == 1 )
    {
        goto branch_yes_5;
    }
    else
    {
        goto branch_no_5;
    }
    branch_yes_5:;
    tmp_ass_subvalue_5 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_held__threading_local );

    if (unlikely( tmp_ass_subvalue_5 == NULL ))
    {
        tmp_ass_subvalue_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_held__threading_local );
    }

    if ( tmp_ass_subvalue_5 == NULL )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "held__threading_local" );
        exception_tb = NULL;

        exception_lineno = 65;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscribed_5 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_ass_subscribed_5 == NULL ))
    {
        tmp_ass_subscribed_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_ass_subscribed_5 == NULL )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 65;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscript_5 = const_str_plain__threading_local;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_5, tmp_ass_subscript_5, tmp_ass_subvalue_5 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );

        exception_lineno = 65;
        goto frame_exception_exit_1;
    }
    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_held__threading_local );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 327 ], 43, 0 );
        exception_tb = NULL;

        exception_lineno = 66;
        goto frame_exception_exit_1;
    }

    branch_no_5:;
    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_holding__threading_local );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 370 ], 46, 0 );
        exception_tb = NULL;

        exception_lineno = 67;
        goto frame_exception_exit_1;
    }

    tmp_cond_value_3 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_holding_thread );

    if (unlikely( tmp_cond_value_3 == NULL ))
    {
        tmp_cond_value_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_holding_thread );
    }

    if ( tmp_cond_value_3 == NULL )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "holding_thread" );
        exception_tb = NULL;

        exception_lineno = 70;
        goto frame_exception_exit_1;
    }

    tmp_cond_truth_3 = CHECK_IF_TRUE( tmp_cond_value_3 );
    if ( tmp_cond_truth_3 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );

        exception_lineno = 70;
        goto frame_exception_exit_1;
    }
    if ( tmp_cond_truth_3 == 1 )
    {
        goto branch_yes_6;
    }
    else
    {
        goto branch_no_6;
    }
    branch_yes_6:;
    tmp_ass_subvalue_6 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_held_thread );

    if (unlikely( tmp_ass_subvalue_6 == NULL ))
    {
        tmp_ass_subvalue_6 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_held_thread );
    }

    if ( tmp_ass_subvalue_6 == NULL )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "held_thread" );
        exception_tb = NULL;

        exception_lineno = 71;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscribed_6 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_ass_subscribed_6 == NULL ))
    {
        tmp_ass_subscribed_6 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_ass_subscribed_6 == NULL )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 71;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscript_6 = const_str_plain_thread;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_6, tmp_ass_subscript_6, tmp_ass_subvalue_6 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );

        exception_lineno = 71;
        goto frame_exception_exit_1;
    }
    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_held_thread );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 416 ], 33, 0 );
        exception_tb = NULL;

        exception_lineno = 72;
        goto frame_exception_exit_1;
    }

    goto branch_end_6;
    branch_no_6:;
    tmp_delsubscr_target_5 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_delsubscr_target_5 == NULL ))
    {
        tmp_delsubscr_target_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_delsubscr_target_5 == NULL )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 74;
        goto frame_exception_exit_1;
    }

    tmp_delsubscr_subscript_5 = const_str_plain_thread;
    tmp_result = DEL_SUBSCRIPT( tmp_delsubscr_target_5, tmp_delsubscr_subscript_5 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );

        exception_lineno = 74;
        goto frame_exception_exit_1;
    }
    branch_end_6:;
    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_holding_thread );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 449 ], 36, 0 );
        exception_tb = NULL;

        exception_lineno = 75;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_dummy_thread );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 485 ], 34, 0 );
        exception_tb = NULL;

        exception_lineno = 77;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_sys_modules );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 519 ], 33, 0 );
        exception_tb = NULL;

        exception_lineno = 78;
        goto frame_exception_exit_1;
    }

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto frame_exception_exit_1;
    // End of try:
    try_end_1:;
    tmp_cond_value_4 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_holding_threading );

    if (unlikely( tmp_cond_value_4 == NULL ))
    {
        tmp_cond_value_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_holding_threading );
    }

    if ( tmp_cond_value_4 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "holding_threading" );
        exception_tb = NULL;

        exception_lineno = 57;
        goto frame_exception_exit_1;
    }

    tmp_cond_truth_4 = CHECK_IF_TRUE( tmp_cond_value_4 );
    if ( tmp_cond_truth_4 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 57;
        goto frame_exception_exit_1;
    }
    if ( tmp_cond_truth_4 == 1 )
    {
        goto branch_yes_7;
    }
    else
    {
        goto branch_no_7;
    }
    branch_yes_7:;
    tmp_ass_subvalue_7 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_held_threading );

    if (unlikely( tmp_ass_subvalue_7 == NULL ))
    {
        tmp_ass_subvalue_7 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_held_threading );
    }

    if ( tmp_ass_subvalue_7 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "held_threading" );
        exception_tb = NULL;

        exception_lineno = 58;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscribed_7 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_ass_subscribed_7 == NULL ))
    {
        tmp_ass_subscribed_7 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_ass_subscribed_7 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 58;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscript_7 = const_str_plain_threading;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_7, tmp_ass_subscript_7, tmp_ass_subvalue_7 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 58;
        goto frame_exception_exit_1;
    }
    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_held_threading );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 252 ], 36, 0 );
        exception_tb = NULL;

        exception_lineno = 59;
        goto frame_exception_exit_1;
    }

    branch_no_7:;
    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_holding_threading );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 288 ], 39, 0 );
        exception_tb = NULL;

        exception_lineno = 60;
        goto frame_exception_exit_1;
    }

    tmp_cond_value_5 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_holding__threading_local );

    if (unlikely( tmp_cond_value_5 == NULL ))
    {
        tmp_cond_value_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_holding__threading_local );
    }

    if ( tmp_cond_value_5 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "holding__threading_local" );
        exception_tb = NULL;

        exception_lineno = 64;
        goto frame_exception_exit_1;
    }

    tmp_cond_truth_5 = CHECK_IF_TRUE( tmp_cond_value_5 );
    if ( tmp_cond_truth_5 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 64;
        goto frame_exception_exit_1;
    }
    if ( tmp_cond_truth_5 == 1 )
    {
        goto branch_yes_8;
    }
    else
    {
        goto branch_no_8;
    }
    branch_yes_8:;
    tmp_ass_subvalue_8 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_held__threading_local );

    if (unlikely( tmp_ass_subvalue_8 == NULL ))
    {
        tmp_ass_subvalue_8 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_held__threading_local );
    }

    if ( tmp_ass_subvalue_8 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "held__threading_local" );
        exception_tb = NULL;

        exception_lineno = 65;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscribed_8 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_ass_subscribed_8 == NULL ))
    {
        tmp_ass_subscribed_8 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_ass_subscribed_8 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 65;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscript_8 = const_str_plain__threading_local;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_8, tmp_ass_subscript_8, tmp_ass_subvalue_8 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 65;
        goto frame_exception_exit_1;
    }
    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_held__threading_local );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 327 ], 43, 0 );
        exception_tb = NULL;

        exception_lineno = 66;
        goto frame_exception_exit_1;
    }

    branch_no_8:;
    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_holding__threading_local );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 370 ], 46, 0 );
        exception_tb = NULL;

        exception_lineno = 67;
        goto frame_exception_exit_1;
    }

    tmp_cond_value_6 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_holding_thread );

    if (unlikely( tmp_cond_value_6 == NULL ))
    {
        tmp_cond_value_6 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_holding_thread );
    }

    if ( tmp_cond_value_6 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "holding_thread" );
        exception_tb = NULL;

        exception_lineno = 70;
        goto frame_exception_exit_1;
    }

    tmp_cond_truth_6 = CHECK_IF_TRUE( tmp_cond_value_6 );
    if ( tmp_cond_truth_6 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 70;
        goto frame_exception_exit_1;
    }
    if ( tmp_cond_truth_6 == 1 )
    {
        goto branch_yes_9;
    }
    else
    {
        goto branch_no_9;
    }
    branch_yes_9:;
    tmp_ass_subvalue_9 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_held_thread );

    if (unlikely( tmp_ass_subvalue_9 == NULL ))
    {
        tmp_ass_subvalue_9 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_held_thread );
    }

    if ( tmp_ass_subvalue_9 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "held_thread" );
        exception_tb = NULL;

        exception_lineno = 71;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscribed_9 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_ass_subscribed_9 == NULL ))
    {
        tmp_ass_subscribed_9 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_ass_subscribed_9 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 71;
        goto frame_exception_exit_1;
    }

    tmp_ass_subscript_9 = const_str_plain_thread;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_9, tmp_ass_subscript_9, tmp_ass_subvalue_9 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 71;
        goto frame_exception_exit_1;
    }
    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_held_thread );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 416 ], 33, 0 );
        exception_tb = NULL;

        exception_lineno = 72;
        goto frame_exception_exit_1;
    }

    goto branch_end_9;
    branch_no_9:;
    tmp_delsubscr_target_6 = GET_STRING_DICT_VALUE( moduledict_dummy_threading, (Nuitka_StringObject *)const_str_plain_sys_modules );

    if (unlikely( tmp_delsubscr_target_6 == NULL ))
    {
        tmp_delsubscr_target_6 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys_modules );
    }

    if ( tmp_delsubscr_target_6 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "sys_modules" );
        exception_tb = NULL;

        exception_lineno = 74;
        goto frame_exception_exit_1;
    }

    tmp_delsubscr_subscript_6 = const_str_plain_thread;
    tmp_result = DEL_SUBSCRIPT( tmp_delsubscr_target_6, tmp_delsubscr_subscript_6 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 74;
        goto frame_exception_exit_1;
    }
    branch_end_9:;
    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_holding_thread );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 449 ], 36, 0 );
        exception_tb = NULL;

        exception_lineno = 75;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_dummy_thread );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 485 ], 34, 0 );
        exception_tb = NULL;

        exception_lineno = 77;
        goto frame_exception_exit_1;
    }

    tmp_res = PyDict_DelItem( (PyObject *)moduledict_dummy_threading, const_str_plain_sys_modules );
    if ( tmp_res == -1 ) CLEAR_ERROR_OCCURRED();

    if ( tmp_res == -1 )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 519 ], 33, 0 );
        exception_tb = NULL;

        exception_lineno = 78;
        goto frame_exception_exit_1;
    }


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

    return MOD_RETURN_VALUE( module_dummy_threading );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
