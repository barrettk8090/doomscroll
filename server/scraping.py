from bs4 import BeautifulSoup
import requests
from supabase_py import create_client
import os 

url = os.getenv('VITE_SUPABASE_URL')
key = os.getenv('VITE_ANON_KEY')
supabase = create_client(url, key)

nytimes_climate = "https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml"

result = requests.get(nytimes_climate)
doc = BeautifulSoup(result.text, features="xml")
title = doc.find_all("title")
# climate = doc.find_all(string="climate")

for text in title:
    if ">" not in text.string and "Climate" in text.string:
        print(text.string)

# Status - we're getting titles of articles that contain climate
# Instead we'll want to filter by category tags - e.g. Global Warming
# As we're looping through we want to add each one to supabase
#   making sure it has a "source", and "url" 

def post_to_supabase():
    pass