import requests
import json


url= 'https://domain.com/wp-content/uploads/2023/04/image.jpg'

r = requests.get('https://domain.com/wp-json/wp/v2/media')
event = r.json()

def find_id(m_url):
    for i in event:
        if i['guid']['rendered'] == m_url:
            return (i['id'])
        
print(find_id(url))
