/* Generated code for Python source for module 'pyreadline.clipboard.no_clipboard'
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

/* The _module_pyreadline$clipboard$no_clipboard is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_pyreadline$clipboard$no_clipboard;
PyDictObject *moduledict_pyreadline$clipboard$no_clipboard;

/* The module constants used, if any. */
extern PyObject *const_str_plain_GetClipboardText;
static PyObject *const_str_digest_f3e912707acf1bcc5f2e4f1e396e80f9;
extern PyObject *const_str_plain_text;
extern PyObject *const_str_plain_unicode_literals;
extern PyObject *const_str_plain___file__;
extern PyObject *const_str_plain_absolute_import;
extern PyObject *const_str_plain_SetClipboardText;
static PyObject *const_str_digest_4f2deb5c50664c8c8ccb8a16db3e46ed;
extern PyObject *const_unicode_empty;
static PyObject *const_str_plain_mybuffer;
extern PyObject *const_str_plain_print_function;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_tuple_str_plain_text_tuple;
extern PyObject *const_tuple_empty;
extern PyObject *const_dict_empty;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_digest_f3e912707acf1bcc5f2e4f1e396e80f9 = UNSTREAM_STRING( &constant_bin[ 768636 ], 36, 0 );
    const_str_digest_4f2deb5c50664c8c8ccb8a16db3e46ed = UNSTREAM_STRING( &constant_bin[ 768672 ], 33, 0 );
    const_str_plain_mybuffer = UNSTREAM_STRING( &constant_bin[ 768705 ], 8, 1 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_pyreadline$clipboard$no_clipboard( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_3600c777ffbd31e79563d98b24ab5c5f;
static PyCodeObject *codeobj_33b48c14dec00810956b8f185bb1ccf0;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_f3e912707acf1bcc5f2e4f1e396e80f9 );
    codeobj_3600c777ffbd31e79563d98b24ab5c5f = MAKE_CODEOBJ( module_filename_obj, const_str_plain_GetClipboardText, 13, const_tuple_empty, 0, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE | CO_FUTURE_UNICODE_LITERALS | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_PRINT_FUNCTION );
    codeobj_33b48c14dec00810956b8f185bb1ccf0 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_SetClipboardText, 16, const_tuple_str_plain_text_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE | CO_FUTURE_UNICODE_LITERALS | CO_FUTURE_ABSOLUTE_IMPORT | CO_FUTURE_PRINT_FUNCTION );
}

// The module function declarations.
static PyObject *MAKE_FUNCTION_function_1_GetClipboardText_of_pyreadline$clipboard$no_clipboard(  );


static PyObject *MAKE_FUNCTION_function_2_SetClipboardText_of_pyreadline$clipboard$no_clipboard(  );


// The module function definitions.
static PyObject *impl_function_1_GetClipboardText_of_pyreadline$clipboard$no_clipboard( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_3600c777ffbd31e79563d98b24ab5c5f, module_pyreadline$clipboard$no_clipboard );
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
    tmp_return_value = GET_STRING_DICT_VALUE( moduledict_pyreadline$clipboard$no_clipboard, (Nuitka_StringObject *)const_str_plain_mybuffer );

    if (unlikely( tmp_return_value == NULL ))
    {
        tmp_return_value = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_mybuffer );
    }

    if ( tmp_return_value == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "mybuffer" );
        exception_tb = NULL;

        exception_lineno = 14;
        goto frame_exception_exit_1;
    }

    Py_INCREF( tmp_return_value );
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
    goto function_return_exit;

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


            detachFrame( exception_tb, tmp_frame_locals );
        }
    }

    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );

    // Return the error.
    goto function_exception_exit;

    frame_no_exception_1:;


    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_1_GetClipboardText_of_pyreadline$clipboard$no_clipboard );
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


static PyObject *impl_function_2_SetClipboardText_of_pyreadline$clipboard$no_clipboard( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_text = python_pars[ 0 ];
    PyObject *tmp_assign_source_1;
    PyObject *tmp_return_value;
    tmp_return_value = NULL;

    // Actual function code.
    tmp_assign_source_1 = par_text;

    UPDATE_STRING_DICT0( moduledict_pyreadline$clipboard$no_clipboard, (Nuitka_StringObject *)const_str_plain_mybuffer, tmp_assign_source_1 );
    // Tried code:
    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_2_SetClipboardText_of_pyreadline$clipboard$no_clipboard );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_text );
    Py_DECREF( par_text );
    par_text = NULL;

    goto function_return_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_2_SetClipboardText_of_pyreadline$clipboard$no_clipboard );
    return NULL;

    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}



