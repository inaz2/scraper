from scraper import scraper
import re

def handler(url, status_code, data):
    if status_code == 200:
        urls = re.findall(r'href="([^"]+)"', data)
        print urls

urls = ['http://www.example.com']
scraper(urls, handler)
