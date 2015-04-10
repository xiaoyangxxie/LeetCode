__author__ = 'xyang'
import os
import re

def simpe():
    foo= "dsdsds"
    if foo.startswith('bar'):
        print "yes"
    else:
        print "no"

def string_number(alist,ex_str):
    counts = alist.count(ex_str)
    return counts


def dup_character(alist):
    counts = {}
    order =[]
    for s in alist:
        for s in order:
            counts[s]+=1
        else:
            counts[s]=1
            order.append(s)
    for i in order:
        if counts[i] ==1:
            return i
def match():
    astr = 'an example word:cat!!'
    amatch = re.search(r'word:\w\w\w', astr)
#   If-statement after search() tests if it succeeded
    if match:
        print 'found', amatch.group() ## 'found word:cat'
    else:
        print 'did not find'

if __name__=="__main__":
    alist =['1','2','3']
    number = string_number(alist,'1')
    print number
    #dup_character(alist)
    match()
