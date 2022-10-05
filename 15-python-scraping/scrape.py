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

# Sort stories by votes


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


# Function for displaying the scraped data

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        # TODO: Fix link not working, issue with getting correct selector
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))
