import requests
from bs4 import BeautifulSoup

# Page we are scraping
res = requests.get('https://news.ycombinator.com/news')

# Create soup object and parse it
soup = BeautifulSoup(res.text, 'html.parser')

# Grab all links with title class
links = soup.select(".title a")

# Grab all votes items with score class
votes = soup.select(".score")

# Function for displaying the scraped data


def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        hn.append({'title': title, 'link': href})
    return hn


print(create_custom_hn(links, votes))
