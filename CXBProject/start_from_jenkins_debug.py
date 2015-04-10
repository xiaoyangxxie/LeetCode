import os
import sys
import time
import getopt
import subprocess
import shutil
import xml.etree.cElementTree as ET
from ResultParser import ResultParser
try:
    import Selenium2Library
except ImportError, e:
    print 'Importing Selenium2Library module failed (%s).' % e
    print 'Please make sure you have Selenium2Library properly installed.'
    print 'See INSTALL.rst for troubleshooting information.'
    sys.exit(1)

ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIGDIR = os.path.join(ROOT,'config.cfg')
DEFAULTOUTPUTDIR = os.path.join(ROOT,'report')

VARIABLE = ''
ARGUMENT = ''
RUNCONFIG =''

FASTSPEED = '0'
NORMALSPEED = '0.4'
SLOWSPEED = '0.8'

DOUBLE_CHECK = 'doublecheck'
FINAL = 'final'

def get_parameter():
    """
    -u baseUrl
    -b browser
    -e loginEmail
    -p loginPassword
    -f enableProfile
    -s screenshotOnError
    -d executeSpeed
    -o ouputDir
    -t RecordORTest
    -m runningModeule
    -j project
    -c case
    -i suite
    -a tag
    -r runfailedcase
    -l emaillist
    """
    parameter = {}
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:b:e:p:f:s:d:o:t:m:j:c:i:a:r:l:")
    except getopt.GetoptError:
        print get_parameter.__doc__
        sys.exit(2)
    parameter['baseUrl'] = ''
    parameter['browser'] = ''
    parameter['loginEmail'] = ''
    parameter['loginPassword'] = ''
    parameter['enableProfile'] = ''
    parameter['screenshotOnError'] = ''
    parameter['executeSpeed'] = ''
    parameter['outputDir'] = ''
    parameter['RecordORTest'] = ''
    parameter['runningModule'] = ''
    parameter['project'] = ''
    parameter['case'] = ''
    parameter['suite'] = ''
    parameter['tag'] = ''
    parameter['runfailedcase'] = ''
    parameter['emaillist'] = ''
    for op, value in opts:
        if op == '-u':
            parameter['baseUrl'] = value
        elif op == '-b':
            parameter['browser'] = value
        elif op == '-e':
            parameter['loginEmail'] = value
        elif op == '-p':
            parameter['loginPassword'] = value
        elif op == '-f':
            parameter['enableProfile'] = value
        elif op == '-s':
            parameter['screenshotOnError'] = value
        elif op == '-d':
            parameter['executeSpeed'] = value
        elif op == '-o':
            parameter['outputDir'] = value
        elif op == '-t':
            parameter['RecordORTest'] = value
        elif op == '-m':
            parameter['runningModule'] = value
        elif op == '-j':
            parameter['project'] = value
        elif op == '-c':
            parameter['case'] = value
        elif op == '-i':
            parameter['suite'] = value
        elif op == '-a':
            parameter['tag'] = value
        elif op == '-r':
            parameter['runfailedcase'] = value
        elif op == '-l':
            parameter['emaillist'] = value
    return parameter

