from robot.libraries.BuiltIn import BuiltIn
import re
import os
import sys
from robot.api import logger

class S2ExLibrary:
    
    def __init__(self):
        self.seleniumlib = BuiltIn().get_library_instance('Selenium2Library')

    def get_text_list_from_elements(self, locator, regex):
        """ Get the text from elements located by locator.
        This method is just for extract page numbers, and need to fix        
        """
        elements = self.seleniumlib._element_find(locator, False, False)
        pattern = re.compile(regex)
        text = []
        for element in elements:
            if re.match(pattern, element.get_attribute('id')) is not None:
                text.append(element.text)
        return text
    
    def get_site_number(self):
        """ Use module re to match site number in the text of 'mainFormTable' element
        """
        element = self.seleniumlib._element_find('id=mainFormTable', True, True)
        pattern = re.compile('\d{12}')
        source = element.text
        number = re.findall(pattern, source)[0]
        return number
    
    def element_should_match_x_times(self, locator, times, message=''):
        """ To verify how many times the element located by locator occurs
        """
        self._info("Verifying element '%s' match '%s' times."
                    % (locator, times))
        elements = []
        elements = self.seleniumlib._element_find(str(locator), False, False)
        if len(elements) != int(times):
            if not message:
                message = "Element '%s' should match '%s' times but "\
                          "match '%s' times." % (locator, times, len(elements))
            raise AssertionError(message)
        
    def get_count_of_variables(self, locator, regex):
        elements = self.seleniumlib._element_find(locator, False, False)
        pattern = re.compile(regex)
        count = 0
        for element in elements:
            if re.match(pattern, element.get_attribute('id')) is not None:
                count += 1
        return count
    
    def get_text_list_from_elements_By_Locator(self, locator):
        """ Get the text from elements located by locator.
        This method is just for extract page numbers, and need to fix        
        """
        elements = self.seleniumlib._element_find(locator, False, False)
        text = []
        for element in elements:
            if element.text.__len__() > 0:
                text.append(element.text)
        return text

    def get_id_list_by_locator(self, locator):
        """ Get the id from elements by locator.               
        """
        elements = self.seleniumlib._element_find(locator, False, False)
        idList = []
        for element in elements:
            idList.append(element.get_attribute('id'))
        return idList
		
    def click_element_by_no(self, no, locator):
        """ Get the elements defined by the locator.
        Return the element designated by the no.
        """
        elements = self.seleniumlib._element_find(locator, False, False)
        self.seleniumlib._info("There are '%s' elements in this page." % len(elements))
        no = int(no) - 1
        elements[no].click()
        
    def select_all_checkboxes(self, locator):
        """ Select all the checkboxes with the same name.
        """
        elements = self.seleniumlib._element_find(locator, False, False, tag='input')
        if len(elements) > 0 :
            for element in elements:
                if not element.is_selected():
                    element.click()
    
    def radio_button_should_be_selected(self, locator):
        """ Check radio button whether is selected by id.
        """
        element = self.seleniumlib._element_find(locator, True, True, tag='input')
        return element.is_selected()
    
    def click_visible_element(self, locator, no):
        """ Click element which is visible.
        """
        elements = self.seleniumlib._element_find(locator, False, False)
        elements = [e for e in elements if e.is_displayed()]
        self.seleniumlib._info("There are '%s' elements in this page." % len(elements))
        no = int(no) - 1
        elements[no].click()
       
        
    def set_element_attr(self, locator, attr, value):
        """ Change element attribute by value.
        """
        element = self.seleniumlib._elemtn_find(locator, True, True)
        element.set_attribute(str(attr), str(value))
        
    def get_visible_element_value(self, locator, no):
        """ Get visible element value ordered by no.
        """
        elements = self.seleniumlib._element_find(locator, False, False)
        elements = [e for e in elements if e.is_displayed()]
        self.seleniumlib._info("There are '%s' elements in this page." % len(elements))
        no = int(no) - 1
        return elements[no].get_attribute('value') if elements[no] is not None else None
    
    def visible_element_value_should_be(self, locator, val, no):
        elements = self.seleniumlib._element_find(locator, False, False)
        elements = [e for e in elements if e.is_displayed()]
        self.seleniumlib._info("There are '%s' elements in this page." % len(elements))
        no = int(no) - 1
        actual_val = elements[no].get_attribute('value') if elements[no] is not None else None
        return str(actual_val) == (str(val))
     
    def get_label_value_by_text(self, locator, text):
        elements = self.seleniumlib._element_find(locator, True, True).find_elements_by_tag_name("option")
        for e in elements:
            if text in e.text:
                return e.get_attribute("value")

    def _parse_locator(self, locator):
        prefix = None
        criteria = locator
        if not locator.startswith('//'):
            locator_parts = locator.partition('=')
            if len(locator_parts[1]) > 0:
                prefix = locator_parts[0].strip().lower()
                criteria = locator_parts[2].strip()
        return (prefix, criteria)

    def select_label(self, locator, text):
        value = self.get_label_value_by_text(locator, text)
        (prefix, criteria) = self._parse_locator(locator)
        if prefix == "id" or prefix == None:
            self.seleniumlib.execute_javascript('$("#%s").val("%s").mousedown().change()' % (criteria, value))
        elif prefix == "name":
            self.seleniumlib.execute_javascript('$("[name=%s]").val("%s").mousedown().change()' % (criteria, value))
        elif prefix == "class":
            self.seleniumlib.execute_javascript('$(".%s").val("%s").mousedown().change()' % (criteria, value))
        else:
            raise AssertionError("Unsupported locator, support id and name")

    def choose_voice_site_in_browse_voice_pages_for_chrome(self, script, title):
        try:
            #window_handle = self.seleniumlib._current_browser()
            #driver = self.seleniumlib._current_browser()
            #driver.get_window_handle()
            self.seleniumlib.execute_javascript(script)
            self.seleniumlib.execute_javascript(script)
        except:
            #self.seleniumlib._current_browser().execute(Command.SWITCH_TO_WINDOW, {'title': title})
            self.seleniumlib.select_window(title)
            logger.info("====select window====",True,True)


if __name__ == "__main__":
    b = BuiltIn()
