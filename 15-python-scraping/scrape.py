import requests
from bs4 import BeautifulSoup

# Page we are scraping
res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')

print(soup.select_one(".score"))

# .titlelink
