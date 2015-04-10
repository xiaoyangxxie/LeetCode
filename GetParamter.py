__author__ = 'xyang'
import Config

paramter = {}
paramter['dbname'] = Config.getConfig("database", "dbname")
paramter['dbport'] = Config.getConfig("database", "dbport")
print paramter