class Utils:
    
    def get_page_number_from_list(self, nums):
        """ To determine which number is page number.
        For example: Input: 1, 2, 3, 4 Output: 5
        Input 1, 3, 4, 5 Output: 2
        """
        numList = list(nums)
        numList = [int(e) for e in numList]
        maxNum = max(numList) + 1
        for i in range(1, maxNum):
            if i not in numList:
                return i
        return maxNum
        
    
    def get_date(self):
        pass

    def strip_string_in_list(self, list):
        return [s.strip() for s in list]

    def get_page_title(self, suite_name):
        if suite_name == "Voice Mail Page":
            return "Voicemail page"
        elif suite_name == "Reverse Phone Lookup":
            return "New Reverse Phone Lookup Page"
        elif suite_name == "QuestionPage":
            return "Question Page"
        else:
            return suite_name

if __name__ == "__main__":
    u = Utils()
    li = [1, 2, 3, 4, 5, 6]
    print type(u.get_page_number_from_list(li))
