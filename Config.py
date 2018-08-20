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

URL_LISTS = conf.get('URL', 'url_lists')
URL_TASKS = conf.get('URL', 'url_tasks')
URL_TASKS_COMMENTS = conf.get('URL', 'url_task_comments')
URL_SUBTASKS = conf.get('URL', 'url_subtasks')
URL_NOTES = conf.get('URL', 'url_notes')
URL_REMINDERS = conf.get('URL', 'url_reminders')
URL_FOLDERS = conf.get('URL', 'url_folders')
URL_FOLDERS_ID = conf.get('URL', 'url_folders_id')
URL_FOLDERS_REV = conf.get('URL', 'url_folder_revs')