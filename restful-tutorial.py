import requests
from requests.exceptions import HTTPError

"""
requests.get('http://192.168.16.89')
print(requests.get('http://192.168.16.89'))
response = requests.get('https://api.github.com')
print(response.status_code)

if response.status_code == 200:
    print('Success! Web found')
elif response.status_code == 404:
    print('Not Found.')

if response:
    print('Success!')
else:
    print('An error has occurred.')
"""
#######
"""
for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
    except Exception as err:
        print(f'Other error occured: {err}')
    else:
        print('Success!')
"""
"""
response = requests.get("https://api.github.com")
response.encoding = 'utf-8'
print(response.content)
print(response.text)
print(response.json())
print(response.headers)
print(response.headers['content-type'])
"""
"""
for response in [requests.get('https://api.github.com/search/repositories', params={'q': 'requests+language:python'}), requests.get('https://api.github.com/search/repositories', params=[('q', 'requests+language:python')]) ]:

    json_response = response.json()
    repository = json_response['items'][0]
    print(f'Response name: {repository["name"]}')
    print(f'Repository description: {repository["description"]}')
"""
"""
response = requests.get('http://api.github.com/search/repositories', params={'q': 'requests+language:python'},headers={'Accept': "application/vnd.github.v3.text-match+json"})

json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')

requests.post('https://httpbin.org/post', data={'key':'value'})
requests.put('https://httpbin.org/put', data={'key':'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key':'value'})
requests.options('https://httpbin.org/get')
"""
response = requests.head('https://httpbin.org/get')
response.headers['Content-type']

response = requests.delete('https://httpbin.org/delete')
json_response = response.json()
json_response['args']