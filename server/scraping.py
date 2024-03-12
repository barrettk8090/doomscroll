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
def nytimes_to_supabase():
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

# nytimes_to_supabase()

############################# B I R D  F L U  N E W S ############################

reddit = praw.Reddit(
    client_id=os.getenv("reddit_client_id"),
    client_secret=os.getenv("reddit_client_secret"),
    user_agent=os.getenv("reddit_user_agent"),
    username=os.getenv("reddit_username"),
    password=os.getenv("reddit_pass")
)

subreddit = reddit.subreddit('H5N1_AvianFlu')

def reddit_to_supabase():
    for post in subreddit.new(limit=10):
        bird_title = post.title
        bird_url = post.url
        data = {
            'title': bird_title,
            'url': bird_url,
            'source': "Reddit",
            'category_id': 1
        }
        # Check if the post URL already exists in the database
        existing_entry = supabase.table('news_item').select('*').eq('url', bird_url).execute()
        if existing_entry['status_code'] == 200 and not existing_entry['data']:
            # This runs for all new URLs not already in db
            response, error = supabase.table('news_item').insert(data).execute()
            if error:
                print(f"Error inserting article: {error}")
            else:
                print(f"Inserted article: {bird_url}")
        elif existing_entry['status_code'] == 200:
            print(f"Article with URL {bird_url} already exists.")
        else:
            print(f"Error checking for existing article: {existing_entry['status_code']}")

reddit_to_supabase()

