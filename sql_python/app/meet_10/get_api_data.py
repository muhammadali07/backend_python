import requests

api = 'https://corona.lmao.ninja/v2/continents?yesterday=true&sort'
response = requests.get(api)
print(response)
print(response.status_code)
print(response.text)

