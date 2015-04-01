__author__ = 'xyang'

import os
import sys
files = os.listdir('D:\\NGTTProject\\aPage\Multi_ASR\\800-002-1020')
filepath= "D:\\NGTTProject\\aPage\Multi_ASR\\800-002-1020\\test_suite_debug.cfg"
testcase = "test_case"
count = 0
lines = open(filepath).readlines()
fp = open('test_suite_debug.cfg','w')
for s in lines:
    if testcase in s:
       # print s
        fp.write(s.lstrip('#'))
        count += 1
    else:
        print "skip"
print "case number is " + str(count)
fp.close()
