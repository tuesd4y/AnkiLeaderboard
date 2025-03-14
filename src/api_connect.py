import json
import requests
from aqt.utils import showWarning
import os

def get_api_base():
	api_base =  os.environ.get('LEADERBOARD_API_BASE')
	if api_base is None:
		# todo
		api_base = 'https://ankileaderboard.pythonanywhere.com'

	return api_base


def get_api_endpoint(endpoint):
	url = f"{get_api_base()}/api/v2/{endpoint}"
	return url


def postRequest(endpoint, data, statusCode, warning=True):
	url = get_api_endpoint(endpoint)
	try:
		response = requests.post(url, data=data, timeout=15)

		if response.status_code == statusCode:
			return response
		else:
			if warning:
				showWarning(str(response.text))
				return False
			else:
				return response
	except Exception as e:
		errormsg = f"Timeout error [{url}] - No internet connection, or server response took too long. \n\n{str(e)}"
		if warning:
			showWarning(errormsg, title="Leaderboard Error")
			return False
		else:
			return errormsg


def getRequest(endpoint):
	url = get_api_endpoint(endpoint)

	try:
		response = requests.get(url, timeout=15)

		if response.status_code == 200:
			return response
		else:
			showWarning(str(response.text))
			return False
	except Exception as e:
		showWarning(f"Timeout error [{url}] - No internet connection, or server response took too long. \n\n{str(e)}",
					title="Leaderboard Error")
		return False
