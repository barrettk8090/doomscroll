from config import *

reddit = praw.Reddit(
    client_id=os.getenv("reddit_client_id"),
    client_secret=os.getenv("reddit_client_secret"),
    user_agent=os.getenv("reddit_user_agent"),
    username=os.getenv("reddit_username"),
    password=os.getenv("reddit_pass")
)

############################# C A T E G O R Y  1 ############################
############################# B I R D  F L U  N E W S ############################

H5N1_subreddit = reddit.subreddit('H5N1_AvianFlu')

def reddit_H5N1_to_supabase():
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

# reddit_H5N1_to_supabase()

############################# C A T E G O R Y  2 ############################
############################# C L I M A T E  N E W S ############################
            
collapse_subreddit_climate = reddit.subreddit("collapse")
#get flair templates
flair_templates = collapse_subreddit_climate.flair.link_templates
# Separate posts by the "Climate" flair
flair_text_climate = "Climate"

def reddit_climate_to_supabase():
    for post in collapse_subreddit_climate.new(limit=100): 
        if post.link_flair_text == flair_text_climate:
            # Strip out extraneous characters from titles
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

# reddit_climate_to_supabase()
                
############################# C A T E G O R Y  3 ############################
############################# C O R O N A V I R U S  N E W S ############################

flair_text_covid = "COVID-19"

def reddit_covid_to_supabase():
    for post in collapse_subreddit_climate.new(limit=100): 
            if post.link_flair_text == flair_text_covid:
                covid_title = post.title.replace("'", "").replace("[", "").replace("]", "").replace("(", "").replace(")", "")
                covid_url = post.url
                data = {
                    'title': covid_title,
                    'url': covid_url,
                    'source': "Reddit", 
                    'category_id': 3
                }
                response, error = supabase.table('news_item').insert(data).execute()
                if error:
                    print(f"Error inserting article: {error}")
                else:
                    print(f"Inserted article: {covid_title}")
# reddit_covid_to_supabase()

############################# C A T E G O R Y  4 ############################
############################# A R T I F I C I A L  I N T E L L I G E N C E  N E W S ############################

artificial_subreddit = reddit.subreddit("artificial")
flair_text_ai_news = "News"

def reddit_ai_to_supabase():
    for post in artificial_subreddit.new(limit=100):
        if post.link_flair_text == flair_text_ai_news:
            ai_title = post.title.replace("'", "").replace("[", "").replace("]", "").replace("(", "").replace(")", "")
            ai_url = post.url
            data = {
                'title': ai_title,
                'url': ai_url,
                'source': "Reddit",
                'category_id': 4 
            }
            response, error = supabase.table('news_item').insert(data).execute()
            if error:
                    print(f"Error inserting article: {error}")
            else:
                    print(f"Inserted article: {ai_title}")
reddit_ai_to_supabase()


############################# C A T E G O R Y  5 ############################
############################# U F O  N E W S ############################

############################# C A T E G O R Y  6 ############################
############################# S O L A R  A C T I V I T Y  N E W S ############################

############################# C A T E G O R Y  7 ############################
############################# H U R R I C A N E  N E W S ############################

############################# C A T E G O R Y  8 ############################
############################# E A R T H Q U A K E  N E W S ############################

############################# C A T E G O R Y  9 ############################
############################# C Y B E R  A T T A C K  N E W S ############################