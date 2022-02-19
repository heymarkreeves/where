from bs4 import BeautifulSoup
import json
import requests

exec(compile(source=open('db.py').read(), filename='db.py', mode='exec'))

select_trader_joes_query = "SELECT DISTINCT zipcode 'zipcode' FROM trader_joes"
with connection.cursor() as cursor:
    cursor.execute(select_trader_joes_query)
    result = cursor.fetchall()
    for row in result:
        bookstoresQueryData = {
            'search_for':row[0],
            'search_radius':'10',
            'op':'Search',
            'form_id':'indie_bookstore_finder_form'
        }
        bookstoresPage = requests.post(f"https://www.indiebound.org/indie-store-finder?q={row[0]}", bookstoresQueryData)

        soup = BeautifulSoup(bookstoresPage.content, 'html.parser')

        # <script type="application/json" data-drupal-selector="drupal-settings-json">
        bookstoresJson = soup.select_one('script[data-drupal-selector="drupal-settings-json"]').getText()

        bookstores = json.loads(bookstoresJson)

        if 'visible_markers' not in bookstores.keys():
            pass
        else:
            for bookstore in bookstores['visible_markers']:
                print(bookstore['marker_title'])
                print(bookstore['city'])
                print(bookstore['state'])
                print(bookstore['lat'])
                print(bookstore['lng'])

                insert_store_query = f"""
INSERT INTO bookstores (name, city, state, latitude, longitude)
VALUES
    ("{bookstore['marker_title']}", "{bookstore['city']}", "{bookstore['state']}", "{bookstore['lat']}", "{bookstore['lng']}")
ON DUPLICATE KEY UPDATE name="{bookstore['marker_title']}", city="{bookstore['city']}", state="{bookstore['state']}", latitude="{bookstore['lat']}", longitude="{bookstore['lng']}"
            """
                with connection.cursor() as cursor:
                    cursor.execute(insert_store_query)
                    connection.commit()