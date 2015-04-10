__author__ = 'xyang'

import os
import sys
import shutil



files = os.listdir('D:\\NGTTProject\\aPage\Multi_ASR\\800-002-1020')
filepath= "D:\\NGTTProject\\aPage\Multi_ASR\\800-002-1020\\test_suite_debug.cfg"
testcase = "test_case"
lines = open(filepath).readlines()
fp = open('test_suite_debug.cfg','w')
for s in lines:
    count = 0
    if testcase in s:
        fp.write(s.lstrip('#'))
        count += 1
    else:
        fp.write(s)
        count += 1
print "case number is " + str(count)
fp.close()
shutil.move('test_suite_debug.cfg', filepath)


