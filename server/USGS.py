from config import *

earthquakes_gov_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.atom"

earthquakes_gov_result = requests.get(earthquakes_gov_url)
earthquakes_gov_doc = BeautifulSoup(earthquakes_gov_result.text, features="xml")

# print(earthquakes_gov_doc.prettify())
entry = earthquakes_gov_doc.find_all("entry")

# Current Status - Successfully posts to supabase, but error status code still gets printed
def earthquakes_gov_to_supabase():
    for earthquake in entry:
        title_text = earthquake.find('title').string
        # use reg ex to separate out magnitude and location
        pattern = r'M\s*(\d+\.\d+)\s*-\s*(.+)'
        match = re.search(pattern, title_text)

        if match:
            # Extract magnitude and location
            earthquake_magnitude = match.group(1)
            earthquake_location = match.group(2).strip()
            earthquake_depth = ""
            # depth is located inside the SECOND <dd> tag
            dd_tags = earthquake.find_all('dd')
            if len(dd_tags) > 1:
                earthquake_depth = dd_tags[1].string
            # find link tag then pull from href for url
            link = earthquake.find('link')
            earthquake_url = (link['href'])
            data = {
                'title': (f"Earthquake!  Magnitude: {earthquake_magnitude}  | Location:  {earthquake_location}  | Depth:  {earthquake_depth}."),
                'url': earthquake_url,
                'source': 'USGS',
                'category_id': 8
            }
            response = supabase.table('news_item').insert(data).execute()
            print(response)
            print(f"Inserted earthquake from: {earthquake_location}")


earthquakes_gov_to_supabase()