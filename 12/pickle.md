##Pickle

The pickle module implements a fundamental, but powerful algorithm for 
serializing and de-serializing a Python object structure.

    pickle.dump(obj, file[, protocol])¶
    pickle.load(file)
    pickle.dumps(obj[, protocol])
    pickle.loads(obj[, protocol])

###what can be pickled

None, True, and False

integers, long integers, floating point numbers, complex numbers

normal and Unicode strings

tuples, lists, sets, and dictionaries containing only picklable objects

functions defined at the top level of a module

built-in functions defined at the top level of a module

classes that are defined at the top level of a module

instances of such classes whose __dict__ or the result of calling __getstate__() is picklable (see section The pickle protocol for details)
