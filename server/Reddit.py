from config import *

reddit = praw.Reddit(
    client_id=os.getenv("reddit_client_id"),
    client_secret=os.getenv("reddit_client_secret"),
    user_agent=os.getenv("reddit_user_agent"),
    username=os.getenv("reddit_username"),
    password=os.getenv("reddit_pass")
)

############################# B I R D  F L U  N E W S ############################

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

############################# C L I M A T E  N E W S ############################
            
collpase_subreddit_climate = reddit.subreddit("collapse")

#get flair templates
flair_templates = collpase_subreddit_climate.flair.link_templates

# Separate posts by the "Climate" flair
flair_text = "Climate"

for post in collpase_subreddit_climate.new(limit=100): 
    if post.link_flair_text == flair_text:
        climate_title = post.title.replace("'", "").replace("[", "").replace("]", "").replace("(", "").replace(")", "")
        climate_url = post.url
        data = {
            'title': climate_title,
            'url': climate_url,
            'source': "Reddit",
            'category_id': 2
        }
        response, error = supabase.table('news_item').insert(data).execute()
        if error:
            print(f"Error inserting article: {error}")
        else:
            print(f"Inserted article: {climate_title}")
        print(data)
