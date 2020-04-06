import urllib.request
import json
import pprint

APIKEY = 'f46ba088596e76092810c544ab52fa27'
city = 'Wellesley'
country_code = 'us'
url = 'http://api.openweathermap.org/data/2.5/weather?q=Wellesley,us&APPID=f46ba088596e76092810c544ab52fa27'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint.pprint(response_data)

# Can you get the current temperature in Wellesley?

pprint.pprint(response_data['main']['temp'])
