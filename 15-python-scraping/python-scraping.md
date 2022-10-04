# Python Scraping

- Using python to grab data from website and using it
- Use schema to only grab information you want
- `robots.txt` - shows which data you are allowed to scrape
- `crawl-delay` - interval while crawling

## Ethical scraping

- Check robots.txt for what you can scrape
- Check and implement crawl delay to not overtax server
- Do not use scraped data for commercial applications without explicit permission

## Crawler

- A Web crawler, sometimes called a spider or spiderbot and often shortened to crawler, is an Internet bot that systematically browses the World Wide Web and that is typically operated by search engines for the purpose of Web indexing (web spidering).
- Googlebot, bing, baidu etc

## Hacker News Scraper Project

- Build with beautiful soup library
- `pip install beautifulsoup4` - default install
- Use requests library for http requests
- `from bs4 import BeautifulSoup` - import beatifulsoup
- `res = requests.get("url")` - set page being scraped
- use bs4 to convert text to object
- `soup = BeautifulSoup(res.text, 'html.parser')` - default way to parse response using bs4
- `soup.find_all('a')` - find all links, can use for html
- `soup.find('a')` - find first link, can use for html
- `soup.select('.class')` - find all css class, use dot notation
- `soup.select_one('.class')` - find first css class, use dot notation
- `soup.select('#id')` - find all id, use pound notation
- debug - index out of range could be because one enumerable didnt have a corresponding value
