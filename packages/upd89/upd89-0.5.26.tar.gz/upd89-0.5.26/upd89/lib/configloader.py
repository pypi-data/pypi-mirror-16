import configparser
import os.path


class ConfigLoader:

    def __init__(self, configname):
        if os.path.isfile(configname):
            self.config = configparser.ConfigParser()
            self.configname = configname
            self.config.read(self.configname)
        else:
            print("Configfile (%s) not found." % configname)
            exit(1)

    def __str__(self):
        return repr(self)

    def getWebserverPort(self):
        return(self.config['webserver']['port'])

    def getWebserverLogfile(self):
        return(self.config['webserver']['logfile'])

    def getWebserverPidfile(self):
        return(self.config['webserver']['pidfile'])

    def getServerHost(self):
        return(self.config['controlcenter']['host'])

    def getServerPort(self):
        return(self.config['controlcenter']['port'])

    def getTlsPath(self):
        return(self.config['tls']['path'])

    def getTlsCa(self):
        return(self.config['tls']['cacert'])

    def getTlsPrivKey(self):
        return(self.config['tls']['privkey'])

    def getTlsPubCert(self):
        return(self.config['tls']['pubcert'])

    def getDataDir(self):
        return(self.config['agent']['datadir'])

    def getLogFile(self):
        return(self.config['agent']['logfile'])

    def getPidFile(self):
        return(self.config['agent']['pidfile'])

    def is_registered(self):
        return self.__ret_if_exists('controlcenter', 'registered') == "true"

    def set_registered(self):
        self.__set_config('controlcenter', 'registered', "true")

    def reloadConfig(self):
        self.config.read(self.configname)

    def __set_config(self, group, tag, value):
        self.config[group][tag] = value
        with open(self.configname, 'w') as configfile:
            self.config.write(configfile)

    def __ret_if_exists(self, group, tag):
        if self.config.has_option(group, tag):
            return(self.config[group][tag])
        else:
            return None
