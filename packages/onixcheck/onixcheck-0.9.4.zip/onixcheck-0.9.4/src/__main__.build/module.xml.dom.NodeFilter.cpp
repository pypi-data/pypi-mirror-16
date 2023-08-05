/* Generated code for Python source for module 'xml.dom.NodeFilter'
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

/* The _module_xml$dom$NodeFilter is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_xml$dom$NodeFilter;
PyDictObject *moduledict_xml$dom$NodeFilter;

/* The module constants used, if any. */
extern PyObject *const_int_pos_128;
extern PyObject *const_str_plain_FILTER_REJECT;
extern PyObject *const_int_pos_256;
extern PyObject *const_int_pos_512;
extern PyObject *const_tuple_str_plain_self_str_plain_node_tuple;
extern PyObject *const_str_digest_f52f7eb89331b9ab3a2c4d75c53fe979;
extern PyObject *const_str_plain_FILTER_SKIP;
extern PyObject *const_str_plain_NodeFilter;
extern PyObject *const_str_plain_SHOW_DOCUMENT_TYPE;
extern PyObject *const_dict_empty;
static PyObject *const_str_digest_882ea31e6be6a7f406762ed1b8f5ce6d;
extern PyObject *const_str_plain_SHOW_ENTITY;
extern PyObject *const_int_pos_32;
extern PyObject *const_str_plain_SHOW_ELEMENT;
extern PyObject *const_int_pos_16;
extern PyObject *const_str_plain_SHOW_DOCUMENT;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_SHOW_NOTATION;
static PyObject *const_str_digest_18dba3c8fc4bad783e9c20669830f69c;
extern PyObject *const_str_plain_SHOW_ENTITY_REFERENCE;
extern PyObject *const_str_plain___file__;
extern PyObject *const_long_pos_4294967295;
extern PyObject *const_str_plain_SHOW_CDATA_SECTION;
extern PyObject *const_int_pos_4;
extern PyObject *const_int_pos_2;
extern PyObject *const_int_pos_3;
extern PyObject *const_int_pos_1;
extern PyObject *const_str_plain_acceptNode;
extern PyObject *const_str_plain_SHOW_PROCESSING_INSTRUCTION;
extern PyObject *const_tuple_empty;
extern PyObject *const_int_pos_8;
extern PyObject *const_str_plain_SHOW_TEXT;
extern PyObject *const_str_plain_SHOW_ALL;
extern PyObject *const_str_plain___module__;
extern PyObject *const_str_plain_node;
extern PyObject *const_str_plain_self;
extern PyObject *const_int_pos_1024;
extern PyObject *const_str_plain___metaclass__;
extern PyObject *const_int_pos_2048;
extern PyObject *const_str_plain_SHOW_DOCUMENT_FRAGMENT;
extern PyObject *const_int_pos_64;
extern PyObject *const_str_plain_SHOW_COMMENT;
extern PyObject *const_str_plain_SHOW_ATTRIBUTE;
extern PyObject *const_str_plain_FILTER_ACCEPT;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_digest_882ea31e6be6a7f406762ed1b8f5ce6d = UNSTREAM_STRING( &constant_bin[ 1164154 ], 76, 0 );
    const_str_digest_18dba3c8fc4bad783e9c20669830f69c = UNSTREAM_STRING( &constant_bin[ 1164230 ], 21, 0 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_xml$dom$NodeFilter( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_aa05aa779440bbdb5e1cc3f6de93d03e;
static PyCodeObject *codeobj_361d41a06243806a9daf5c7461d20faf;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_18dba3c8fc4bad783e9c20669830f69c );
    codeobj_aa05aa779440bbdb5e1cc3f6de93d03e = MAKE_CODEOBJ( module_filename_obj, const_str_plain_NodeFilter, 1, const_tuple_empty, 0, CO_NOFREE );
    codeobj_361d41a06243806a9daf5c7461d20faf = MAKE_CODEOBJ( module_filename_obj, const_str_plain_acceptNode, 26, const_tuple_str_plain_self_str_plain_node_tuple, 2, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
}

// The module function declarations.
NUITKA_LOCAL_MODULE PyObject *impl_class_1_NodeFilter_of_xml$dom$NodeFilter( PyObject **python_pars );


static PyObject *MAKE_FUNCTION_function_1_acceptNode_of_class_1_NodeFilter_of_xml$dom$NodeFilter(  );


// The module function definitions.
NUITKA_LOCAL_MODULE PyObject *impl_class_1_NodeFilter_of_xml$dom$NodeFilter( PyObject **python_pars )
{
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
    assert(!had_error); // Do not enter inlined functions with error set.
#endif

    // Local variable declarations.
    PyObject *var___module__ = NULL;
    PyObject *var___doc__ = NULL;
    PyObject *var_FILTER_ACCEPT = NULL;
    PyObject *var_FILTER_REJECT = NULL;
    PyObject *var_FILTER_SKIP = NULL;
    PyObject *var_SHOW_ALL = NULL;
    PyObject *var_SHOW_ELEMENT = NULL;
    PyObject *var_SHOW_ATTRIBUTE = NULL;
    PyObject *var_SHOW_TEXT = NULL;
    PyObject *var_SHOW_CDATA_SECTION = NULL;
    PyObject *var_SHOW_ENTITY_REFERENCE = NULL;
    PyObject *var_SHOW_ENTITY = NULL;
    PyObject *var_SHOW_PROCESSING_INSTRUCTION = NULL;
    PyObject *var_SHOW_COMMENT = NULL;
    PyObject *var_SHOW_DOCUMENT = NULL;
    PyObject *var_SHOW_DOCUMENT_TYPE = NULL;
    PyObject *var_SHOW_DOCUMENT_FRAGMENT = NULL;
    PyObject *var_SHOW_NOTATION = NULL;
    PyObject *var_acceptNode = NULL;
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
    PyObject *tmp_assign_source_16;
    PyObject *tmp_assign_source_17;
    PyObject *tmp_assign_source_18;
    PyObject *tmp_assign_source_19;
    PyObject *tmp_return_value;
    tmp_return_value = NULL;

    // Actual function code.
    tmp_assign_source_1 = const_str_digest_f52f7eb89331b9ab3a2c4d75c53fe979;
    assert( var___module__ == NULL );
    Py_INCREF( tmp_assign_source_1 );
    var___module__ = tmp_assign_source_1;

    tmp_assign_source_2 = const_str_digest_882ea31e6be6a7f406762ed1b8f5ce6d;
    assert( var___doc__ == NULL );
    Py_INCREF( tmp_assign_source_2 );
    var___doc__ = tmp_assign_source_2;

    tmp_assign_source_3 = const_int_pos_1;
    assert( var_FILTER_ACCEPT == NULL );
    Py_INCREF( tmp_assign_source_3 );
    var_FILTER_ACCEPT = tmp_assign_source_3;

    tmp_assign_source_4 = const_int_pos_2;
    assert( var_FILTER_REJECT == NULL );
    Py_INCREF( tmp_assign_source_4 );
    var_FILTER_REJECT = tmp_assign_source_4;

    tmp_assign_source_5 = const_int_pos_3;
    assert( var_FILTER_SKIP == NULL );
    Py_INCREF( tmp_assign_source_5 );
    var_FILTER_SKIP = tmp_assign_source_5;

    tmp_assign_source_6 = const_long_pos_4294967295;
    assert( var_SHOW_ALL == NULL );
    Py_INCREF( tmp_assign_source_6 );
    var_SHOW_ALL = tmp_assign_source_6;

    tmp_assign_source_7 = const_int_pos_1;
    assert( var_SHOW_ELEMENT == NULL );
    Py_INCREF( tmp_assign_source_7 );
    var_SHOW_ELEMENT = tmp_assign_source_7;

    tmp_assign_source_8 = const_int_pos_2;
    assert( var_SHOW_ATTRIBUTE == NULL );
    Py_INCREF( tmp_assign_source_8 );
    var_SHOW_ATTRIBUTE = tmp_assign_source_8;

    tmp_assign_source_9 = const_int_pos_4;
    assert( var_SHOW_TEXT == NULL );
    Py_INCREF( tmp_assign_source_9 );
    var_SHOW_TEXT = tmp_assign_source_9;

    tmp_assign_source_10 = const_int_pos_8;
    assert( var_SHOW_CDATA_SECTION == NULL );
    Py_INCREF( tmp_assign_source_10 );
    var_SHOW_CDATA_SECTION = tmp_assign_source_10;

    tmp_assign_source_11 = const_int_pos_16;
    assert( var_SHOW_ENTITY_REFERENCE == NULL );
    Py_INCREF( tmp_assign_source_11 );
    var_SHOW_ENTITY_REFERENCE = tmp_assign_source_11;

    tmp_assign_source_12 = const_int_pos_32;
    assert( var_SHOW_ENTITY == NULL );
    Py_INCREF( tmp_assign_source_12 );
    var_SHOW_ENTITY = tmp_assign_source_12;

    tmp_assign_source_13 = const_int_pos_64;
    assert( var_SHOW_PROCESSING_INSTRUCTION == NULL );
    Py_INCREF( tmp_assign_source_13 );
    var_SHOW_PROCESSING_INSTRUCTION = tmp_assign_source_13;

    tmp_assign_source_14 = const_int_pos_128;
    assert( var_SHOW_COMMENT == NULL );
    Py_INCREF( tmp_assign_source_14 );
    var_SHOW_COMMENT = tmp_assign_source_14;

    tmp_assign_source_15 = const_int_pos_256;
    assert( var_SHOW_DOCUMENT == NULL );
    Py_INCREF( tmp_assign_source_15 );
    var_SHOW_DOCUMENT = tmp_assign_source_15;

    tmp_assign_source_16 = const_int_pos_512;
    assert( var_SHOW_DOCUMENT_TYPE == NULL );
    Py_INCREF( tmp_assign_source_16 );
    var_SHOW_DOCUMENT_TYPE = tmp_assign_source_16;

    tmp_assign_source_17 = const_int_pos_1024;
    assert( var_SHOW_DOCUMENT_FRAGMENT == NULL );
    Py_INCREF( tmp_assign_source_17 );
    var_SHOW_DOCUMENT_FRAGMENT = tmp_assign_source_17;

    tmp_assign_source_18 = const_int_pos_2048;
    assert( var_SHOW_NOTATION == NULL );
    Py_INCREF( tmp_assign_source_18 );
    var_SHOW_NOTATION = tmp_assign_source_18;

    tmp_assign_source_19 = MAKE_FUNCTION_function_1_acceptNode_of_class_1_NodeFilter_of_xml$dom$NodeFilter(  );
    assert( var_acceptNode == NULL );
    var_acceptNode = tmp_assign_source_19;

    // Tried code:
    tmp_return_value = PyDict_New();
    if ( var___module__ )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain___module__,
            var___module__
        );

        assert( res == 0 );
    }

    if ( var___doc__ )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain___doc__,
            var___doc__
        );

        assert( res == 0 );
    }

    if ( var_FILTER_ACCEPT )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_FILTER_ACCEPT,
            var_FILTER_ACCEPT
        );

        assert( res == 0 );
    }

    if ( var_FILTER_REJECT )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_FILTER_REJECT,
            var_FILTER_REJECT
        );

        assert( res == 0 );
    }

    if ( var_FILTER_SKIP )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_FILTER_SKIP,
            var_FILTER_SKIP
        );

        assert( res == 0 );
    }

    if ( var_SHOW_ALL )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_ALL,
            var_SHOW_ALL
        );

        assert( res == 0 );
    }

    if ( var_SHOW_ELEMENT )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_ELEMENT,
            var_SHOW_ELEMENT
        );

        assert( res == 0 );
    }

    if ( var_SHOW_ATTRIBUTE )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_ATTRIBUTE,
            var_SHOW_ATTRIBUTE
        );

        assert( res == 0 );
    }

    if ( var_SHOW_TEXT )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_TEXT,
            var_SHOW_TEXT
        );

        assert( res == 0 );
    }

    if ( var_SHOW_CDATA_SECTION )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_CDATA_SECTION,
            var_SHOW_CDATA_SECTION
        );

        assert( res == 0 );
    }

    if ( var_SHOW_ENTITY_REFERENCE )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_ENTITY_REFERENCE,
            var_SHOW_ENTITY_REFERENCE
        );

        assert( res == 0 );
    }

    if ( var_SHOW_ENTITY )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_ENTITY,
            var_SHOW_ENTITY
        );

        assert( res == 0 );
    }

    if ( var_SHOW_PROCESSING_INSTRUCTION )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_PROCESSING_INSTRUCTION,
            var_SHOW_PROCESSING_INSTRUCTION
        );

        assert( res == 0 );
    }

    if ( var_SHOW_COMMENT )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_COMMENT,
            var_SHOW_COMMENT
        );

        assert( res == 0 );
    }

    if ( var_SHOW_DOCUMENT )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_DOCUMENT,
            var_SHOW_DOCUMENT
        );

        assert( res == 0 );
    }

    if ( var_SHOW_DOCUMENT_TYPE )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_DOCUMENT_TYPE,
            var_SHOW_DOCUMENT_TYPE
        );

        assert( res == 0 );
    }

    if ( var_SHOW_DOCUMENT_FRAGMENT )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_DOCUMENT_FRAGMENT,
            var_SHOW_DOCUMENT_FRAGMENT
        );

        assert( res == 0 );
    }

    if ( var_SHOW_NOTATION )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_SHOW_NOTATION,
            var_SHOW_NOTATION
        );

        assert( res == 0 );
    }

    if ( var_acceptNode )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_acceptNode,
            var_acceptNode
        );

        assert( res == 0 );
    }

    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( class_1_NodeFilter_of_xml$dom$NodeFilter );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)var___module__ );
    Py_DECREF( var___module__ );
    var___module__ = NULL;

    CHECK_OBJECT( (PyObject *)var___doc__ );
    Py_DECREF( var___doc__ );
    var___doc__ = NULL;

    CHECK_OBJECT( (PyObject *)var_FILTER_ACCEPT );
    Py_DECREF( var_FILTER_ACCEPT );
    var_FILTER_ACCEPT = NULL;

    CHECK_OBJECT( (PyObject *)var_FILTER_REJECT );
    Py_DECREF( var_FILTER_REJECT );
    var_FILTER_REJECT = NULL;

    CHECK_OBJECT( (PyObject *)var_FILTER_SKIP );
    Py_DECREF( var_FILTER_SKIP );
    var_FILTER_SKIP = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_ALL );
    Py_DECREF( var_SHOW_ALL );
    var_SHOW_ALL = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_ELEMENT );
    Py_DECREF( var_SHOW_ELEMENT );
    var_SHOW_ELEMENT = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_ATTRIBUTE );
    Py_DECREF( var_SHOW_ATTRIBUTE );
    var_SHOW_ATTRIBUTE = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_TEXT );
    Py_DECREF( var_SHOW_TEXT );
    var_SHOW_TEXT = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_CDATA_SECTION );
    Py_DECREF( var_SHOW_CDATA_SECTION );
    var_SHOW_CDATA_SECTION = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_ENTITY_REFERENCE );
    Py_DECREF( var_SHOW_ENTITY_REFERENCE );
    var_SHOW_ENTITY_REFERENCE = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_ENTITY );
    Py_DECREF( var_SHOW_ENTITY );
    var_SHOW_ENTITY = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_PROCESSING_INSTRUCTION );
    Py_DECREF( var_SHOW_PROCESSING_INSTRUCTION );
    var_SHOW_PROCESSING_INSTRUCTION = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_COMMENT );
    Py_DECREF( var_SHOW_COMMENT );
    var_SHOW_COMMENT = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_DOCUMENT );
    Py_DECREF( var_SHOW_DOCUMENT );
    var_SHOW_DOCUMENT = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_DOCUMENT_TYPE );
    Py_DECREF( var_SHOW_DOCUMENT_TYPE );
    var_SHOW_DOCUMENT_TYPE = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_DOCUMENT_FRAGMENT );
    Py_DECREF( var_SHOW_DOCUMENT_FRAGMENT );
    var_SHOW_DOCUMENT_FRAGMENT = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_NOTATION );
    Py_DECREF( var_SHOW_NOTATION );
    var_SHOW_NOTATION = NULL;

    CHECK_OBJECT( (PyObject *)var_acceptNode );
    Py_DECREF( var_acceptNode );
    var_acceptNode = NULL;

    goto function_return_exit;
    // End of try:
    CHECK_OBJECT( (PyObject *)var___module__ );
    Py_DECREF( var___module__ );
    var___module__ = NULL;

    CHECK_OBJECT( (PyObject *)var___doc__ );
    Py_DECREF( var___doc__ );
    var___doc__ = NULL;

    CHECK_OBJECT( (PyObject *)var_FILTER_ACCEPT );
    Py_DECREF( var_FILTER_ACCEPT );
    var_FILTER_ACCEPT = NULL;

    CHECK_OBJECT( (PyObject *)var_FILTER_REJECT );
    Py_DECREF( var_FILTER_REJECT );
    var_FILTER_REJECT = NULL;

    CHECK_OBJECT( (PyObject *)var_FILTER_SKIP );
    Py_DECREF( var_FILTER_SKIP );
    var_FILTER_SKIP = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_ALL );
    Py_DECREF( var_SHOW_ALL );
    var_SHOW_ALL = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_ELEMENT );
    Py_DECREF( var_SHOW_ELEMENT );
    var_SHOW_ELEMENT = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_ATTRIBUTE );
    Py_DECREF( var_SHOW_ATTRIBUTE );
    var_SHOW_ATTRIBUTE = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_TEXT );
    Py_DECREF( var_SHOW_TEXT );
    var_SHOW_TEXT = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_CDATA_SECTION );
    Py_DECREF( var_SHOW_CDATA_SECTION );
    var_SHOW_CDATA_SECTION = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_ENTITY_REFERENCE );
    Py_DECREF( var_SHOW_ENTITY_REFERENCE );
    var_SHOW_ENTITY_REFERENCE = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_ENTITY );
    Py_DECREF( var_SHOW_ENTITY );
    var_SHOW_ENTITY = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_PROCESSING_INSTRUCTION );
    Py_DECREF( var_SHOW_PROCESSING_INSTRUCTION );
    var_SHOW_PROCESSING_INSTRUCTION = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_COMMENT );
    Py_DECREF( var_SHOW_COMMENT );
    var_SHOW_COMMENT = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_DOCUMENT );
    Py_DECREF( var_SHOW_DOCUMENT );
    var_SHOW_DOCUMENT = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_DOCUMENT_TYPE );
    Py_DECREF( var_SHOW_DOCUMENT_TYPE );
    var_SHOW_DOCUMENT_TYPE = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_DOCUMENT_FRAGMENT );
    Py_DECREF( var_SHOW_DOCUMENT_FRAGMENT );
    var_SHOW_DOCUMENT_FRAGMENT = NULL;

    CHECK_OBJECT( (PyObject *)var_SHOW_NOTATION );
    Py_DECREF( var_SHOW_NOTATION );
    var_SHOW_NOTATION = NULL;

    CHECK_OBJECT( (PyObject *)var_acceptNode );
    Py_DECREF( var_acceptNode );
    var_acceptNode = NULL;


    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( class_1_NodeFilter_of_xml$dom$NodeFilter );
    return NULL;

    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}


