from config import *

############################# C L I M A T E  N E W S ############################

#NYTimes
nytimes_climate_url = "https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml"
nytimes_climate_result = requests.get(nytimes_climate_url)
nytimes_climate_doc = BeautifulSoup(nytimes_climate_result.text, features="xml")

#Parse tags - NYTimes xml articles live inside item tags
item_tag = nytimes_climate_doc.find_all("item")

#Loop through each article and extract details, save to db
def nytimes_to_supabase():
    for article_details in item_tag:
        climate_title = (article_details.find("title")).string
        climate_source = "NYTimes"
        climate_url = (article_details.find("link")).string
        climate_category = (article_details.find_all("category"))
        all_cats = []
        for cat in climate_category:
            all_cats.append(cat.string)
        if "Global Warming" in all_cats and "United States Politics and Government" not in all_cats:
            data = {
                'title': climate_title,
                'url': climate_url,
                'source': climate_source,
                'category_id': 4
            }
            response, error = supabase.table('news_item').insert(data).execute()
            if error:
                print(f"Error inserting article: {error}")
            else:
                print(f"Inserted article: {climate_title}")

nytimes_to_supabase()