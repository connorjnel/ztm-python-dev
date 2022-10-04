import requests
from bs4 import BeautifulSoup
import pprint

# Page we are scraping
res = requests.get('https://news.ycombinator.com/news')

# Create soup object and parse it
soup = BeautifulSoup(res.text, 'html.parser')

# Grab all links with title class
links = soup.select('.titleline')

# Grab all votes items with score class
subtext = soup.select('.subtext')


# Function for displaying the scraped data
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn


pprint.pprint(create_custom_hn(links, subtext))
