import urllib2
import time

def scraper(urls, handler, interval=2, ua=None, referer=None):
    headers = {}
    if ua:
        headers['User-Agent'] = ua
    if referer:
        headers['Referer'] = referer

    for url in urls:
        req = urllib2.Request(url, headers=headers)
        f = urllib2.urlopen(req)
        data = f.read()
        f.close()
        handler(url, data)
        time.sleep(interval)
