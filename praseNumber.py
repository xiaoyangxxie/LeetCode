__author__ = 'xyang'
import time
from datetime import date,timedelta

def list_should_contain(textlist, value):
    for c in value:
        print c
        print "index:", textlist.index(c)
    return True


def time_is_captured(timelist):
    atime = ['0515p', '0515a' ,'2015h']
    print atime
    result = list_should_contain(timelist,atime)
    return result

def date_is_captured(datelist):
    c_date = time.strftime('%Y%m%d')
    yeserday = date.today() - timedelta(1)
    yeserday = yeserday.strftime('%Y%m%d')
    tommorrow = date.today() + timedelta(1)
    tommorrow = tommorrow.strftime('%Y%m%d')
    adate = ['20150307','19800307','19800407','19800309','20150309',c_date,yeserday,tommorrow]
    result = list_should_contain(datelist,adate)
    return result

def currency_is_captured(currencylist):
    currency =['EUR32.00' ,'EUR32.05','EUR0.05','BRL32.00','EUR3.00','EUR04.00','USD5.25']
    result = list_should_contain(currencylist,currency)
    return result

def list_should_not_contain(strlist, str):
    for c in str:
         if c in strlist:
             print "should not in the list: " + c
             raise AssertionError
         else:
             print  "can not find it in the list: " + c
             return False


def speech_input_value_is_captured(timelist,datelist,currencylist):
    brl = ['BRR35.05']
    time_is_captured(timelist)
    date_is_captured(datelist)
    currency_is_captured(currencylist)
    list_should_not_contain(currencylist,brl)




