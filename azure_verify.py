import requests

target_email = "johnvincentagbayani@deltek.com"
tenant_id = "abf9f4cd-56cd-4d8a-9a02-7c288b91d9a5"

data = {
"scope":"https://graph.microsoft.com/.default",
"grant_type":"client_credentials",
"client_id":"d26bf6c6-0dd3-4291-8d82-86ff18044322",
"client_secret":"U0E8Q~EhDDUEBQBvLpZc_YCcX6KLgGHY~H24Qb2Q"
}

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post(f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token", headers=headers, data=data)
bearer_token = response.json()['access_token']

headers = {'Authorization': f'Bearer {bearer_token}'}
response = requests.get("https://graph.microsoft.com/v1.0/users", headers=headers).json()

for item in response['value']:
	if item['mail']:
		if target_email in item['mail'].lower():
			print(item)
			with open("deletion_source.txt", "w") as source_file:
			    source_file.write(item['id'])