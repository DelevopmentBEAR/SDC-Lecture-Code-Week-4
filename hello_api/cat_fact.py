import requests 

try:
    response = requests.get('https://catfact.ninja/fact').json()
    print(response.status_code) 

    response.raise_for_status()  # Raise an exception if the request was unsuccessful aka 400 or 500 error
    print(response.text)
    print(response.json())

    data = response.json()
    fact = data['fact']
    print(f'Here is a random cat fact: {fact}')

except Exception as e:
    print(f'An error occurred: {e}')