import uuid
import urllib.request
import urllib.parse
import pandas as pd

root = 'Resilience in computer systems and networks'
depth = 3

url = 'https://serpapi.com/search'
args = {
    'engine': 'google_scholar',
    'q': root,
    'hl': 'en'
}
arg_string = urllib.parse.urlencode(args)
full_url = f'{url}?{arg_string}'
f = urllib.request.urlopen(full_url)
print(f.read().decode('utf-8'))