import requests

def get_user_id(target_email, tenant_id, api_id, api_secret):

	data = {
	"scope":"https://graph.microsoft.com/.default",
	"grant_type":"client_credentials",
	"client_id":api_id,
	"client_secret":api_secret
	}

	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	response = requests.post(f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token", headers=headers, data=data)
	print(response)
	bearer_token = response.json()['access_token']

	cont = True
	full_user_list = []
	target_query_url = "https://graph.microsoft.com/v1.0/users"
	headers = {'Authorization': f'Bearer {bearer_token}'}

	while cont:

		response = requests.get(target_query_url, headers=headers).json()

		if "@odata.nextLink" in response.keys():
			target_query_url = response['@odata.nextLink']
		else:
			cont = False

		full_user_list.extend(response['value'])

	for item in full_user_list:
		if item['mail']:
			if target_email in item['mail'].lower():
				return(item['id'])

	return('No match found')