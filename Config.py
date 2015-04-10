__author__ = 'xyang'
import ConfigParser
import os

"""
get date from config file
"""


def getConfig(section, key):
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '\db.cfg'
    #print path
    config.read(path)
    return config.get(section, key)

