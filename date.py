__author__ = 'xyang'


d={}
a =['1','1','2','2','2','3']
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
#print d
b = ['4','6']
for i in b:
    if i in a:
        if d[i] == 2:
            print "the count is 2"
        else:
            raise AssertionError
    else:
        print "I'm %s years old" %i