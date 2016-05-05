lst = [2,4,7,3,9]    

def compare(it1,it2):
    if it1>it2:
        return 1
    else:
        return -1

lst.sort(compare)
print lst


lst = [('c', 4), ('b', 2), ('a', 3)] 

def letter_cmp(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] == b[1]:
        if a[0] > b[0]:
            return 1
        else:
            return -1
    else:
        return 1

lst.sort(letter_cmp)
print lst


