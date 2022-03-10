import requests
from bs4 import BeautifulSoup as bs

search = input('what you need to search for: ')
url = 'https://www.bing.com/?setlang=en/search'
param = {'q': search}
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36'}
req = requests.get(url, params= param, headers= header)

page = bs(req.text, 'html.parser')
result = page.find('ol', {'id':'b_results'})
links = result.findAll('li', {'class':'b_algo'})

linksList = []
print(len(links))

for item in links:
    name = item.find('a').text
    href = item.find('a').attrs['href']

    if name and href:

        linksList.append({'name': name, 'href': href})
        print(name, '\t', href)

