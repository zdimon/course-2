from subprocess import call
file = open('output.txt','w')
call('ls',stdout=file,shell=True)
print 'done!'

