/* Generated code for Python source for module 'isbnlib._data.data4info'
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

/* The _module_isbnlib$_data$data4info is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_isbnlib$_data$data4info;
PyDictObject *moduledict_isbnlib$_data$data4info;

/* The module constants used, if any. */
extern PyObject *const_str_plain_d;
extern PyObject *const_str_plain___file__;
static PyObject *const_dict_3010267b083f6147191bcd3d6251704c;
extern PyObject *const_str_plain_RDDATE;
static PyObject *const_str_digest_750579e4d64b95029049c6b1e9b2df95;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_20160427;
static PyObject *const_tuple_5469d81ef8f171fea2bd870e919a4419_tuple;
extern PyObject *const_str_plain_identifiers;
static PyObject *const_str_digest_33ab2f33dae2fc9d4b34af924e879e2c;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_dict_3010267b083f6147191bcd3d6251704c = PyMarshal_ReadObjectFromString( (char *)&constant_bin[ 429560 ], 6049 );
    const_str_digest_750579e4d64b95029049c6b1e9b2df95 = UNSTREAM_STRING( &constant_bin[ 435609 ], 23, 0 );
    const_tuple_5469d81ef8f171fea2bd870e919a4419_tuple = PyMarshal_ReadObjectFromString( (char *)&constant_bin[ 435632 ], 2939 );
    const_str_digest_33ab2f33dae2fc9d4b34af924e879e2c = UNSTREAM_STRING( &constant_bin[ 438571 ], 26, 0 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_isbnlib$_data$data4info( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.


static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_33ab2f33dae2fc9d4b34af924e879e2c );
}

// The module function declarations.


// The module function definitions.



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_isbnlib$_data$data4info =
{
    PyModuleDef_HEAD_INIT,
    "isbnlib._data.data4info",   /* m_name */
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

MOD_INIT_DECL( isbnlib$_data$data4info )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_isbnlib$_data$data4info );
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

    // puts( "in initisbnlib$_data$data4info" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_isbnlib$_data$data4info = Py_InitModule4(
        "isbnlib._data.data4info",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_isbnlib$_data$data4info = PyModule_Create( &mdef_isbnlib$_data$data4info );
#endif

    moduledict_isbnlib$_data$data4info = (PyDictObject *)((PyModuleObject *)module_isbnlib$_data$data4info)->md_dict;

    CHECK_OBJECT( module_isbnlib$_data$data4info );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_digest_750579e4d64b95029049c6b1e9b2df95, module_isbnlib$_data$data4info );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_isbnlib$_data$data4info );

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

    // Module code.
    tmp_assign_source_1 = Py_None;
    UPDATE_STRING_DICT0( moduledict_isbnlib$_data$data4info, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_isbnlib$_data$data4info, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_assign_source_3 = PyDict_Copy( const_dict_3010267b083f6147191bcd3d6251704c );
    UPDATE_STRING_DICT1( moduledict_isbnlib$_data$data4info, (Nuitka_StringObject *)const_str_plain_d, tmp_assign_source_3 );
    tmp_assign_source_4 = const_tuple_5469d81ef8f171fea2bd870e919a4419_tuple;
    UPDATE_STRING_DICT0( moduledict_isbnlib$_data$data4info, (Nuitka_StringObject *)const_str_plain_identifiers, tmp_assign_source_4 );
    tmp_assign_source_5 = const_str_plain_20160427;
    UPDATE_STRING_DICT0( moduledict_isbnlib$_data$data4info, (Nuitka_StringObject *)const_str_plain_RDDATE, tmp_assign_source_5 );

    return MOD_RETURN_VALUE( module_isbnlib$_data$data4info );
}
