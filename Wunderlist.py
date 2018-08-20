import json
import Config
import Auth

params = {}

def get(url, params = params):
	return Auth.wunderlist.get(url, params = params)

def post(url, json = params):
	return Auth.wunderlist.post(url, json = params)

def get_lists():
	res = get(Config.URL_LISTS)
	lists = json.loads(res.text)
	list_info = []
	for list in lists:
		list_info.append({list['id']: list['title']})
	return res.status_code, list_info

def create_task(params):
	res = post(Config.URL_TASKS, json = params)
	result = json.loads(res.text)
	task_info = {
		'id': result['id']
		,'created_at': result['created_at']
		,'created_by_id': result['created_by_id']
		,'completed': result['completed']
		,'starred': result['revision']
		,'list_id': result['list_id']
		,'revision': result['revision']
		,'title': result['title']
		,'type': result['type']
	}
	return res.status_code, task_info
