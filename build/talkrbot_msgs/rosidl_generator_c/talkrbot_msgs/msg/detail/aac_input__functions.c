// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from talkrbot_msgs:msg/AACInput.idl
// generated code does not contain a copyright notice
#include "talkrbot_msgs/msg/detail/aac_input__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `text`
// Member `user_id`
// Member `input_method`
// Member `metadata`
#include "rosidl_runtime_c/string_functions.h"
// Member `timestamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
talkrbot_msgs__msg__AACInput__init(talkrbot_msgs__msg__AACInput * msg)
{
  if (!msg) {
    return false;
  }
  // text
  if (!rosidl_runtime_c__String__init(&msg->text)) {
    talkrbot_msgs__msg__AACInput__fini(msg);
    return false;
  }
  // user_id
  if (!rosidl_runtime_c__String__init(&msg->user_id)) {
    talkrbot_msgs__msg__AACInput__fini(msg);
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__init(&msg->timestamp)) {
    talkrbot_msgs__msg__AACInput__fini(msg);
    return false;
  }
  // input_method
  if (!rosidl_runtime_c__String__init(&msg->input_method)) {
    talkrbot_msgs__msg__AACInput__fini(msg);
    return false;
  }
  // confidence
  // metadata
  if (!rosidl_runtime_c__String__init(&msg->metadata)) {
    talkrbot_msgs__msg__AACInput__fini(msg);
    return false;
  }
  return true;
}

void
talkrbot_msgs__msg__AACInput__fini(talkrbot_msgs__msg__AACInput * msg)
{
  if (!msg) {
    return;
  }
  // text
  rosidl_runtime_c__String__fini(&msg->text);
  // user_id
  rosidl_runtime_c__String__fini(&msg->user_id);
  // timestamp
  builtin_interfaces__msg__Time__fini(&msg->timestamp);
  // input_method
  rosidl_runtime_c__String__fini(&msg->input_method);
  // confidence
  // metadata
  rosidl_runtime_c__String__fini(&msg->metadata);
}

bool
talkrbot_msgs__msg__AACInput__are_equal(const talkrbot_msgs__msg__AACInput * lhs, const talkrbot_msgs__msg__AACInput * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // text
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->text), &(rhs->text)))
  {
    return false;
  }
  // user_id
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->user_id), &(rhs->user_id)))
  {
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->timestamp), &(rhs->timestamp)))
  {
    return false;
  }
  // input_method
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->input_method), &(rhs->input_method)))
  {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
    return false;
  }
  // metadata
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->metadata), &(rhs->metadata)))
  {
    return false;
  }
  return true;
}

bool
talkrbot_msgs__msg__AACInput__copy(
  const talkrbot_msgs__msg__AACInput * input,
  talkrbot_msgs__msg__AACInput * output)
{
  if (!input || !output) {
    return false;
  }
  // text
  if (!rosidl_runtime_c__String__copy(
      &(input->text), &(output->text)))
  {
    return false;
  }
  // user_id
  if (!rosidl_runtime_c__String__copy(
      &(input->user_id), &(output->user_id)))
  {
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->timestamp), &(output->timestamp)))
  {
    return false;
  }
  // input_method
  if (!rosidl_runtime_c__String__copy(
      &(input->input_method), &(output->input_method)))
  {
    return false;
  }
  // confidence
  output->confidence = input->confidence;
  // metadata
  if (!rosidl_runtime_c__String__copy(
      &(input->metadata), &(output->metadata)))
  {
    return false;
  }
  return true;
}

talkrbot_msgs__msg__AACInput *
talkrbot_msgs__msg__AACInput__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  talkrbot_msgs__msg__AACInput * msg = (talkrbot_msgs__msg__AACInput *)allocator.allocate(sizeof(talkrbot_msgs__msg__AACInput), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(talkrbot_msgs__msg__AACInput));
  bool success = talkrbot_msgs__msg__AACInput__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
talkrbot_msgs__msg__AACInput__destroy(talkrbot_msgs__msg__AACInput * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    talkrbot_msgs__msg__AACInput__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
talkrbot_msgs__msg__AACInput__Sequence__init(talkrbot_msgs__msg__AACInput__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  talkrbot_msgs__msg__AACInput * data = NULL;

  if (size) {
    data = (talkrbot_msgs__msg__AACInput *)allocator.zero_allocate(size, sizeof(talkrbot_msgs__msg__AACInput), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = talkrbot_msgs__msg__AACInput__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        talkrbot_msgs__msg__AACInput__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
talkrbot_msgs__msg__AACInput__Sequence__fini(talkrbot_msgs__msg__AACInput__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      talkrbot_msgs__msg__AACInput__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

talkrbot_msgs__msg__AACInput__Sequence *
talkrbot_msgs__msg__AACInput__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  talkrbot_msgs__msg__AACInput__Sequence * array = (talkrbot_msgs__msg__AACInput__Sequence *)allocator.allocate(sizeof(talkrbot_msgs__msg__AACInput__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = talkrbot_msgs__msg__AACInput__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
talkrbot_msgs__msg__AACInput__Sequence__destroy(talkrbot_msgs__msg__AACInput__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    talkrbot_msgs__msg__AACInput__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
talkrbot_msgs__msg__AACInput__Sequence__are_equal(const talkrbot_msgs__msg__AACInput__Sequence * lhs, const talkrbot_msgs__msg__AACInput__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!talkrbot_msgs__msg__AACInput__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
talkrbot_msgs__msg__AACInput__Sequence__copy(
  const talkrbot_msgs__msg__AACInput__Sequence * input,
  talkrbot_msgs__msg__AACInput__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(talkrbot_msgs__msg__AACInput);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    talkrbot_msgs__msg__AACInput * data =
      (talkrbot_msgs__msg__AACInput *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!talkrbot_msgs__msg__AACInput__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          talkrbot_msgs__msg__AACInput__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!talkrbot_msgs__msg__AACInput__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
