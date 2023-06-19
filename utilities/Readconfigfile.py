import configparser

config = configparser.RawConfigParser()

config.read("C:\\Users\\HP\\Desktop\\Python\\OrangeHRM\\Configuration\\config.ini")


class ReadValue():

    @staticmethod
    def getUsername():
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login info', 'password')
        return password
