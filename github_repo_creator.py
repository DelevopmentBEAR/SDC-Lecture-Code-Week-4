import os
import requests
import webbrowser

GITHUB_API_TOKEN = os.environ.get('GITHUB_API_TOKEN')

base_url = 'https://api.github.com'
path = '/user/repos'
url = base_url + path

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {GITHUB_API_TOKEN}',
    'X-GitHub-Api-Version': '2026-03-10'
}

body = {
    'name': 'new-repo',
}

response = requests.post(url, headers=headers, json=body)
new_repo_response = response.json()
status_code = response.status_code

#print(new_repo_response)
#print(status_code)

if status_code == 201:
    print(f"Repository '{new_repo_response['name']}' created successfully.")
    webbrowser.open(new_repo_response['html_url'])
else:
    print(f"Failed to create repository. Status code: {status_code}")
    print(f"Response: {new_repo_response}")