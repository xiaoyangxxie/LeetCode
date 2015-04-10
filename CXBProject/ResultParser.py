import subprocess
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

class ResultParser(object):
    def __init__(self, xmlFile):
        # xmlFile is the file path
        self.tree = ET.ElementTree(file = xmlFile)      #xml is parsed here

    def get_failed_case_num(self):
        for elem in self.tree.findall('.//statistics/total/stat'):
            if elem.text == 'All Tests':
                return elem.attrib['fail']

    def get_passed_case_num(self):
        for elem in self.tree.findall('.//statistics/total/stat'):
            if elem.text == 'All Tests':
                return elem.attrib['pass']

    def get_failed_case_num_by_name(self, name):
        for elem in self.tree.findall('.//statistics/suite/stat'):
            if elem.attrib['name'] == name:
                return elem.attrib['fail']

    def get_passed_case_num_by_name(self, name):
        for elem in self.tree.findall('.//statistics/suite/stat'):
            if elem.attrib['name'] == name:
                return elem.attrib['pass']

    def write(self, path):
        self.tree.write(path)

    def merge_result(self, xmlFile):
        # xmlFile is the file path.
        treeMerge = ET.ElementTree(file = xmlFile)
        self._merge_result(treeMerge)

    def _merge_result(self, elementTree):
        suiteName = ['Address Capture Page', 'Call Queue Page','Call Transfer Page','Compare','Data Page',
                     'Logic Page','Message Page','Name Capture Page','QuestionPage','Reverse Phone Lookup',
                     'Schedule Page','SMS Page','Transaction Page','Voice Mail Page']

        for elem in elementTree.iter(tag='test'):
            test_name = elem.attrib['name']
            for e in elem.findall('./status'):
                if e.attrib['status'] == 'PASS':
                    double_check_status = 'PASS'
                else:
                    double_check_status = 'FAIL'

            for elem in self.tree.findall('.//test'):
                if elem.attrib['name'] == test_name:
                    for child_elem in elem.findall('.//status'):
                        if child_elem.attrib['status'] == 'FAIL' and double_check_status == 'PASS':
                            child_elem.set('status', 'PASS')
                            #self._replace_test_node(elementTree, test_name)

        for name in suiteName:
            if self.get_passed_case_num_by_name(name) == '0':
                for elem in self.tree.findall('.//suite[@name="%s"]/*' %(name, )):
                    if elem.tag != 'suite':
                        self.tree.find('.//suite[@name="%s"]' %(name, )).remove(elem)
                for e in elementTree.findall('.//suite[@name="%s"]/*' %(name, )):
                    if e.tag != 'suite':
                        self.tree.find('.//suite[@name="%s"]' %(name, )).append(e)

    def _replace_suite_node(self, elementTree, nodeName):
        # elementTree is the source xml tree which will merge into self.tree
        # nodeName is the name attribute of the element to replace
        self.tree.find('.//suite[@name="%s"]/..' %(nodeName, )).append(elementTree.find('.//suite[@name="%s"]' %(nodeName, )))
        self.tree.find('.//suite[@name="%s"]/..' %(nodeName, )).remove(self.tree.find('.//suite[@name="%s"]' %(nodeName, )))

    def _replace_test_node(self, elementTree, nodeName):
        self.tree.find('.//test[@name="%s"]/..' %(nodeName, )).append(elementTree.find('.//test[@name="%s"]' %(nodeName, )))
        self.tree.find('.//test[@name="%s"]/..' %(nodeName, )).remove(self.tree.find('.//test[@name="%s"]' %(nodeName, )))

if __name__ == '__main__':
    parser = ResultParser('output.xml')
    parser.merge_result('doublecheck-output.xml')
    parser.write('final.xml')
    subprocess.call('rebot -n asr -o final-output.xml -r final-report.html -l final-log.html final.xml', shell=True)