import configparser

PROPERTY_FILE = 'Wunderlist_auth.properties'
PROPERTY_FILE = 'Wunderlist.properties'
conf = configparser.SafeConfigParser()
conf.read(PROPERTY_FILE)

if __name__ == '__main__':
    for section in conf.sections():
        print('[' + section + ']')
        for key in conf.options(section):
            print(conf.get(section, key))

CLIENT_ID = conf.get('AUTH_INFO', 'client_id')
ACCESS_TOKEN = conf.get('AUTH_INFO', 'access_token')
