// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from talkrbot_msgs:msg/AACInput.idl
// generated code does not contain a copyright notice

#ifndef TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__STRUCT_HPP_
#define TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__STRUCT_HPP_

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
# define DEPRECATED__talkrbot_msgs__msg__AACInput __attribute__((deprecated))
#else
# define DEPRECATED__talkrbot_msgs__msg__AACInput __declspec(deprecated)
#endif

namespace talkrbot_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct AACInput_
{
  using Type = AACInput_<ContainerAllocator>;

  explicit AACInput_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : timestamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->text = "";
      this->user_id = "";
      this->input_method = "";
      this->confidence = 0.0f;
      this->metadata = "";
    }
  }

  explicit AACInput_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : text(_alloc),
    user_id(_alloc),
    timestamp(_alloc, _init),
    input_method(_alloc),
    metadata(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->text = "";
      this->user_id = "";
      this->input_method = "";
      this->confidence = 0.0f;
      this->metadata = "";
    }
  }

  // field types and members
  using _text_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _text_type text;
  using _user_id_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _user_id_type user_id;
  using _timestamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _timestamp_type timestamp;
  using _input_method_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _input_method_type input_method;
  using _confidence_type =
    float;
  _confidence_type confidence;
  using _metadata_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _metadata_type metadata;

  // setters for named parameter idiom
  Type & set__text(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->text = _arg;
    return *this;
  }
  Type & set__user_id(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->user_id = _arg;
    return *this;
  }
  Type & set__timestamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__input_method(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->input_method = _arg;
    return *this;
  }
  Type & set__confidence(
    const float & _arg)
  {
    this->confidence = _arg;
    return *this;
  }
  Type & set__metadata(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->metadata = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    talkrbot_msgs::msg::AACInput_<ContainerAllocator> *;
  using ConstRawPtr =
    const talkrbot_msgs::msg::AACInput_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<talkrbot_msgs::msg::AACInput_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<talkrbot_msgs::msg::AACInput_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      talkrbot_msgs::msg::AACInput_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<talkrbot_msgs::msg::AACInput_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      talkrbot_msgs::msg::AACInput_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<talkrbot_msgs::msg::AACInput_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<talkrbot_msgs::msg::AACInput_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<talkrbot_msgs::msg::AACInput_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__talkrbot_msgs__msg__AACInput
    std::shared_ptr<talkrbot_msgs::msg::AACInput_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__talkrbot_msgs__msg__AACInput
    std::shared_ptr<talkrbot_msgs::msg::AACInput_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AACInput_ & other) const
  {
    if (this->text != other.text) {
      return false;
    }
    if (this->user_id != other.user_id) {
      return false;
    }
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->input_method != other.input_method) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    if (this->metadata != other.metadata) {
      return false;
    }
    return true;
  }
  bool operator!=(const AACInput_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AACInput_

// alias to use template instance with default allocator
using AACInput =
  talkrbot_msgs::msg::AACInput_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace talkrbot_msgs

#endif  // TALKRBOT_MSGS__MSG__DETAIL__AAC_INPUT__STRUCT_HPP_
