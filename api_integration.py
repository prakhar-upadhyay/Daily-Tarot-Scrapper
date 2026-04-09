import requests
import csv
from datetime import datetime

url="https://tarotapi.dev/api/v1/cards/random?n=3"
response = requests.get(url)

data = response.json()
cards = data['cards']

with open('data_log.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    for card in cards:
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
            card['name'], 
            card['type'], 
            card['meaning_up']
        ])

print('API data successfully retrieved & logged !')