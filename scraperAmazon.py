from bs4  import BeautifulSoup
search = 'guitar'
url = 'https://www.amazon.com/s?k='+search+'&ref=nb_sb_noss_2'

import urllib.request
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')
print(soup.findAll({"class":'a-link-normal'}))


