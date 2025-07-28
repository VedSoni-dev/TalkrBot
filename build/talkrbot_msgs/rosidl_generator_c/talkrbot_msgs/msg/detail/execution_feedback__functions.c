// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from talkrbot_msgs:msg/ExecutionFeedback.idl
// generated code does not contain a copyright notice
#include "talkrbot_msgs/msg/detail/execution_feedback__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `step`
// Member `status`
// Member `notes`
#include "rosidl_runtime_c/string_functions.h"
// Member `timestamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
talkrbot_msgs__msg__ExecutionFeedback__init(talkrbot_msgs__msg__ExecutionFeedback * msg)
{
  if (!msg) {
    return false;
  }
  // step
  if (!rosidl_runtime_c__String__init(&msg->step)) {
    talkrbot_msgs__msg__ExecutionFeedback__fini(msg);
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__init(&msg->status)) {
    talkrbot_msgs__msg__ExecutionFeedback__fini(msg);
    return false;
  }
  // notes
  if (!rosidl_runtime_c__String__init(&msg->notes)) {
    talkrbot_msgs__msg__ExecutionFeedback__fini(msg);
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__init(&msg->timestamp)) {
    talkrbot_msgs__msg__ExecutionFeedback__fini(msg);
    return false;
  }
  return true;
}

void
talkrbot_msgs__msg__ExecutionFeedback__fini(talkrbot_msgs__msg__ExecutionFeedback * msg)
{
  if (!msg) {
    return;
  }
  // step
  rosidl_runtime_c__String__fini(&msg->step);
  // status
  rosidl_runtime_c__String__fini(&msg->status);
  // notes
  rosidl_runtime_c__String__fini(&msg->notes);
  // timestamp
  builtin_interfaces__msg__Time__fini(&msg->timestamp);
}

bool
talkrbot_msgs__msg__ExecutionFeedback__are_equal(const talkrbot_msgs__msg__ExecutionFeedback * lhs, const talkrbot_msgs__msg__ExecutionFeedback * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // step
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->step), &(rhs->step)))
  {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->status), &(rhs->status)))
  {
    return false;
  }
  // notes
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->notes), &(rhs->notes)))
  {
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->timestamp), &(rhs->timestamp)))
  {
    return false;
  }
  return true;
}

bool
talkrbot_msgs__msg__ExecutionFeedback__copy(
  const talkrbot_msgs__msg__ExecutionFeedback * input,
  talkrbot_msgs__msg__ExecutionFeedback * output)
{
  if (!input || !output) {
    return false;
  }
  // step
  if (!rosidl_runtime_c__String__copy(
      &(input->step), &(output->step)))
  {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__copy(
      &(input->status), &(output->status)))
  {
    return false;
  }
  // notes
  if (!rosidl_runtime_c__String__copy(
      &(input->notes), &(output->notes)))
  {
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->timestamp), &(output->timestamp)))
  {
    return false;
  }
  return true;
}

talkrbot_msgs__msg__ExecutionFeedback *
talkrbot_msgs__msg__ExecutionFeedback__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  talkrbot_msgs__msg__ExecutionFeedback * msg = (talkrbot_msgs__msg__ExecutionFeedback *)allocator.allocate(sizeof(talkrbot_msgs__msg__ExecutionFeedback), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(talkrbot_msgs__msg__ExecutionFeedback));
  bool success = talkrbot_msgs__msg__ExecutionFeedback__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
talkrbot_msgs__msg__ExecutionFeedback__destroy(talkrbot_msgs__msg__ExecutionFeedback * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    talkrbot_msgs__msg__ExecutionFeedback__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
talkrbot_msgs__msg__ExecutionFeedback__Sequence__init(talkrbot_msgs__msg__ExecutionFeedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  talkrbot_msgs__msg__ExecutionFeedback * data = NULL;

  if (size) {
    data = (talkrbot_msgs__msg__ExecutionFeedback *)allocator.zero_allocate(size, sizeof(talkrbot_msgs__msg__ExecutionFeedback), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = talkrbot_msgs__msg__ExecutionFeedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        talkrbot_msgs__msg__ExecutionFeedback__fini(&data[i - 1]);
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
talkrbot_msgs__msg__ExecutionFeedback__Sequence__fini(talkrbot_msgs__msg__ExecutionFeedback__Sequence * array)
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
      talkrbot_msgs__msg__ExecutionFeedback__fini(&array->data[i]);
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

talkrbot_msgs__msg__ExecutionFeedback__Sequence *
talkrbot_msgs__msg__ExecutionFeedback__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  talkrbot_msgs__msg__ExecutionFeedback__Sequence * array = (talkrbot_msgs__msg__ExecutionFeedback__Sequence *)allocator.allocate(sizeof(talkrbot_msgs__msg__ExecutionFeedback__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = talkrbot_msgs__msg__ExecutionFeedback__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
talkrbot_msgs__msg__ExecutionFeedback__Sequence__destroy(talkrbot_msgs__msg__ExecutionFeedback__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    talkrbot_msgs__msg__ExecutionFeedback__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
talkrbot_msgs__msg__ExecutionFeedback__Sequence__are_equal(const talkrbot_msgs__msg__ExecutionFeedback__Sequence * lhs, const talkrbot_msgs__msg__ExecutionFeedback__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!talkrbot_msgs__msg__ExecutionFeedback__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
talkrbot_msgs__msg__ExecutionFeedback__Sequence__copy(
  const talkrbot_msgs__msg__ExecutionFeedback__Sequence * input,
  talkrbot_msgs__msg__ExecutionFeedback__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(talkrbot_msgs__msg__ExecutionFeedback);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    talkrbot_msgs__msg__ExecutionFeedback * data =
      (talkrbot_msgs__msg__ExecutionFeedback *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!talkrbot_msgs__msg__ExecutionFeedback__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          talkrbot_msgs__msg__ExecutionFeedback__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!talkrbot_msgs__msg__ExecutionFeedback__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
