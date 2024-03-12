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

