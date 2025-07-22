// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from talkrbot_msgs:msg/TaskCommand.idl
// generated code does not contain a copyright notice
#include "talkrbot_msgs/msg/detail/task_command__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `task`
// Member `object`
// Member `location`
// Member `parameters`
// Member `command_id`
#include "rosidl_runtime_c/string_functions.h"
// Member `timestamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
talkrbot_msgs__msg__TaskCommand__init(talkrbot_msgs__msg__TaskCommand * msg)
{
  if (!msg) {
    return false;
  }
  // task
  if (!rosidl_runtime_c__String__init(&msg->task)) {
    talkrbot_msgs__msg__TaskCommand__fini(msg);
    return false;
  }
  // object
  if (!rosidl_runtime_c__String__init(&msg->object)) {
    talkrbot_msgs__msg__TaskCommand__fini(msg);
    return false;
  }
  // location
  if (!rosidl_runtime_c__String__init(&msg->location)) {
    talkrbot_msgs__msg__TaskCommand__fini(msg);
    return false;
  }
  // parameters
  if (!rosidl_runtime_c__String__init(&msg->parameters)) {
    talkrbot_msgs__msg__TaskCommand__fini(msg);
    return false;
  }
  // confidence
  // command_id
  if (!rosidl_runtime_c__String__init(&msg->command_id)) {
    talkrbot_msgs__msg__TaskCommand__fini(msg);
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__init(&msg->timestamp)) {
    talkrbot_msgs__msg__TaskCommand__fini(msg);
    return false;
  }
  return true;
}

void
talkrbot_msgs__msg__TaskCommand__fini(talkrbot_msgs__msg__TaskCommand * msg)
{
  if (!msg) {
    return;
  }
  // task
  rosidl_runtime_c__String__fini(&msg->task);
  // object
  rosidl_runtime_c__String__fini(&msg->object);
  // location
  rosidl_runtime_c__String__fini(&msg->location);
  // parameters
  rosidl_runtime_c__String__fini(&msg->parameters);
  // confidence
  // command_id
  rosidl_runtime_c__String__fini(&msg->command_id);
  // timestamp
  builtin_interfaces__msg__Time__fini(&msg->timestamp);
}

bool
talkrbot_msgs__msg__TaskCommand__are_equal(const talkrbot_msgs__msg__TaskCommand * lhs, const talkrbot_msgs__msg__TaskCommand * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // task
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->task), &(rhs->task)))
  {
    return false;
  }
  // object
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->object), &(rhs->object)))
  {
    return false;
  }
  // location
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->location), &(rhs->location)))
  {
    return false;
  }
  // parameters
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->parameters), &(rhs->parameters)))
  {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
    return false;
  }
  // command_id
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->command_id), &(rhs->command_id)))
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
talkrbot_msgs__msg__TaskCommand__copy(
  const talkrbot_msgs__msg__TaskCommand * input,
  talkrbot_msgs__msg__TaskCommand * output)
{
  if (!input || !output) {
    return false;
  }
  // task
  if (!rosidl_runtime_c__String__copy(
      &(input->task), &(output->task)))
  {
    return false;
  }
  // object
  if (!rosidl_runtime_c__String__copy(
      &(input->object), &(output->object)))
  {
    return false;
  }
  // location
  if (!rosidl_runtime_c__String__copy(
      &(input->location), &(output->location)))
  {
    return false;
  }
  // parameters
  if (!rosidl_runtime_c__String__copy(
      &(input->parameters), &(output->parameters)))
  {
    return false;
  }
  // confidence
  output->confidence = input->confidence;
  // command_id
  if (!rosidl_runtime_c__String__copy(
      &(input->command_id), &(output->command_id)))
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

talkrbot_msgs__msg__TaskCommand *
talkrbot_msgs__msg__TaskCommand__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  talkrbot_msgs__msg__TaskCommand * msg = (talkrbot_msgs__msg__TaskCommand *)allocator.allocate(sizeof(talkrbot_msgs__msg__TaskCommand), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(talkrbot_msgs__msg__TaskCommand));
  bool success = talkrbot_msgs__msg__TaskCommand__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
talkrbot_msgs__msg__TaskCommand__destroy(talkrbot_msgs__msg__TaskCommand * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    talkrbot_msgs__msg__TaskCommand__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
talkrbot_msgs__msg__TaskCommand__Sequence__init(talkrbot_msgs__msg__TaskCommand__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  talkrbot_msgs__msg__TaskCommand * data = NULL;

  if (size) {
    data = (talkrbot_msgs__msg__TaskCommand *)allocator.zero_allocate(size, sizeof(talkrbot_msgs__msg__TaskCommand), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = talkrbot_msgs__msg__TaskCommand__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        talkrbot_msgs__msg__TaskCommand__fini(&data[i - 1]);
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
talkrbot_msgs__msg__TaskCommand__Sequence__fini(talkrbot_msgs__msg__TaskCommand__Sequence * array)
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
      talkrbot_msgs__msg__TaskCommand__fini(&array->data[i]);
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

talkrbot_msgs__msg__TaskCommand__Sequence *
talkrbot_msgs__msg__TaskCommand__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  talkrbot_msgs__msg__TaskCommand__Sequence * array = (talkrbot_msgs__msg__TaskCommand__Sequence *)allocator.allocate(sizeof(talkrbot_msgs__msg__TaskCommand__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = talkrbot_msgs__msg__TaskCommand__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
talkrbot_msgs__msg__TaskCommand__Sequence__destroy(talkrbot_msgs__msg__TaskCommand__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    talkrbot_msgs__msg__TaskCommand__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
talkrbot_msgs__msg__TaskCommand__Sequence__are_equal(const talkrbot_msgs__msg__TaskCommand__Sequence * lhs, const talkrbot_msgs__msg__TaskCommand__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!talkrbot_msgs__msg__TaskCommand__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
talkrbot_msgs__msg__TaskCommand__Sequence__copy(
  const talkrbot_msgs__msg__TaskCommand__Sequence * input,
  talkrbot_msgs__msg__TaskCommand__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(talkrbot_msgs__msg__TaskCommand);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    talkrbot_msgs__msg__TaskCommand * data =
      (talkrbot_msgs__msg__TaskCommand *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!talkrbot_msgs__msg__TaskCommand__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          talkrbot_msgs__msg__TaskCommand__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!talkrbot_msgs__msg__TaskCommand__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
