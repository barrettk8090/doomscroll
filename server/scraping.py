from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/2024/01/30/science/antarctica-bird-flu-penguins.html"

proxy_addresses = {
    'http': 'http://72.206.181.123:4145',
    'https': 'http://191.96.100.33:3128'
}

result = requests.get(url, proxies=proxy_addresses)
print(result)