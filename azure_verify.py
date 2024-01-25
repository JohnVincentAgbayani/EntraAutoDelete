import requests

def get_user_id(target_email, tenant_id):

	data = {
	"scope":"https://graph.microsoft.com/.default",
	"grant_type":"client_credentials",
	"client_id":"d26bf6c6-0dd3-4291-8d82-86ff18044322",
	"client_secret":"U0E8Q~EhDDUEBQBvLpZc_YCcX6KLgGHY~H24Qb2Q"
	}

	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	response = requests.post(f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token", headers=headers, data=data)
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