def generate_command(parameter):
    baseUrl = parameter['baseUrl']
    browser = parameter['browser']
    loginEmail = parameter['loginEmail']
    loginPassword = parameter['loginPassword']
    enableProfile = parameter['enableProfile']
    screenshotOnError = parameter['screenshotOnError']
    executeSpeed = parameter['executeSpeed']
    outputDir = parameter['outputDir']
    RecordORTest = parameter['RecordORTest']
    runningModule = parameter['runningModule']
    emaillist = parameter['emaillist']
    case = parameter['case']
    suite = parameter['suite']
    tag = parameter['tag']
    project = parameter['project']

    '''define varible to run '''
    global VARIABLE
    VARIABLELIST = []
    if baseUrl.__len__() != 0:
        if not baseUrl.startswith('http://'):
            baseUrl = '%s%s' % ('http://', baseUrl)
        baseUrl = '%s%s' % ('baseUrl:',baseUrl)
        VARIABLELIST.append(baseUrl)
    else:
        raise AssertionError("baseUrl is required.please give the value in config.cfg.")

    if browser.__len__() != 0:
        browser = '%s%s' % ('browser:',browser)
        VARIABLELIST.append(browser)
    else:
        browser = '%s%s' % ('browser:','ff')
        VARIABLELIST.append(browser)

    if loginEmail.__len__() != 0:
        loginEmail = '%s%s' % ('loginEmail:',loginEmail)
        VARIABLELIST.append(loginEmail)
    else:
        raise AssertionError('loginEmail is required, please give the value in config.cfg.')

    if loginPassword.__len__() != 0:
        loginPassword = '%s%s' % ('loginPassword:',loginPassword)
        VARIABLELIST.append(loginPassword)
    else:
        raise AssertionError('loginPassword is required, please give the value in config.cfg.')

    if enableProfile.__len__() !=0:
        enableProfile = '%s%s' % ('enableProfile:',enableProfile)
        VARIABLELIST.append(enableProfile)
    else:
        enableProfile = '%s%s' % ('enableProfile:','yes')
        VARIABLELIST.append(enableProfile)

    if screenshotOnError.__len__() != 0:
        screenshotOnError = '%s%s' % ('screenshotOnError:',screenshotOnError)
        VARIABLELIST.append(screenshotOnError)
    else:
        screenshotOnError = '%s%s' % ('screenshotOnError:','yes')
        VARIABLELIST.append(screenshotOnError)

    if executeSpeed.__len__() !=0:
        if executeSpeed == 'slow':
            executeSpeed = '%s%s' % ('executeSpeed:',SLOWSPEED)
        elif  executeSpeed == 'normal':
            executeSpeed = '%s%s' % ('executeSpeed:',NORMALSPEED)
        else:
            executeSpeed = '%s%s' % ('executeSpeed:',FASTSPEED)
        VARIABLELIST.append(executeSpeed)

    if emaillist.__len__() !=0:
        emaillist == 's%s%' % ('emaillist:',emaillist)
        VARIABLELIST.append(emaillist)
    else:
        raise AssertionError('emaillist is required,please give the value')

    if RecordORTest.__len__() != 0:
        RecordORTest = '%s%s' % ('recordOrTest:',RecordORTest)
        VARIABLELIST.append(RecordORTest)
    else:
        RecordORTest = '%s%s' % ('recordOrTest:','Test')
        VARIABLELIST.append(RecordORTest)

    VARIABLE = ' --variable '.join(VARIABLELIST)
    VARIABLE = '%s%s' % (' --variable ',VARIABLE)

    '''get the project name'''
    PROJECTDIR = os.path.join(ROOT,project)

    global ARGUMENT
    if outputDir.__len__() != 0:
        if outputDir == 'default':
            if os.path.exists(DEFAULTOUTPUTDIR):
                shutil.rmtree(DEFAULTOUTPUTDIR)
                time.sleep(5)
                os.mkdir(DEFAULTOUTPUTDIR)
            outputDir = '%s %s' % ('--outputdir',DEFAULTOUTPUTDIR)
        else:
            outputDir = os.path.join(outputDir,'report')
            if os.path.exists(outputDir):
                shutil.rmtree(outputDir)
                time.sleep(5)
                os.mkdir(outputDir)
            outputDir = '%s %s' % ('--outputdir',outputDir)
    elif outputDir.__len__() == 0:
        if os.path.exists(DEFAULTOUTPUTDIR):
            shutil.rmtree(DEFAULTOUTPUTDIR)
            time.sleep(5)
            os.mkdir(DEFAULTOUTPUTDIR)
        outputDir = '%s %s' % ('--outputdir',DEFAULTOUTPUTDIR)
    ARGUMENT = ' %s%s ' % (ARGUMENT,outputDir)

    LIBRARYDIR = os.path.join(PROJECTDIR,'Library')
    libraryArg = '%s %s' % ('--pythonpath',LIBRARYDIR)
    ARGUMENT = ' %s %s ' % (ARGUMENT,libraryArg)

    global RUNCONFIG

    if runningModule == 'all':
        RUNCONFIG = PROJECTDIR
    elif runningModule == 'case':
        caseList = case.split(',')
        for c in caseList:
            c.strip()
            if c != '':
                RUNCONFIG = '%s%s%s' % (RUNCONFIG,' --test ',c)
        RUNCONFIG = '%s %s' % (RUNCONFIG,PROJECTDIR)
    elif runningModule == 'suite':
        suiteList = suite.split(',')
        for s in suiteList:
            s.strip()
            if s != '':
                RUNCONFIG = '%s%s%s' % (RUNCONFIG,' --suite ',s)
        RUNCONFIG = '%s %s' % (RUNCONFIG,PROJECTDIR)
    elif runningModule == 'tag':
        tagList = tag.split(',')
        for t in tagList:
            t.strip()
            if t != '':
                RUNCONFIG = '%s%s%s' % (RUNCONFIG,' --include ',t)
        RUNCONFIG = '%s %s' % (RUNCONFIG,PROJECTDIR)
    else:
        raise AssertionError("plese give the allORcaseORsuiteORtag value in config.cfg to define how to run the project")

