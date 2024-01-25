import os

from azure_verify import get_user_id
from azure_delete import delete_user

target_email = os.environ['Email']

env_file = open("temp_env.txt")
target_environment = env_file.read()
target_environment = target_environment.replace("\n","")

api_id_file = open("temp_id.txt")
api_id = api_id_file.read()
api_id = api_id.replace("\n","")

print(api_id)

tenant_id_lookup = {
	"Deltekcloud":"abf9f4cd-56cd-4d8a-9a02-7c288b91d9a5",
	"Conceptshare":"05142a66-17ef-42ce-9c1e-9690d507700d",
	"ITConceptshare":"44ecf5c5-5945-4f24-96ec-a73db8335538"
}

tenant_id = tenant_id_lookup[target_environment]

if '@' not in target_email or 'deltek.com' not in target_email:
	print("\n------------------------------------------\nERROR! Unexpected or malformed email format! Format should be <user>@deltek.com\n------------------------------------------\n")
	exit(0)


target_id = get_user_id(target_email, tenant_id)
if "match" not in target_id:
	print("\n--------------\nMATCH FOUND\n--------------\n")
	print(target_id)

	delete_response = delete_user(target_id, tenant_id)
	if delete_response.status_code==204:
		print("\n------------------------\nDELETION SUCCESSFUL\n------------------------\n")
else:
	print("\n--------------\nNO MATCH FOUND\n--------------\n")