static PyObject *impl_function_1_acceptNode_of_class_1_NodeFilter_of_xml$dom$NodeFilter( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_self = python_pars[ 0 ];
    PyObject *par_node = python_pars[ 1 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_raise_type_1;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;


    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_361d41a06243806a9daf5c7461d20faf, module_xml$dom$NodeFilter );
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
    tmp_raise_type_1 = PyExc_NotImplementedError;
    exception_type = tmp_raise_type_1;
    Py_INCREF( tmp_raise_type_1 );
    exception_lineno = 27;
    RAISE_EXCEPTION_WITH_TYPE( &exception_type, &exception_value, &exception_tb );
    goto frame_exception_exit_1;

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
            if ( par_self )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_self,
                    par_self
                );

                assert( res == 0 );
            }

            if ( par_node )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_node,
                    par_node
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
    NUITKA_CANNOT_GET_HERE( function_1_acceptNode_of_class_1_NodeFilter_of_xml$dom$NodeFilter );
    return NULL;
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

    CHECK_OBJECT( (PyObject *)par_self );
    Py_DECREF( par_self );
    par_self = NULL;

    CHECK_OBJECT( (PyObject *)par_node );
    Py_DECREF( par_node );
    par_node = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_1_acceptNode_of_class_1_NodeFilter_of_xml$dom$NodeFilter );
    return NULL;

