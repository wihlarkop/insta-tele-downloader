import requests
from instagram import get_images

url = 'https://www.instagram.com/p/CDJhhC5BrMwra32gbrpblGUKgKsGaFZeZXzpdQ0/?__a=1'

print(get_images(url))