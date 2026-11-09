import requests

response = requests.get('https://yesno.wtf/api').json()
print(response)