static PyObject *MAKE_FUNCTION_function_1_GetClipboardText_of_pyreadline$clipboard$no_clipboard(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_1_GetClipboardText_of_pyreadline$clipboard$no_clipboard,
        const_str_plain_GetClipboardText,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_3600c777ffbd31e79563d98b24ab5c5f,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_pyreadline$clipboard$no_clipboard,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_2_SetClipboardText_of_pyreadline$clipboard$no_clipboard(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_2_SetClipboardText_of_pyreadline$clipboard$no_clipboard,
        const_str_plain_SetClipboardText,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_33b48c14dec00810956b8f185bb1ccf0,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_pyreadline$clipboard$no_clipboard,
        Py_None
    );

    return result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_pyreadline$clipboard$no_clipboard =
{
    PyModuleDef_HEAD_INIT,
    "pyreadline.clipboard.no_clipboard",   /* m_name */
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

MOD_INIT_DECL( pyreadline$clipboard$no_clipboard )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_pyreadline$clipboard$no_clipboard );
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

    // puts( "in initpyreadline$clipboard$no_clipboard" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_pyreadline$clipboard$no_clipboard = Py_InitModule4(
        "pyreadline.clipboard.no_clipboard",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_pyreadline$clipboard$no_clipboard = PyModule_Create( &mdef_pyreadline$clipboard$no_clipboard );
#endif

    moduledict_pyreadline$clipboard$no_clipboard = (PyDictObject *)((PyModuleObject *)module_pyreadline$clipboard$no_clipboard)->md_dict;

    CHECK_OBJECT( module_pyreadline$clipboard$no_clipboard );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_digest_4f2deb5c50664c8c8ccb8a16db3e46ed, module_pyreadline$clipboard$no_clipboard );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_pyreadline$clipboard$no_clipboard );

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
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_assign_source_5;
    PyObject *tmp_assign_source_6;
    PyObject *tmp_assign_source_7;
    PyObject *tmp_assign_source_8;

    // Module code.
    tmp_assign_source_1 = Py_None;
    UPDATE_STRING_DICT0( moduledict_pyreadline$clipboard$no_clipboard, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_pyreadline$clipboard$no_clipboard, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_assign_source_3 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "print_function");
    UPDATE_STRING_DICT0( moduledict_pyreadline$clipboard$no_clipboard, (Nuitka_StringObject *)const_str_plain_print_function, tmp_assign_source_3 );
    tmp_assign_source_4 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "unicode_literals");
    UPDATE_STRING_DICT0( moduledict_pyreadline$clipboard$no_clipboard, (Nuitka_StringObject *)const_str_plain_unicode_literals, tmp_assign_source_4 );
    tmp_assign_source_5 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "absolute_import");
    UPDATE_STRING_DICT0( moduledict_pyreadline$clipboard$no_clipboard, (Nuitka_StringObject *)const_str_plain_absolute_import, tmp_assign_source_5 );
    tmp_assign_source_6 = const_unicode_empty;
    UPDATE_STRING_DICT0( moduledict_pyreadline$clipboard$no_clipboard, (Nuitka_StringObject *)const_str_plain_mybuffer, tmp_assign_source_6 );
    tmp_assign_source_7 = MAKE_FUNCTION_function_1_GetClipboardText_of_pyreadline$clipboard$no_clipboard(  );
    UPDATE_STRING_DICT1( moduledict_pyreadline$clipboard$no_clipboard, (Nuitka_StringObject *)const_str_plain_GetClipboardText, tmp_assign_source_7 );
    tmp_assign_source_8 = MAKE_FUNCTION_function_2_SetClipboardText_of_pyreadline$clipboard$no_clipboard(  );
    UPDATE_STRING_DICT1( moduledict_pyreadline$clipboard$no_clipboard, (Nuitka_StringObject *)const_str_plain_SetClipboardText, tmp_assign_source_8 );

    return MOD_RETURN_VALUE( module_pyreadline$clipboard$no_clipboard );
}
