import requests

api_key = '1517c5d2-e198-4456-98ae-6867d43b0c4a'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()



for definition in definitions:
    print(definition)