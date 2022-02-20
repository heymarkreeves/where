import json
import requests
from throttler import ExecutionTimer
from urllib.parse import urlencode, quote_plus

exec(compile(source=open('db.py').read(), filename='db.py', mode='exec'))

select_trader_joes_query = f"""
SELECT
city, state, latitude, longitude FROM bookstores
WHERE state in ('ME', 'NH', 'VT', 'MA', 'RI', 'CT', 'NY', 'NJ', 'PA', 'DE', 'MD', 'WV', 'VA', 'NC', 'SC', 'GA', 'NM', 'UT', 'AZ', 'TX', 'OH', 'IL', 'IN', 'KY', 'TN')
LIMIT 0, 2000
    """
batch = ExecutionTimer(10, align_sleep=True)
with batch:
    with connection.cursor() as cursor:
        cursor.execute(select_trader_joes_query)
        result = cursor.fetchall()
        et = ExecutionTimer(6, align_sleep=True)
        for row in result:
            with et:
                # https://api.walkscore.com/score?format=json&
                # address=1119%8th%20Avenue%20Seattle%20WA%2098101&lat=47.6085&
                # lon=-122.3295&transit=1&bike=1&wsapikey=<YOUR-WSAPIKEY>
                payload = {
                    'format': 'json',
                    'address': row[0] + ', ' + row[1],
                    'lat': row[2],
                    'lng': row[3],
                    'transit': 1,
                    'bike': 2,
                    'wsapikey': os.getenv('WALKSCORE_API_KEY')
                }
                walkscore_api_url = f"https://api.walkscore.com/score?{urlencode(payload, quote_via=quote_plus)}"
                walkscore = requests.get(walkscore_api_url)
                print(walkscore.json())
                walkscore_data = walkscore.json()

                insert_walkscore_query = f"""
INSERT INTO walkscore
(
    latitude,
    longitude,
    status,
    walkscore,
    description,
    updated,
    logo_url,
    more_info_icon,
    more_info_link,
    ws_link,
    help_link,
    snapped_lat,
    snapped_lon,
    transit_score,
    transit_description,
    bike_score,
    bike_description
)
VALUES
(
    {row[2]},
    {row[3]},
    {walkscore_data['status']},
    {walkscore_data['walkscore']},
    "{walkscore_data['description']}",
    "{walkscore_data['updated']}",
    "{walkscore_data['logo_url']}",
    "{walkscore_data['more_info_icon']}",
    "{walkscore_data['more_info_link']}",
    "{walkscore_data['ws_link']}",
    "{walkscore_data['help_link']}",
    {walkscore_data['snapped_lat']},
    {walkscore_data['snapped_lon']},
    "{walkscore_data['transit']['score'] if 'transit' in walkscore_data.keys() else "0"}",
    "{walkscore_data['transit']['description'] if 'transit' in walkscore_data.keys() else ""}",
    "{walkscore_data['bike']['score'] if 'bike' in walkscore_data.keys() else "0"}",
    "{walkscore_data['bike']['description'] if 'bike' in walkscore_data.keys() else ""}"
)
ON DUPLICATE KEY UPDATE
    latitude={row[2]},
    longitude={row[3]},
    status={walkscore_data['status']},
    walkscore={walkscore_data['walkscore']},
    description="{walkscore_data['description']}",
    updated="{walkscore_data['updated']}",
    logo_url="{walkscore_data['logo_url']}",
    more_info_icon="{walkscore_data['more_info_icon']}",
    more_info_link="{walkscore_data['more_info_link']}",
    ws_link="{walkscore_data['ws_link']}",
    help_link="{walkscore_data['help_link']}",
    snapped_lat={walkscore_data['snapped_lat']},
    snapped_lon={walkscore_data['snapped_lon']},
    transit_score="{walkscore_data['transit']['score'] if 'transit' in walkscore_data.keys() else "0"}",
    transit_description="{walkscore_data['transit']['description'] if 'transit' in walkscore_data.keys() else ""}",
    bike_score="{walkscore_data['bike']['score'] if 'bike' in walkscore_data.keys() else "0"}",
    bike_description="{walkscore_data['bike']['description'] if 'bike' in walkscore_data.keys() else ""}"
                """
                with connection.cursor() as cursor:
                    cursor.execute(insert_walkscore_query)
                    connection.commit()