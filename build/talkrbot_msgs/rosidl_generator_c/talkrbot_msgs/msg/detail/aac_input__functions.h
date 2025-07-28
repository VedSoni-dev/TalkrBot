// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from talkrbot_msgs:msg/AACInput.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__FUNCTIONS_H_
#define TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "talkrbot_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "talkrbot_msgs/msg/detail/aac_input__struct.h"

/// Initialize msg/AACInput message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * talkrbot_msgs__msg__AACInput
 * )) before or use
 * talkrbot_msgs__msg__AACInput__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
bool
talkrbot_msgs__msg__AACInput__init(talkrbot_msgs__msg__AACInput * msg);

/// Finalize msg/AACInput message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
void
talkrbot_msgs__msg__AACInput__fini(talkrbot_msgs__msg__AACInput * msg);

/// Create msg/AACInput message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * talkrbot_msgs__msg__AACInput__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
talkrbot_msgs__msg__AACInput *
talkrbot_msgs__msg__AACInput__create();

/// Destroy msg/AACInput message.
/**
 * It calls
 * talkrbot_msgs__msg__AACInput__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
void
talkrbot_msgs__msg__AACInput__destroy(talkrbot_msgs__msg__AACInput * msg);

/// Check for msg/AACInput message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
bool
talkrbot_msgs__msg__AACInput__are_equal(const talkrbot_msgs__msg__AACInput * lhs, const talkrbot_msgs__msg__AACInput * rhs);

/// Copy a msg/AACInput message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
bool
talkrbot_msgs__msg__AACInput__copy(
  const talkrbot_msgs__msg__AACInput * input,
  talkrbot_msgs__msg__AACInput * output);

/// Initialize array of msg/AACInput messages.
/**
 * It allocates the memory for the number of elements and calls
 * talkrbot_msgs__msg__AACInput__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
bool
talkrbot_msgs__msg__AACInput__Sequence__init(talkrbot_msgs__msg__AACInput__Sequence * array, size_t size);

/// Finalize array of msg/AACInput messages.
/**
 * It calls
 * talkrbot_msgs__msg__AACInput__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
void
talkrbot_msgs__msg__AACInput__Sequence__fini(talkrbot_msgs__msg__AACInput__Sequence * array);

/// Create array of msg/AACInput messages.
/**
 * It allocates the memory for the array and calls
 * talkrbot_msgs__msg__AACInput__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
talkrbot_msgs__msg__AACInput__Sequence *
talkrbot_msgs__msg__AACInput__Sequence__create(size_t size);

/// Destroy array of msg/AACInput messages.
/**
 * It calls
 * talkrbot_msgs__msg__AACInput__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
void
talkrbot_msgs__msg__AACInput__Sequence__destroy(talkrbot_msgs__msg__AACInput__Sequence * array);

/// Check for msg/AACInput message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
bool
talkrbot_msgs__msg__AACInput__Sequence__are_equal(const talkrbot_msgs__msg__AACInput__Sequence * lhs, const talkrbot_msgs__msg__AACInput__Sequence * rhs);

/// Copy an array of msg/AACInput messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
bool
talkrbot_msgs__msg__AACInput__Sequence__copy(
  const talkrbot_msgs__msg__AACInput__Sequence * input,
  talkrbot_msgs__msg__AACInput__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__FUNCTIONS_H_
