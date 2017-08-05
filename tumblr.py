import requests
import time
import urllib
from bs4 import BeautifulSoup

key = lambda x: x and x.startswith('photo reblogged') 
#key = lambda x: x and x.startswith('photoset ')
#key = lambda x: x and x.startswith('photo ')

url = 'https://ailikee.tumblr.com'
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,"html.parser")
posts = soup.find_all('article', { 'class' : key})
#posts = soup.find_all('article')


for _ in posts:
    content = _.find_all('section', {'class' : 'post'})

for _ in posts:
    for i in _.find_all('a'):
        if i.img and 'post-avatar-image' not in str(i.img):
            print(i.img['src'])

print(len(posts))

