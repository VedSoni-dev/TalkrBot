// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from talkrbot_msgs:msg/ExecutionFeedback.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__EXECUTION_FEEDBACK__STRUCT_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__EXECUTION_FEEDBACK__STRUCT_HPP_

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
# define DEPRECATED__talkrbot_msgs__msg__ExecutionFeedback __attribute__((deprecated))
#else
# define DEPRECATED__talkrbot_msgs__msg__ExecutionFeedback __declspec(deprecated)
#endif

namespace talkrbot_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ExecutionFeedback_
{
  using Type = ExecutionFeedback_<ContainerAllocator>;

  explicit ExecutionFeedback_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : timestamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->step = "";
      this->status = "";
      this->notes = "";
    }
  }

  explicit ExecutionFeedback_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : step(_alloc),
    status(_alloc),
    notes(_alloc),
    timestamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->step = "";
      this->status = "";
      this->notes = "";
    }
  }

  // field types and members
  using _step_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _step_type step;
  using _status_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _status_type status;
  using _notes_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _notes_type notes;
  using _timestamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _timestamp_type timestamp;

  // setters for named parameter idiom
  Type & set__step(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->step = _arg;
    return *this;
  }
  Type & set__status(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__notes(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->notes = _arg;
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
    talkrbot_msgs::msg::ExecutionFeedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const talkrbot_msgs::msg::ExecutionFeedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<talkrbot_msgs::msg::ExecutionFeedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<talkrbot_msgs::msg::ExecutionFeedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      talkrbot_msgs::msg::ExecutionFeedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<talkrbot_msgs::msg::ExecutionFeedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      talkrbot_msgs::msg::ExecutionFeedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<talkrbot_msgs::msg::ExecutionFeedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<talkrbot_msgs::msg::ExecutionFeedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<talkrbot_msgs::msg::ExecutionFeedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__talkrbot_msgs__msg__ExecutionFeedback
    std::shared_ptr<talkrbot_msgs::msg::ExecutionFeedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__talkrbot_msgs__msg__ExecutionFeedback
    std::shared_ptr<talkrbot_msgs::msg::ExecutionFeedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ExecutionFeedback_ & other) const
  {
    if (this->step != other.step) {
      return false;
    }
    if (this->status != other.status) {
      return false;
    }
    if (this->notes != other.notes) {
      return false;
    }
    if (this->timestamp != other.timestamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const ExecutionFeedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ExecutionFeedback_

// alias to use template instance with default allocator
using ExecutionFeedback =
  talkrbot_msgs::msg::ExecutionFeedback_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace talkrbot_msgs

#endif  // TALKRBOT_MSGS__MSG__DETAIL__EXECUTION_FEEDBACK__STRUCT_HPP_
