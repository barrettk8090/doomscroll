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
    if climate_category == "Global Warming" and climate_category != "United States Politics and Government":
        data = {
            'title': climate_title,
            'url': climate_url,
            'source': climate_source,
            'category_id': 4
        }
        # Check to make sure that an article doesnt already exist in supabase
        existing_articles, error = supabase.table('news_item').select('title').filter('title', 'eq', climate_title).execute()
        if error:
            print(f"Error checking for existing article: {error}")
        elif existing_articles:
            print(f"Article with title {climate_title} already exists")
        else:
            response, error = supabase.table('news_item').insert(data).execute()
            if error:
                print(f"Error inserting article: {error}")
            else:
                print(f"Inserted article: {climate_title}")

def post_to_supabase():
    pass