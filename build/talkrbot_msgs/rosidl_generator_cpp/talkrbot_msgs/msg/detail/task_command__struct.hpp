// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from talkrbot_msgs:msg/TaskCommand.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__STRUCT_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__talkrbot_msgs__msg__TaskCommand __attribute__((deprecated))
#else
# define DEPRECATED__talkrbot_msgs__msg__TaskCommand __declspec(deprecated)
#endif

namespace talkrbot_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TaskCommand_
{
  using Type = TaskCommand_<ContainerAllocator>;

  explicit TaskCommand_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : timestamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->task = "";
      this->object = "";
      this->location = "";
      this->parameters = "";
      this->confidence = 0.0f;
      this->command_id = "";
    }
  }

  explicit TaskCommand_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : task(_alloc),
    object(_alloc),
    location(_alloc),
    parameters(_alloc),
    command_id(_alloc),
    timestamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->task = "";
      this->object = "";
      this->location = "";
      this->parameters = "";
      this->confidence = 0.0f;
      this->command_id = "";
    }
  }

  // field types and members
  using _task_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _task_type task;
  using _object_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _object_type object;
  using _location_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _location_type location;
  using _parameters_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _parameters_type parameters;
  using _confidence_type =
    float;
  _confidence_type confidence;
  using _command_id_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _command_id_type command_id;
  using _timestamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _timestamp_type timestamp;

  // setters for named parameter idiom
  Type & set__task(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->task = _arg;
    return *this;
  }
  Type & set__object(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->object = _arg;
    return *this;
  }
  Type & set__location(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->location = _arg;
    return *this;
  }
  Type & set__parameters(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->parameters = _arg;
    return *this;
  }
  Type & set__confidence(
    const float & _arg)
  {
    this->confidence = _arg;
    return *this;
  }
  Type & set__command_id(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->command_id = _arg;
    return *this;
  }
  Type & set__timestamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    talkrbot_msgs::msg::TaskCommand_<ContainerAllocator> *;
  using ConstRawPtr =
    const talkrbot_msgs::msg::TaskCommand_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<talkrbot_msgs::msg::TaskCommand_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<talkrbot_msgs::msg::TaskCommand_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      talkrbot_msgs::msg::TaskCommand_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<talkrbot_msgs::msg::TaskCommand_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      talkrbot_msgs::msg::TaskCommand_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<talkrbot_msgs::msg::TaskCommand_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<talkrbot_msgs::msg::TaskCommand_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<talkrbot_msgs::msg::TaskCommand_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__talkrbot_msgs__msg__TaskCommand
    std::shared_ptr<talkrbot_msgs::msg::TaskCommand_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__talkrbot_msgs__msg__TaskCommand
    std::shared_ptr<talkrbot_msgs::msg::TaskCommand_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskCommand_ & other) const
  {
    if (this->task != other.task) {
      return false;
    }
    if (this->object != other.object) {
      return false;
    }
    if (this->location != other.location) {
      return false;
    }
    if (this->parameters != other.parameters) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    if (this->command_id != other.command_id) {
      return false;
    }
    if (this->timestamp != other.timestamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskCommand_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskCommand_

// alias to use template instance with default allocator
using TaskCommand =
  talkrbot_msgs::msg::TaskCommand_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace talkrbot_msgs

#endif  // TALKRBOT_MSGS__MSG__DETAIL__TASK_COMMAND__STRUCT_HPP_
