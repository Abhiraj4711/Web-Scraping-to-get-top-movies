# Import necessary libraries
import requests 
# This will help in sending requests to webpage
from bs4 import BeautifulSoup
# This will help in parsing the contents of our webpage in html to something from where we can scrape output
import datetime
# This is to make sure input is valid

# Step 1: take input of year
year=input("Enter year from which you want top 10: IMDB movies:(year must be between 1950 and current year): ")
# Step 2: make sure that input is valid
if(int(datetime.datetime.now().year)>=int(year) and int(year)>=1950):
    # Step 3 : Fetch the webpage
    url = "https://www.imdb.com/search/title/?title_type=feature&release_date="+year+"-01-01,"+year+"-12-31"
    headers = {"User-Agent": "Mozilla/5.0"}  # This will prevent bot detection
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser") # parse it into soup format

    li_tags = soup.find_all("li", class_="ipc-metadata-list-summary-item", limit=10)  
    # Here we find the top 10 movies, if we set the limit to a higher number, we will get more movies

    if not li_tags:
        print("No <li> elements found. The class name might have changed or the page is dynamic.")
        
    for i, li in enumerate(li_tags, start=1):
        h_tag = li.find("h3", class_="ipc-title__text")
        if h_tag:
            text = h_tag.get_text(strip=True)
            print(f"{text}")
        else:
            print(f"{i}. No <h> tag found in this <li>.")
else:
    print("Invalid date mentioned")
