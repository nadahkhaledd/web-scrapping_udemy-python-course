import requests
from bs4 import BeautifulSoup as bs
from PIL import Image
from io import BytesIO
import os
import json

search = input('what you need to search for: ')
folder = search.replace(' ', '-').lower()
if not os.path.isdir(folder):
    os.makedirs(folder)

url = 'https://www.bing.com/images/search'
param = {'q': search}
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36'}
req = requests.get(url, params= param, headers= header)

page = bs(req.text, 'html.parser')
result = page.findAll('a', {'class':'iusc'})

for item in result:
    try:
        pic = requests.get(json.loads(item.attrs['m'])['murl'])
        name = json.loads(item.attrs['m'])['murl'].split('/')[-1]
        try:
            img = Image.open(BytesIO(pic.content))
            img.save('./'+folder+'/' + name, img.format)
            print('saving  ', json.loads(item.attrs['m'])['murl'])
        except:
            print("couldn't save")
    except:
        print('image not available')




