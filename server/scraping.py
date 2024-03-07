from bs4 import BeautifulSoup
import requests
from supabase_py import create_client
import os 
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('SUPABASE_URL')
key = os.getenv('ANON_KEY')
supabase = create_client(url, key)

#Get Climate News 
nytimes_climate = "https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml"

#NYTIMES CLIMATE - get xml document and save to variable
result = requests.get(nytimes_climate)
doc = BeautifulSoup(result.text, features="xml")

#Parse tags 
item_tag = doc.find_all("item")

for article_details in item_tag:
    climate_title = (article_details.find("title")).string
    climate_source = "NYTimes"
    climate_url = (article_details.find("link")).string
    climate_category = (article_details.find("category")).string
    # Need to add logic "and this article isn't already in supabase..."
    if climate_category == "Global Warming" and climate_category != "United States Politics and Government":
        data = {
            'title': climate_title,
            'url': climate_url,
            'source': climate_source,
            'category_id': 4
        }
        response = supabase.table('news_item').insert(data)
        # if error:
        #     print(f"Error inserting article: {error}")
        # else:
        #     print(f"Inserted article: {climate_title}")


title = doc.find_all("title")
category = doc.find_all("Global Warming")
# climate = doc.find_all(string="climate")

# for text in title:
#     if ">" not in text.string and "Climate" in text.string:
#         print(text.string)

# Status - we're getting titles of articles that contain climate
# Instead we'll want to filter by category tags - e.g. Global Warming
# As we're looping through we want to add each one to supabase
#   making sure it has a "source", and "url" 

def post_to_supabase():
    pass