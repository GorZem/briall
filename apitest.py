import requests

r = requests.get("https://reqres.in/api/users?per_page=12").json()
print(r)