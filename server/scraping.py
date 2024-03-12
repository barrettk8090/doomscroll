from bs4 import BeautifulSoup
import requests
from supabase_py import create_client
import os 
from dotenv import load_dotenv
import json
import praw
import re 

#Get supabase
load_dotenv()
url = os.getenv('SUPABASE_URL')
key = os.getenv('ANON_KEY')
supabase = create_client(url, key)

############################# C L I M A T E  N E W S ############################

#NYTimes
nytimes_climate_url = "https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml"
nytimes_climate_result = requests.get(nytimes_climate_url)
nytimes_climate_doc = BeautifulSoup(nytimes_climate_result.text, features="lxml")

#Parse tags - NYTimes xml articles live inside item tags
item_tag = nytimes_climate_doc.find_all("item")

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

H5N1_subreddit = reddit.subreddit('H5N1_AvianFlu')

def reddit_to_supabase():
    for post in H5N1_subreddit.new(limit=10):
        bird_title = post.title
        bird_url = post.url
        data = {
            'title': bird_title,
            'url': bird_url,
            'source': "Reddit",
            'category_id': 1
        }
        response, error = supabase.table('news_item').insert(data).execute()
        if error:
            print(f"Error inserting article: {error}")
        else:
            print(f"Inserted article: {bird_url}")

# reddit_to_supabase()

#################### E A R T H Q U A K E S ####################
            
earthquakes_gov_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.atom"

earthquakes_gov_result = requests.get(earthquakes_gov_url)
earthquakes_gov_doc = BeautifulSoup(earthquakes_gov_result.text, features="lxml")

# print(earthquakes_gov_doc.prettify())
entry = earthquakes_gov_doc.find_all("entry")


def earthquakes_gov_to_supabase():
    for earthquake in entry:
        title_text = earthquake.find('title').string
        pattern = r'M\s*(\d+\.\d+)\s*-\s*(.+)'
        match = re.search(pattern, title_text)

        if match:
            # Extract magnitude and location
            earthquake_magnitude = match.group(1)
            earthquake_location = match.group(2).strip()

            earthquake_depth = (earthquake.find('dd')).string
            link = earthquake.find('link')
            earthquake_url = (link['href'])
            data = {
                'title': (f"Earthquake!  Magnitude: {earthquake_magnitude}  | Location:  {earthquake_location}  | Depth:  {earthquake_depth}."),
                'url': earthquake_url,
                'source': 'USGS',
                'category': 8
            }
            response, error = supabase.table('news_item').insert(data).execute()
            if error:
                print(f"Error inserting earthquake: {error}")
            else:
                print(f"Inserted earthquake from: {earthquake_location}")

earthquakes_gov_to_supabase()