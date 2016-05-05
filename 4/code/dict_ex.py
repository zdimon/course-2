dict = {1: 'one', 2: 'two'}
print dict[1]
#print dict[3]
print dict.get(3,'no')

seq = ('name', 'age', 'sex')
val = (10,20,30)
dict = dict.fromkeys(seq,val)
print dict

dict = {1:'one', 2:'two'}
print dict.items()
print dict.get(3,'none')
print dict.setdefault(2, None)

dict.update({3:'thre', 4:'four'})
print dict 

print dict.values()
