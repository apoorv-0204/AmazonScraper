from bs4  import BeautifulSoup
search = 'guitar'
url = 'https://www.walmart.com/search/?query='+search


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

main=soup.select('.product-title-link')[0].attrs['href']


newURL='https://www.walmart.com'+main
req = urllib.request.Request(
    newURL, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')
print(soup.select('.prod-ProductTitle')[0].attrs['content'])
print(soup.select('.price-characteristic')[0].attrs['content'])