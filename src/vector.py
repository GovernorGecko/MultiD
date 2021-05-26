"""
Vector

Can dynamic methods be properties?
Can we have dynamic args like x=0.0 for offset/scale?
    Could be dynamic method

"""


class Descriptor(object):
    """
    """

    def __init__(self):
        self.label = None

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.label, None)

    def __set__(self, instance, value):
        instance.__dict__[self.label] = value


class DescriptorOwner(type):
    """
    Find all descriptors, auto-set their labels
    """

    def __new__(cls, name, bases, attrs):
        for n, v in attrs.items():
            if isinstance(v, Descriptor):
                v.label = n
        return super(DescriptorOwner, cls).__new__(cls, name, bases, attrs)


class Vector():
    """
    Parameters:
        (float, ...) or [float, ...] or float, float
    """

    __metaclass__ = DescriptorOwner
    __slots__ = ["__dict__", "__values"]

    def __init__(self, *args, values=[]):

        # Requires a Dict for Values
        if (
            not isinstance(values, list) or
            len(values) == 0 or
            not all(
                isinstance(k, str) for k in values
            )
        ):
            raise ValueError("Values must be a list of length > 0.")
        self.__values = {key: 0.0 for key in values}

        # Error/Type Checking
        if (
            len(args) > 0 and
            isinstance(args[0], (list, tuple))
        ):
            self.set([v for v in args[0]])
        elif len(args) == len(self.__values):
            self.set([*args])
        else:
            self.set(None)  # [0.0 for _ in self.__value_length])

        # Dynamic variable creation!
        for v in self.__values.keys():
            setattr(self, v.upper(), Descriptor())
            setattr(self, v.upper(), self.__values[v])

            """
            def value_method(self):
                print(v)
                return self.__values[v]
            value_method.__doc__ = "Nothing yet"
            value_method.__name__ = v.upper()
            setattr(self.__class__, value_method.__name__, value_method)
            """

    def __repr__(self):
        """
        Returns:
            __str__()
        """
        return self.__str__()

    def __str__(self):
        """
        Returns:
            str of our values.
        """
        return f"{self.__values}"

    def __eq__(self, other):
        """
        Parameters:
            VectorX
        Returns:
            bool if this Vector2 is equal to another Vector2.
        """
        if not isinstance(other, self.__class__):
            return False
        return self.get_value_list() == other.get_value_list()

    def __sub__(self, other):
        """
        Parameters:
            VectorX
        Returns:
            VectorX
        """
        if not isinstance(other, self.__class__):
            raise ValueError(f"Expected {self.__class__}")
        return self.__class__(
            [j - k for (j, k) in zip(
                self.get_value_list(), other.get_value_list()
            )])

    def get(self):
        """
        Returns:
            dict of values
        """
        return self.__values

    def get_value_list(self):
        """
        Returns:
            [float, ...]
        """
        return list(self.__values.values())

    def set(self, values):
        """
        Parameters:
            [float, ...]
        """
        if (
            not isinstance(values, list) or
            not all(isinstance(v, float) for v in values) or
            not len(values) == len(self.__values)
        ):
            raise ValueError(
                f"Didn't receive at least {len(self.__values)} floats."
            )
        i = 0
        for k in self.__values.keys():
            self.__values[k] = values[i]
            i += 1


class Vector2(Vector):

    def __init__(self, *args):
        Vector.__init__(self, *args, values=["x", "y"])
