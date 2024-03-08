from bs4 import BeautifulSoup
import requests
from supabase_py import create_client
import os 
from dotenv import load_dotenv
import json
import praw

#Get supabase
load_dotenv()
url = os.getenv('SUPABASE_URL')
key = os.getenv('ANON_KEY')
supabase = create_client(url, key)

############################# C L I M A T E  N E W S ############################

#NYTimes
nytimes_climate_url = "https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml"
result = requests.get(nytimes_climate_url)
doc = BeautifulSoup(result.text, features="lxml")

#Parse tags - NYTimes xml articles live inside item tags
item_tag = doc.find_all("item")

#Loop through each article and extract details, save to db
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

############################# B I R D  F L U  N E W S ############################

bf_subreddit_url = "https://www.reddit.com/r/h5N1_AvianFlu/.json"
result2 = requests.get(bf_subreddit_url)
doc2 = json.loads(result2.text)
print(doc2)
