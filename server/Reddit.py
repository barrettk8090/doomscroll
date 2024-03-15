from config import *

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

reddit_to_supabase()

### CLIMATE NEWS #### 
            
# need to check for how to filter by flair 
climate_subreddit = reddit.subreddit("https://www.reddit.com/r/collapse/new/?f=flair_name%3A%22Climate%22")