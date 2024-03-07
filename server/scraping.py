from bs4 import BeautifulSoup
import requests

nytimes_climate = "https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml"

proxy_addresses = {
    'http': 'http://72.206.181.123:4145',
    'https': 'http://191.96.100.33:3128'
}

result = requests.get(nytimes_climate)
print(result)