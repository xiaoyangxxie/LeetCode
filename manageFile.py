__author__ = 'xyang'

import os
import shutil
import fileinput
import re

class manageFile():

    def __init__(self):
        pass

    def remove_character(self, filepath, count, testcase,mode):
        lines = open(filepath).readlines()
        fp = open('test_suite_debug.cfg','w')
        for s in lines:
            if testcase in s:
                fp.write(s.lstrip('#'))
                count += 1
            elif mode == 1:
                fp.write(s)
                count += 1
            elif mode == 2:
                count +=1
            else:
                fp.write(s)
        print "case number is " + str(count)
        fp.close()
        shutil.move('test_suite_debug.cfg', filepath)

    def add_character(self,filepath, count, testcase,comment):
        lines = open(filepath).readlines()
        fp = open('test_suite_debug.cfg','w')
        for s in lines:
            if testcase in s:
                fp.write(s.replace(testcase,comment))
                count += 1
            else:
                fp.write(s)
                count += 1
        print "case number is " + str(count)
        fp.close()
        shutil.move('test_suite_debug.cfg', filepath)

    def append_file(self,source,des,last):
        file = open(des,"r")
        fileadd = open(source,"r")
        conten = file.read()
        contenadd = fileadd.read()
        pos = conten.find(last)
        print pos
        if pos != -1:
            conten = conten[:pos] + contenadd
            file = open(des,"w")
            file.write(conten)
            print "OK"

    def append_file_mem(self,copyfifle,sourcefile,newfile):
        with open(copyfifle,'rb') as fin1, \
                open(sourcefile,'rb') as fin2,  \
                open(newfile,'wb') as fout:
                shutil.copyfileobj(fin1, fout)
                fin1.seek(-len(os.linesep), 2)
                if fin1.read() != os.linesep:
                    fout.write(os.linesep)
                shutil.copyfileobj(fin2, fout)


if __name__ == '__main__':
    fp = manageFile()
    files = os.listdir('D:\\NGTTProject\\aPage\Multi_ASR\\800-002-1020')
    path= "D:\\NGTTProject\\aPage\Multi_ASR\\800-002-1020\\test_suite_debug.cfg"
    despath= "D:\\NGTTProject\\aPage\Multi_ASR\\800-002-1020\\test_suite.cfg"
    testcase = "test_case"
    comment = "#test_case"
    count = 0
    #fp.remove_character(path,count,testcase,2)
    #fp.add_character(path,count,testcase,comment)
    fp.append_file(path,despath,"digit_fr_8")
    #fp.append_file_mem()