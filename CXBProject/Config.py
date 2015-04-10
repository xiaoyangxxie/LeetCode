import sys
import ConfigParser

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Config(object):
    def __init__(self, fileName):
        self.cfgInfo = {}
        self._parse_config(fileName)

    def _parse_config(self, fileName):
        config = ConfigParser.ConfigParser()
        config.read(fileName)
        for section in config.sections():
            for option in config.options(section):
                self.cfgInfo[option.lower()] = config.get(section, option, True)

    def get_parameter(self, para_name):
        try:
            return self.cfgInfo[para_name]
        except KeyError:
            print 'No parameter called "%s" exists in config file.' %(para_name, )
            sys.exit(1)

if __name__ == '__main__':
    cfg1 = Config('config.cfg')
    cfg2 = Config('config.cfg')
    print cfg1.get_parameter('baseurl')
    print cfg1.get_parameter('runfailed')
    print cfg2.get_parameter('outputdir')
    print cfg2.get_parameter('case')