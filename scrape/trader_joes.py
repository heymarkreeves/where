from bs4 import BeautifulSoup
# import json
import requests

exec(compile(source=open('db.py').read(), filename='db.py', mode='exec'))

# 1. Loop through state links: https://locations.traderjoes.com/
states_page = requests.get('https://locations.traderjoes.com/')

soup = BeautifulSoup(states_page.content, 'html.parser')

# there are some data attributes here, too, ex: data-galoc
for state in soup.find_all('a', class_='listitem'):

    # 2. Loop through city links
    cities_page = requests.get(state['href'])

    soup = BeautifulSoup(cities_page.content, 'html.parser')

    for city in soup.find_all('a', class_='listitem'):

        # 3. Loop through locations
        locations_page = requests.get(city['href'])

        soup = BeautifulSoup(locations_page.content, 'html.parser')

        for location in soup.find_all('a', class_='listitem'):

            # 4. Get location details
            location = requests.get(location['href'])

            soup = BeautifulSoup(location.content, 'html.parser')

            latitude = soup.select_one('meta[property="place:location:latitude"]')['content']
            longitude = soup.select_one('meta[property="place:location:longitude"]')['content']
            title = soup.select_one('meta[property="og:title"]')['content']
            address = soup.select_one('meta[property="business:contact_data:street_address"]')['content']
            zipcode = soup.select_one('meta[property="business:contact_data:postal_code"]')['content']

            print(latitude)
            print(longitude)
            print(title)
            print(zipcode)

            insert_store_query = f"""
INSERT INTO trader_joes (name, address, zipcode, latitude, longitude)
VALUES
    ("{title}", "{address}", "{zipcode}", "{latitude}", "{longitude}")
ON DUPLICATE KEY UPDATE name="{title}", address="{address}", zipcode="{zipcode}", latitude="{latitude}", longitude="{longitude}"
"""
            with connection.cursor() as cursor:
                cursor.execute(insert_store_query)
                connection.commit()