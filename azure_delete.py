import requests

def delete_user(user_id, tenant_id, api_id, api_secret):

	data = {
	"scope":"https://graph.microsoft.com/.default",
	"grant_type":"client_credentials",
	"client_id":api_id,
	"client_secret":api_secret
	}

	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	response = requests.post(f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token", headers=headers, data=data)
	bearer_token = response.json()['access_token']

	headers = {'Authorization': f'Bearer {bearer_token}'}
	response = requests.delete(f"https://graph.microsoft.com/v1.0/users/{user_id}", headers=headers)

	return(response)