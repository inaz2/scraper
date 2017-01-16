from scraper import scraper
import re

def handler(url, data):
    urls = re.findall(r'href="([^"]+)"', data)
    print urls

urls = ['http://www.example.com']
scraper(urls, handler)