function_exception_exit:
    assert( exception_type );
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );

    return NULL;

}



static PyObject *MAKE_FUNCTION_function_1_acceptNode_of_class_1_NodeFilter_of_xml$dom$NodeFilter(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_1_acceptNode_of_class_1_NodeFilter_of_xml$dom$NodeFilter,
        const_str_plain_acceptNode,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_361d41a06243806a9daf5c7461d20faf,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_xml$dom$NodeFilter,
        Py_None
    );

    return result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_xml$dom$NodeFilter =
{
    PyModuleDef_HEAD_INIT,
    "xml.dom.NodeFilter",   /* m_name */
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

MOD_INIT_DECL( xml$dom$NodeFilter )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_xml$dom$NodeFilter );
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

    // puts( "in initxml$dom$NodeFilter" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_xml$dom$NodeFilter = Py_InitModule4(
        "xml.dom.NodeFilter",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_xml$dom$NodeFilter = PyModule_Create( &mdef_xml$dom$NodeFilter );
#endif

    moduledict_xml$dom$NodeFilter = (PyDictObject *)((PyModuleObject *)module_xml$dom$NodeFilter)->md_dict;

    CHECK_OBJECT( module_xml$dom$NodeFilter );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_digest_f52f7eb89331b9ab3a2c4d75c53fe979, module_xml$dom$NodeFilter );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_xml$dom$NodeFilter );

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
    PyObject *tmp_class_creation_1__class_dict = NULL;
    PyObject *tmp_class_creation_1__metaclass = NULL;
    PyObject *tmp_class_creation_1__class = NULL;
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
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_assign_source_5;
    PyObject *tmp_assign_source_6;
    PyObject *tmp_bases_name_1;
    PyObject *tmp_called_name_1;
    int tmp_cmp_In_1;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_dict_name_1;
    PyObject *tmp_key_name_1;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = Py_None;
    UPDATE_STRING_DICT0( moduledict_xml$dom$NodeFilter, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_xml$dom$NodeFilter, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_assign_source_3 = impl_class_1_NodeFilter_of_xml$dom$NodeFilter( NULL );
    assert( tmp_assign_source_3 != NULL );
    assert( tmp_class_creation_1__class_dict == NULL );
    tmp_class_creation_1__class_dict = tmp_assign_source_3;

    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_aa05aa779440bbdb5e1cc3f6de93d03e, module_xml$dom$NodeFilter );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    // Tried code:
    tmp_compare_left_1 = const_str_plain___metaclass__;
    tmp_compare_right_1 = tmp_class_creation_1__class_dict;

    tmp_cmp_In_1 = PySequence_Contains( tmp_compare_right_1, tmp_compare_left_1 );
    assert( !(tmp_cmp_In_1 == -1) );
    if ( tmp_cmp_In_1 == 1 )
    {
        goto condexpr_true_1;
    }
    else
    {
        goto condexpr_false_1;
    }
    condexpr_true_1:;
    tmp_dict_name_1 = tmp_class_creation_1__class_dict;

    tmp_key_name_1 = const_str_plain___metaclass__;
    tmp_assign_source_4 = DICT_GET_ITEM( tmp_dict_name_1, tmp_key_name_1 );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto try_except_handler_1;
    }
    goto condexpr_end_1;
    condexpr_false_1:;
    tmp_bases_name_1 = const_tuple_empty;
    tmp_assign_source_4 = SELECT_METACLASS( tmp_bases_name_1, GET_STRING_DICT_VALUE( moduledict_xml$dom$NodeFilter, (Nuitka_StringObject *)const_str_plain___metaclass__ ) );
    condexpr_end_1:;
    assert( tmp_class_creation_1__metaclass == NULL );
    tmp_class_creation_1__metaclass = tmp_assign_source_4;

    tmp_called_name_1 = tmp_class_creation_1__metaclass;

    tmp_args_element_name_1 = const_str_plain_NodeFilter;
    tmp_args_element_name_2 = const_tuple_empty;
    tmp_args_element_name_3 = tmp_class_creation_1__class_dict;

    frame_module->f_lineno = 4;
    {
        PyObject *call_args[] = { tmp_args_element_name_1, tmp_args_element_name_2, tmp_args_element_name_3 };
        tmp_assign_source_5 = CALL_FUNCTION_WITH_ARGS3( tmp_called_name_1, call_args );
    }

    if ( tmp_assign_source_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto try_except_handler_1;
    }
    assert( tmp_class_creation_1__class == NULL );
    tmp_class_creation_1__class = tmp_assign_source_5;

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

    CHECK_OBJECT( (PyObject *)tmp_class_creation_1__class_dict );
    Py_DECREF( tmp_class_creation_1__class_dict );
    tmp_class_creation_1__class_dict = NULL;

    Py_XDECREF( tmp_class_creation_1__metaclass );
    tmp_class_creation_1__metaclass = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto frame_exception_exit_1;
    // End of try:
    try_end_1:;

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
    tmp_assign_source_6 = tmp_class_creation_1__class;

    UPDATE_STRING_DICT0( moduledict_xml$dom$NodeFilter, (Nuitka_StringObject *)const_str_plain_NodeFilter, tmp_assign_source_6 );
    CHECK_OBJECT( (PyObject *)tmp_class_creation_1__class );
    Py_DECREF( tmp_class_creation_1__class );
    tmp_class_creation_1__class = NULL;

    CHECK_OBJECT( (PyObject *)tmp_class_creation_1__class_dict );
    Py_DECREF( tmp_class_creation_1__class_dict );
    tmp_class_creation_1__class_dict = NULL;

    CHECK_OBJECT( (PyObject *)tmp_class_creation_1__metaclass );
    Py_DECREF( tmp_class_creation_1__metaclass );
    tmp_class_creation_1__metaclass = NULL;


    return MOD_RETURN_VALUE( module_xml$dom$NodeFilter );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