def run_failed(parameter):
    browser = parameter['browser']
    executeSpeed = parameter['executeSpeed']
    outputDir = parameter['outputDir']
    runfailedcase = parameter['runfailedcase']
    project = parameter['project']

    runFailed = '%s %s' %('--runfailed', outputDir + r'\report\output.xml')
    reportDir = outputDir + r'\report'

    parser = ResultParser(r'%s\output.xml' % (reportDir,))

    if runfailedcase == 'no'or parser.get_failed_case_num() == '0':
        # No need to run failed case, because all cases passed
        subprocess.call(r'copy %s\output.xml %s\%s-output.xml' %(reportDir, reportDir, FINAL), shell=True)
        subprocess.call(r'copy %s\report.html %s\%s-report.html' %(reportDir, reportDir, FINAL), shell=True)
        subprocess.call(r'copy %s\log.html %s\%s-log.html' %(reportDir, reportDir, FINAL), shell=True)
        return

    global VARIABLE
    VARIABLELIST = []

    if browser.__len__() != 0:
        browser = '%s%s' % ('browser:',browser)
        VARIABLELIST.append(browser)
    else:
        browser = '%s%s' % ('browser:','ff')
        VARIABLELIST.append(browser)

    if executeSpeed.__len__() !=0:
        if executeSpeed == 'slow':
            executeSpeed = '%s%s' % ('executeSpeed:',SLOWSPEED)
        elif  executeSpeed == 'normal':
            executeSpeed = '%s%s' % ('executeSpeed:',NORMALSPEED)
        else:
            executeSpeed = '%s%s' % ('executeSpeed:',FASTSPEED)
        VARIABLELIST.append(executeSpeed)

    VARIABLE = ' --variable '.join(VARIABLELIST)
    VARIABLE = '%s%s' % (' --variable ',VARIABLE)

    PROJECTDIR = os.path.join(ROOT,project)

    global ARGUMENT
    if outputDir.__len__() != 0:
        if outputDir == 'default':
            outputDir = '%s %s' % ('--outputdir',DEFAULTOUTPUTDIR)
        else:
            outputDir = os.path.join(outputDir,'report')
            outputDir = '%s %s' % ('--outputdir',outputDir)
    elif outputDir.__len__() == 0:
        outputDir = '%s %s' % ('--outputdir',DEFAULTOUTPUTDIR)

    ARGUMENT = '%s %s ' % (ARGUMENT,runFailed + ' ' + outputDir + r' -o %s-output.xml -r %s-report.html -l %s-log.html' %(DOUBLE_CHECK, DOUBLE_CHECK, DOUBLE_CHECK))

    LIBRARYDIR = os.path.join(PROJECTDIR,'Library')
    libraryArg = '%s %s' % ('--pythonpath',LIBRARYDIR)
    ARGUMENT = ' %s %s ' % (ARGUMENT,libraryArg)
    ARGUMENT = '%s %s' % (ARGUMENT, PROJECTDIR)

    cmd = r"pybot -n asr %s %s" %(VARIABLE, ARGUMENT, )
    subprocess.call(cmd, shell=True)

    parser.merge_result(r'%s\%s-output.xml' % (reportDir, DOUBLE_CHECK))
    parser.write('%s\%s.xml' % (reportDir, FINAL))

    subprocess.call(r"rebot -n asr --outputdir %s -o %s-output.xml -r %s-report.html -l %s-log.html %s\%s.xml" %(reportDir, FINAL, FINAL, FINAL, reportDir, FINAL), shell=True)

def run_tests(parameter):
    generate_command(parameter)
    pybotCommand = '%s -n asr %s %s %s' % ('pybot ',ARGUMENT,VARIABLE,RUNCONFIG)
    subprocess.call(pybotCommand, shell=True)

if __name__ == '__main__':
    parameter = get_parameter()
    run_tests(parameter)
    run_failed(parameter)