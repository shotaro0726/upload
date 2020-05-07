from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os
import time
import sys

key = 'c6067534174988a296d62d006778d8ad'
secret = '934254040f913443'
wait_time = 1

keyword = sys.argv[1]
savedir = "./" + keyword

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text=keyword,
    per_page=400,
    media='photos',
    sort='relevance',
    sefe_search=0,
    extras='url_q, license',
)

photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath):
        continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
