import sys, StringIO

out = StringIO.StringIO()

sys.stdout = out

print "hi, I'm going out"

sys.stdout = sys.__stdout__

#print out.getvalue()

import pdb; pdb.set_trace()
