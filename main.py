import os

from azure_verify import get_user_id
from azure_delete import delete_user

target_email = os.environ['Email']
tenant_id = "abf9f4cd-56cd-4d8a-9a02-7c288b91d9a5"

if '@' not in target_email or 'deltek.com' not in target_email:
	print("--------------\nERROR! Unexpected or malformed email format! Format should be <user>@deltek.com\n--------------\n")


target_id = get_user_id(target_email, tenant_id)
if "match" not in target_id:
	print("--------------\nMATCH FOUND\n--------------\n")
	print(target_id)

	delete_response = delete_user(target_id, tenant_id)
	if delete_response.status_code==204:
		print("------------------------\nDELETION SUCCESSFUL\n------------------------\n")
else:
	print("--------------\nNO MATCH FOUND\n--------------\n")