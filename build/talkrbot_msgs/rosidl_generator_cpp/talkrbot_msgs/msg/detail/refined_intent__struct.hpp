// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from talkrbot_msgs:msg/RefinedIntent.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__REFINED_INTENT__STRUCT_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__REFINED_INTENT__STRUCT_HPP_

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
# define DEPRECATED__talkrbot_msgs__msg__RefinedIntent __attribute__((deprecated))
#else
# define DEPRECATED__talkrbot_msgs__msg__RefinedIntent __declspec(deprecated)
#endif

namespace talkrbot_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RefinedIntent_
{
  using Type = RefinedIntent_<ContainerAllocator>;

  explicit RefinedIntent_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : timestamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->intent = "";
      this->user_location = "";
      this->priority = "";
      this->original_text = "";
    }
  }

  explicit RefinedIntent_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : intent(_alloc),
    user_location(_alloc),
    priority(_alloc),
    original_text(_alloc),
    timestamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->intent = "";
      this->user_location = "";
      this->priority = "";
      this->original_text = "";
    }
  }

  // field types and members
  using _intent_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _intent_type intent;
  using _user_location_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _user_location_type user_location;
  using _priority_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _priority_type priority;
  using _original_text_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _original_text_type original_text;
  using _timestamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _timestamp_type timestamp;

  // setters for named parameter idiom
  Type & set__intent(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->intent = _arg;
    return *this;
  }
  Type & set__user_location(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->user_location = _arg;
    return *this;
  }
  Type & set__priority(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->priority = _arg;
    return *this;
  }
  Type & set__original_text(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->original_text = _arg;
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
    talkrbot_msgs::msg::RefinedIntent_<ContainerAllocator> *;
  using ConstRawPtr =
    const talkrbot_msgs::msg::RefinedIntent_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<talkrbot_msgs::msg::RefinedIntent_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<talkrbot_msgs::msg::RefinedIntent_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      talkrbot_msgs::msg::RefinedIntent_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<talkrbot_msgs::msg::RefinedIntent_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      talkrbot_msgs::msg::RefinedIntent_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<talkrbot_msgs::msg::RefinedIntent_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<talkrbot_msgs::msg::RefinedIntent_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<talkrbot_msgs::msg::RefinedIntent_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__talkrbot_msgs__msg__RefinedIntent
    std::shared_ptr<talkrbot_msgs::msg::RefinedIntent_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__talkrbot_msgs__msg__RefinedIntent
    std::shared_ptr<talkrbot_msgs::msg::RefinedIntent_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RefinedIntent_ & other) const
  {
    if (this->intent != other.intent) {
      return false;
    }
    if (this->user_location != other.user_location) {
      return false;
    }
    if (this->priority != other.priority) {
      return false;
    }
    if (this->original_text != other.original_text) {
      return false;
    }
    if (this->timestamp != other.timestamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const RefinedIntent_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RefinedIntent_

// alias to use template instance with default allocator
using RefinedIntent =
  talkrbot_msgs::msg::RefinedIntent_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace talkrbot_msgs

#endif  // TALKRBOT_MSGS__MSG__DETAIL__REFINED_INTENT__STRUCT_HPP_
