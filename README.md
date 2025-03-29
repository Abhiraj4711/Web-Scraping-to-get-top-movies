# Web-Scraping-to-get-top-movies
I have used python web scraping to get the top 10 movies from the year that user specifies. 

# Learning outcomes:
To get html code of any websitewe have to use the request library. 

Some websites use auto bot detection. This works by detecting the user agent of the bot that is trying to scrape/access the website. It also check the ip address of requests. if requests from 1 IP are too frequent it sends a captcha to check if its a bot or human trying to access the data.

If the user agent is unspecified or is of type python-request, it catches our bot. That's why we need to use the code line headers = {"User-Agent": "Mozilla/5.0"} to bypass this detection. 

The actual HTML code can be huge and finding the required part means a dive into a rabbithole. Manually this is easy as we can verify each part of the code by the part of website it highlights.

 In our code we can bypass this whole check by cleverly looking for tags and their class_ attributes (which will specify the tags) and then narrowing our search in these specific tags. That's what i have done, by just finding the \<li\> tags and the \<h3\> tags, both of these are multiple layers deep in the html file, but due to the different class_ attribute, we can quickly fetch them.

# How It Works
The script prompts the user to enter a year.
It then sends a request to IMDb to fetch movie data.
Using BeautifulSoup, it parses the HTML and extracts the top 10 movie titles.
The results are displayed on the screen.
