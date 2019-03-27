/**
 * SC-Controller - Bindings
 *
 * Functions used by python (and potentially other) bindings.
 */

#pragma once
#ifdef __cplusplus
extern "C" {
#endif
#include "scc/action.h"
#include "scc/parameter.h"

#ifndef DLL_EXPORT
#if defined _WIN32 || defined __CYGWIN__
#	define DLL_EXPORT __declspec(dllexport)
#else
#	if __GNUC__ >= 4
#		define DLL_EXPORT __attribute__((visibility("default")))
#	else
#		define DLL_EXPORT
#	endif
#endif
#endif

typedef union { ParamOE* p; ActionOE* a; ActionError* e; } APError;

typedef struct EnumValue {
	const char*		name;
	uint32_t		value;
} EnumValue;

/**
 * Returns action type.
 * Returned string should not be modified and will be kept in memory
 * at least until action is deallocated.
 */
DLL_EXPORT const char* scc_action_get_type(Action* a);

/**
 * Returns named property of action.
 *
 * Returns Parameter* instance with one reference that caller has to release or
 * NULL if property with such name is not known.
 */
DLL_EXPORT Parameter* scc_action_get_property(Action* a, const char* name);

/**
 * Calls compress method on action and returns Action that it returns, or NULL
 * if it returs itself. If 'a' is NULL, action it points to doesn't have compress
 * method defined, function returns NULL.
 *
 * If returned value is not NULL, caller has to release reference on it.
  */
DLL_EXPORT Action* scc_action_get_compressed(Action* a);

/**
 * For applicable modifiers, returns child action.
 * For everything else, returns NULL.
 *
 * If returned value is not NULL, caller has to release reference on it.
 */
DLL_EXPORT Action* scc_action_get_child(Action* a);

/** Increases reference count on action */
DLL_EXPORT Action* scc_action_ref(Action* a);

/** Unreferences action */
DLL_EXPORT void scc_action_unref(Action* a);

/** Increases reference count on parameter */
DLL_EXPORT Parameter* scc_parameter_ref(Parameter* p);

/** Unreferences parameter */
DLL_EXPORT void scc_parameter_unref(Parameter* p);

/** Returns error message */
DLL_EXPORT const char* scc_error_get_message(APError e);

/** Parses array of paramertrers into action */
DLL_EXPORT ActionOE scc_action_new_from_array(const char* keyword, size_t count, Parameter* params[]);


#undef scc_parameter_as_action
#undef scc_parameter_as_string
#undef scc_parameter_as_int
#undef scc_parameter_as_float

/**
 * Returns Action instance without increasing reference count.
 * If caller wish to keep reference to Action after Parameter is dereferenced,
 * it should call scc_action_ref.
 */
DLL_EXPORT Action* scc_parameter_as_action(Parameter* p);

/** Returns char* which should not be deallocated nor modified by caller */
DLL_EXPORT const char* scc_parameter_as_string(Parameter* p);

DLL_EXPORT int64_t scc_parameter_as_int(Parameter* p);

DLL_EXPORT float scc_parameter_as_float(Parameter* p);

DLL_EXPORT uint8_t scc_parameter_tuple_get_count(Parameter* p);

DLL_EXPORT Parameter* scc_parameter_tuple_get_child(Parameter* p, uint8_t n);

/**
 * Fills constants into pre-allocated array. 'count' is number of values to which
 * array is allocated.
 * Returns actual number of values. If this number is larger than 'count',
 * array is left in undefined state (partially overwritten).
 */
DLL_EXPORT size_t scc_get_key_constants(EnumValue array[], size_t count);

/** Same as scc_get_key_constants, but returns names of absolute axes */
DLL_EXPORT size_t scc_get_axis_constants(EnumValue array[], size_t count);

/** Same as scc_get_key_constants, but returns names of relative axes */
DLL_EXPORT size_t scc_get_rels_constants(EnumValue array[], size_t count);

/** Same as scc_get_key_constants, but returns button names */
DLL_EXPORT size_t scc_get_button_constants(EnumValue array[], size_t count);

/**
 * Converts constant name into constant-parameter.
 * Caller has to dereference returned parameter.
 *
 * Returns NULL if name is not recognized.
 */
DLL_EXPORT Parameter* scc_get_const_parameter(const char* name);

/**
 * Returns directory where shared files are kept.
 * Usually /usr/share/scc, cwd() or $SCC_SHARED if defined
 * Returned value is cached internally and should NOT be free'd by caller.
 */
DLL_EXPORT const char* scc_get_share_path();


#ifdef __cplusplus
}
#endif
