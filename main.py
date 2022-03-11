import os, requests
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv('BEARER_TOKEN')

headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
}
data = requests.get(f'https://api.twitter.com/2/users/1453616508035272705/tweets?max_results=5&expansions=attachments.media_keys&media.fields=preview_image_url', headers=headers) # https://tweeterid.com/
print(data.text)