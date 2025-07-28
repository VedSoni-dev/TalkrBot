// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from talkrbot_msgs:msg/DetectedObject.idl
// generated code does not contain a copyright notice
#include "talkrbot_msgs/msg/detail/detected_object__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `class_name`
// Member `properties`
// Member `object_id`
#include "rosidl_runtime_c/string_functions.h"
// Member `pose`
#include "geometry_msgs/msg/detail/pose_stamped__functions.h"
// Member `timestamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
talkrbot_msgs__msg__DetectedObject__init(talkrbot_msgs__msg__DetectedObject * msg)
{
  if (!msg) {
    return false;
  }
  // class_name
  if (!rosidl_runtime_c__String__init(&msg->class_name)) {
    talkrbot_msgs__msg__DetectedObject__fini(msg);
    return false;
  }
  // confidence
  // bbox_x
  // bbox_y
  // bbox_width
  // bbox_height
  // pose
  if (!geometry_msgs__msg__PoseStamped__init(&msg->pose)) {
    talkrbot_msgs__msg__DetectedObject__fini(msg);
    return false;
  }
  // properties
  if (!rosidl_runtime_c__String__init(&msg->properties)) {
    talkrbot_msgs__msg__DetectedObject__fini(msg);
    return false;
  }
  // object_id
  if (!rosidl_runtime_c__String__init(&msg->object_id)) {
    talkrbot_msgs__msg__DetectedObject__fini(msg);
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__init(&msg->timestamp)) {
    talkrbot_msgs__msg__DetectedObject__fini(msg);
    return false;
  }
  return true;
}

void
talkrbot_msgs__msg__DetectedObject__fini(talkrbot_msgs__msg__DetectedObject * msg)
{
  if (!msg) {
    return;
  }
  // class_name
  rosidl_runtime_c__String__fini(&msg->class_name);
  // confidence
  // bbox_x
  // bbox_y
  // bbox_width
  // bbox_height
  // pose
  geometry_msgs__msg__PoseStamped__fini(&msg->pose);
  // properties
  rosidl_runtime_c__String__fini(&msg->properties);
  // object_id
  rosidl_runtime_c__String__fini(&msg->object_id);
  // timestamp
  builtin_interfaces__msg__Time__fini(&msg->timestamp);
}

bool
talkrbot_msgs__msg__DetectedObject__are_equal(const talkrbot_msgs__msg__DetectedObject * lhs, const talkrbot_msgs__msg__DetectedObject * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // class_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->class_name), &(rhs->class_name)))
  {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
    return false;
  }
  // bbox_x
  if (lhs->bbox_x != rhs->bbox_x) {
    return false;
  }
  // bbox_y
  if (lhs->bbox_y != rhs->bbox_y) {
    return false;
  }
  // bbox_width
  if (lhs->bbox_width != rhs->bbox_width) {
    return false;
  }
  // bbox_height
  if (lhs->bbox_height != rhs->bbox_height) {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__PoseStamped__are_equal(
      &(lhs->pose), &(rhs->pose)))
  {
    return false;
  }
  // properties
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->properties), &(rhs->properties)))
  {
    return false;
  }
  // object_id
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->object_id), &(rhs->object_id)))
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
talkrbot_msgs__msg__DetectedObject__copy(
  const talkrbot_msgs__msg__DetectedObject * input,
  talkrbot_msgs__msg__DetectedObject * output)
{
  if (!input || !output) {
    return false;
  }
  // class_name
  if (!rosidl_runtime_c__String__copy(
      &(input->class_name), &(output->class_name)))
  {
    return false;
  }
  // confidence
  output->confidence = input->confidence;
  // bbox_x
  output->bbox_x = input->bbox_x;
  // bbox_y
  output->bbox_y = input->bbox_y;
  // bbox_width
  output->bbox_width = input->bbox_width;
  // bbox_height
  output->bbox_height = input->bbox_height;
  // pose
  if (!geometry_msgs__msg__PoseStamped__copy(
      &(input->pose), &(output->pose)))
  {
    return false;
  }
  // properties
  if (!rosidl_runtime_c__String__copy(
      &(input->properties), &(output->properties)))
  {
    return false;
  }
  // object_id
  if (!rosidl_runtime_c__String__copy(
      &(input->object_id), &(output->object_id)))
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

talkrbot_msgs__msg__DetectedObject *
talkrbot_msgs__msg__DetectedObject__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  talkrbot_msgs__msg__DetectedObject * msg = (talkrbot_msgs__msg__DetectedObject *)allocator.allocate(sizeof(talkrbot_msgs__msg__DetectedObject), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(talkrbot_msgs__msg__DetectedObject));
  bool success = talkrbot_msgs__msg__DetectedObject__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
talkrbot_msgs__msg__DetectedObject__destroy(talkrbot_msgs__msg__DetectedObject * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    talkrbot_msgs__msg__DetectedObject__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
talkrbot_msgs__msg__DetectedObject__Sequence__init(talkrbot_msgs__msg__DetectedObject__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  talkrbot_msgs__msg__DetectedObject * data = NULL;

  if (size) {
    data = (talkrbot_msgs__msg__DetectedObject *)allocator.zero_allocate(size, sizeof(talkrbot_msgs__msg__DetectedObject), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = talkrbot_msgs__msg__DetectedObject__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        talkrbot_msgs__msg__DetectedObject__fini(&data[i - 1]);
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
talkrbot_msgs__msg__DetectedObject__Sequence__fini(talkrbot_msgs__msg__DetectedObject__Sequence * array)
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
      talkrbot_msgs__msg__DetectedObject__fini(&array->data[i]);
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

talkrbot_msgs__msg__DetectedObject__Sequence *
talkrbot_msgs__msg__DetectedObject__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  talkrbot_msgs__msg__DetectedObject__Sequence * array = (talkrbot_msgs__msg__DetectedObject__Sequence *)allocator.allocate(sizeof(talkrbot_msgs__msg__DetectedObject__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = talkrbot_msgs__msg__DetectedObject__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
talkrbot_msgs__msg__DetectedObject__Sequence__destroy(talkrbot_msgs__msg__DetectedObject__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    talkrbot_msgs__msg__DetectedObject__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
talkrbot_msgs__msg__DetectedObject__Sequence__are_equal(const talkrbot_msgs__msg__DetectedObject__Sequence * lhs, const talkrbot_msgs__msg__DetectedObject__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!talkrbot_msgs__msg__DetectedObject__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
talkrbot_msgs__msg__DetectedObject__Sequence__copy(
  const talkrbot_msgs__msg__DetectedObject__Sequence * input,
  talkrbot_msgs__msg__DetectedObject__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(talkrbot_msgs__msg__DetectedObject);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    talkrbot_msgs__msg__DetectedObject * data =
      (talkrbot_msgs__msg__DetectedObject *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!talkrbot_msgs__msg__DetectedObject__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          talkrbot_msgs__msg__DetectedObject__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!talkrbot_msgs__msg__DetectedObject__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
