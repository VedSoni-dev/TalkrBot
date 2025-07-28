# generated from rosidl_generator_py/resource/_idl.py.em
# with input from talkrbot_msgs:msg/RefinedIntent.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RefinedIntent(type):
    """Metaclass of message 'RefinedIntent'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('talkrbot_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'talkrbot_msgs.msg.RefinedIntent')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__refined_intent
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__refined_intent
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__refined_intent
            cls._TYPE_SUPPORT = module.type_support_msg__msg__refined_intent
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__refined_intent

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RefinedIntent(metaclass=Metaclass_RefinedIntent):
    """Message class 'RefinedIntent'."""

    __slots__ = [
        '_intent',
        '_user_location',
        '_priority',
        '_original_text',
        '_timestamp',
    ]

    _fields_and_field_types = {
        'intent': 'string',
        'user_location': 'string',
        'priority': 'string',
        'original_text': 'string',
        'timestamp': 'builtin_interfaces/Time',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.intent = kwargs.get('intent', str())
        self.user_location = kwargs.get('user_location', str())
        self.priority = kwargs.get('priority', str())
        self.original_text = kwargs.get('original_text', str())
        from builtin_interfaces.msg import Time
        self.timestamp = kwargs.get('timestamp', Time())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.intent != other.intent:
            return False
        if self.user_location != other.user_location:
            return False
        if self.priority != other.priority:
            return False
        if self.original_text != other.original_text:
            return False
        if self.timestamp != other.timestamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def intent(self):
        """Message field 'intent'."""
        return self._intent

    @intent.setter
    def intent(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'intent' field must be of type 'str'"
        self._intent = value

    @builtins.property
    def user_location(self):
        """Message field 'user_location'."""
        return self._user_location

    @user_location.setter
    def user_location(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'user_location' field must be of type 'str'"
        self._user_location = value

    @builtins.property
    def priority(self):
        """Message field 'priority'."""
        return self._priority

    @priority.setter
    def priority(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'priority' field must be of type 'str'"
        self._priority = value

    @builtins.property
    def original_text(self):
        """Message field 'original_text'."""
        return self._original_text

    @original_text.setter
    def original_text(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'original_text' field must be of type 'str'"
        self._original_text = value

    @builtins.property
    def timestamp(self):
        """Message field 'timestamp'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'timestamp' field must be a sub message of type 'Time'"
        self._timestamp = value
