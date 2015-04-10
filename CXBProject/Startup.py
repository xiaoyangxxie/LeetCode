'''
Created on Jul 8, 2013

@author: chzhou
'''
import os
import sys
import getopt
import subprocess
import shutil
import xml.etree.cElementTree as ET
from ResultParser import ResultParser
from start_from_jenkins import run_tests, run_failed
from Config import Config
try:
    import Selenium2Library
except ImportError, e:
    print 'Importing Selenium2Library module failed (%s).' % e
    print 'Please make sure you have Selenium2Library properly installed.'
    print 'See INSTALL.rst for troubleshooting information.'
    sys.exit(1)

def get_parameter():
    parameter = {}
    cfg = Config('config.cfg')
    #cfg = Config('CXBuilder-Automation\config.cfg')
    parameter['baseUrl'] = cfg.get_parameter('baseurl')
    parameter['browser'] = cfg.get_parameter('browser')
    parameter['loginEmail'] = cfg.get_parameter('loginemail')
    parameter['loginPassword'] = cfg.get_parameter('loginpassword')
    parameter['enableProfile'] = cfg.get_parameter('enableprofile')
    parameter['screenshotOnError'] = cfg.get_parameter('screenshotonerror')
    parameter['executeSpeed'] = cfg.get_parameter('executespeed')
    parameter['outputDir'] = cfg.get_parameter('outputdir')
    parameter['RecordORTest'] = cfg.get_parameter('recordortest')
    parameter['runningModule'] = cfg.get_parameter('allorcaseorsuiteortag')
    parameter['project'] = cfg.get_parameter('project')
    parameter['case'] = cfg.get_parameter('case')
    parameter['suite'] = cfg.get_parameter('suite')
    parameter['tag'] = cfg.get_parameter('tag')
    parameter['runfailedcase'] = cfg.get_parameter('runfailed')
    return parameter

if __name__ == '__main__':
    parameter = get_parameter()
    run_tests(parameter)
    run_failed(parameter)