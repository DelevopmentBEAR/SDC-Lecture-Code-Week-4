import requests
from pprint import pprint

github_user_url = 'https://api.github.com/users/DelevopmentBEAR'

response = requests.get(github_user_url).json()
# pprint(response)

# {'avatar_url': 'https://avatars.githubusercontent.com/u/10088152?v=4',
#  'bio': None,
#  'blog': '',
#  'company': 'Minneapolis College',
#  'created_at': '2014-12-05T14:22:40Z',
#  'email': None,
#  'events_url': 'https://api.github.com/users/claraj/events{/privacy}',
#  'followers': 118,
#  'followers_url': 'https://api.github.com/users/claraj/followers',
#  'following': 0,
#  'following_url': 'https://api.github.com/users/claraj/following{/other_user}',
#  'gists_url': 'https://api.github.com/users/claraj/gists{/gist_id}',
#  'gravatar_id': '',
#  'hireable': None,
#  'html_url': 'https://github.com/claraj',
#  'id': 10088152,
#  'location': 'Minneapolis, MN',
#  'login': 'claraj',
#  'name': 'Clara',
#  'node_id': 'MDQ6VXNlcjEwMDg4MTUy',
#  'organizations_url': 'https://api.github.com/users/claraj/orgs',
#  'public_gists': 86,
#  'public_repos': 499,
#  'received_events_url': 'https://api.github.com/users/claraj/received_events',
#  'repos_url': 'https://api.github.com/users/claraj/repos',
#  'site_admin': False,
#  'starred_url': 'https://api.github.com/users/claraj/starred{/owner}{/repo}',
#  'subscriptions_url': 'https://api.github.com/users/claraj/subscriptions',
#  'twitter_username': None,
#  'type': 'User',
#  'updated_at': '2026-10-14T17:24:39Z',
#  'url': 'https://api.github.com/users/claraj',
#  'user_view_type': 'public'}

public_repo_count = response['public_repos']
print(f'User {response["login"]} has {public_repo_count} public repositories.') # User claraj has 499 public repositories.
print(type(public_repo_count))  # <class 'int'>