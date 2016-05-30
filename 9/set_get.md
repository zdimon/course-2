## Descroptors

A descriptor is an object with any of the following methods (__get__, __set__, or __delete__), intended to be used via dotted-lookup as if it were a typical attribute of an instance.

Protocol.

descriptor.__get__(self, obj_instance, owner_class) (returning a value)
is invoked by
obj_instance.descriptor
descriptor.__set__(self, obj_instance, value) (returning None)
is invoked by
obj_instance.descriptor = value
descriptor.__delete__(self, obj_instance) (returning None)
is invoked by
del obj_instance.descriptor


