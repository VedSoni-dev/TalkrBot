# generated from rosidl_generator_py/resource/_idl.py.em
# with input from talkrbot_msgs:msg/AACInput.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AACInput(type):
    """Metaclass of message 'AACInput'."""

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
                'talkrbot_msgs.msg.AACInput')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__aac_input
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__aac_input
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__aac_input
            cls._TYPE_SUPPORT = module.type_support_msg__msg__aac_input
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__aac_input

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


class AACInput(metaclass=Metaclass_AACInput):
    """Message class 'AACInput'."""

    __slots__ = [
        '_text',
        '_user_id',
        '_timestamp',
        '_input_method',
        '_confidence',
        '_metadata',
    ]

    _fields_and_field_types = {
        'text': 'string',
        'user_id': 'string',
        'timestamp': 'builtin_interfaces/Time',
        'input_method': 'string',
        'confidence': 'float',
        'metadata': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.text = kwargs.get('text', str())
        self.user_id = kwargs.get('user_id', str())
        from builtin_interfaces.msg import Time
        self.timestamp = kwargs.get('timestamp', Time())
        self.input_method = kwargs.get('input_method', str())
        self.confidence = kwargs.get('confidence', float())
        self.metadata = kwargs.get('metadata', str())

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
        if self.text != other.text:
            return False
        if self.user_id != other.user_id:
            return False
        if self.timestamp != other.timestamp:
            return False
        if self.input_method != other.input_method:
            return False
        if self.confidence != other.confidence:
            return False
        if self.metadata != other.metadata:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def text(self):
        """Message field 'text'."""
        return self._text

    @text.setter
    def text(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'text' field must be of type 'str'"
        self._text = value

    @builtins.property
    def user_id(self):
        """Message field 'user_id'."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'user_id' field must be of type 'str'"
        self._user_id = value

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

    @builtins.property
    def input_method(self):
        """Message field 'input_method'."""
        return self._input_method

    @input_method.setter
    def input_method(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'input_method' field must be of type 'str'"
        self._input_method = value

    @builtins.property
    def confidence(self):
        """Message field 'confidence'."""
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'confidence' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'confidence' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._confidence = value

    @builtins.property
    def metadata(self):
        """Message field 'metadata'."""
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'metadata' field must be of type 'str'"
        self._metadata = value
