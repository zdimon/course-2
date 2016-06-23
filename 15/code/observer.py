class Freedge(object):
    users = []
    def give_icecream_to_all(self):
        for u in self.users:
            u.get()

    def add_user(self,user):
        self.users.append(user)

    def remove_user(self,user):
        for index, u in enumerate(self.users):
            if u.name == user.name:
                del self.users[index]

class User(object):
    name = ''
    def __init__(self,name):
        self.name = name
    def get(self):
        import time
        file_name = self.name+'.txt'
        f = open(file_name,'w+')
        f.write('open the freedge')
        time.sleep(2)
        f.write('take some icecream')
        time.sleep(2)
        f.write('close the freedge')
        f.close()

user1 = User('dima')
user2 = User('vova')
freedge = Freedge()
freedge.add_user(user1)
import pdb; pdb.set_trace()
freedge.add_user(user2)
freedge.give_icecream_to_all()





