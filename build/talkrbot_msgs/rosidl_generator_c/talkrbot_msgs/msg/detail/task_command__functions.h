// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from talkrbot_msgs:msg/TaskCommand.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__FUNCTIONS_H_
#define TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "talkrbot_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "talkrbot_msgs/msg/detail/task_command__struct.h"

/// Initialize msg/TaskCommand message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * talkrbot_msgs__msg__TaskCommand
 * )) before or use
 * talkrbot_msgs__msg__TaskCommand__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
bool
talkrbot_msgs__msg__TaskCommand__init(talkrbot_msgs__msg__TaskCommand * msg);

/// Finalize msg/TaskCommand message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
void
talkrbot_msgs__msg__TaskCommand__fini(talkrbot_msgs__msg__TaskCommand * msg);

/// Create msg/TaskCommand message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * talkrbot_msgs__msg__TaskCommand__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
talkrbot_msgs__msg__TaskCommand *
talkrbot_msgs__msg__TaskCommand__create();

/// Destroy msg/TaskCommand message.
/**
 * It calls
 * talkrbot_msgs__msg__TaskCommand__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
void
talkrbot_msgs__msg__TaskCommand__destroy(talkrbot_msgs__msg__TaskCommand * msg);

/// Check for msg/TaskCommand message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
bool
talkrbot_msgs__msg__TaskCommand__are_equal(const talkrbot_msgs__msg__TaskCommand * lhs, const talkrbot_msgs__msg__TaskCommand * rhs);

/// Copy a msg/TaskCommand message.
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
talkrbot_msgs__msg__TaskCommand__copy(
  const talkrbot_msgs__msg__TaskCommand * input,
  talkrbot_msgs__msg__TaskCommand * output);

/// Initialize array of msg/TaskCommand messages.
/**
 * It allocates the memory for the number of elements and calls
 * talkrbot_msgs__msg__TaskCommand__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
bool
talkrbot_msgs__msg__TaskCommand__Sequence__init(talkrbot_msgs__msg__TaskCommand__Sequence * array, size_t size);

/// Finalize array of msg/TaskCommand messages.
/**
 * It calls
 * talkrbot_msgs__msg__TaskCommand__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
void
talkrbot_msgs__msg__TaskCommand__Sequence__fini(talkrbot_msgs__msg__TaskCommand__Sequence * array);

/// Create array of msg/TaskCommand messages.
/**
 * It allocates the memory for the array and calls
 * talkrbot_msgs__msg__TaskCommand__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
talkrbot_msgs__msg__TaskCommand__Sequence *
talkrbot_msgs__msg__TaskCommand__Sequence__create(size_t size);

/// Destroy array of msg/TaskCommand messages.
/**
 * It calls
 * talkrbot_msgs__msg__TaskCommand__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
void
talkrbot_msgs__msg__TaskCommand__Sequence__destroy(talkrbot_msgs__msg__TaskCommand__Sequence * array);

/// Check for msg/TaskCommand message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_talkrbot_msgs
bool
talkrbot_msgs__msg__TaskCommand__Sequence__are_equal(const talkrbot_msgs__msg__TaskCommand__Sequence * lhs, const talkrbot_msgs__msg__TaskCommand__Sequence * rhs);

/// Copy an array of msg/TaskCommand messages.
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
talkrbot_msgs__msg__TaskCommand__Sequence__copy(
  const talkrbot_msgs__msg__TaskCommand__Sequence * input,
  talkrbot_msgs__msg__TaskCommand__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__FUNCTIONS_H_
