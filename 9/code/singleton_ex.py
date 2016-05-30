class B(object):
    pass

class C(object):
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(C, cls).__new__(cls)
        return cls.instance

import pdb; pdb.set_trace()
