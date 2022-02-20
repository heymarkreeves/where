# Places

## Criteria

1. Trader Joe&rsquo;s
2. Indie bookstore(s) within 10 miles
3. *Co-op grocery store*
4. Walk Score in vicinity of indie bookstore

## Reports

### Report 1

[Independent bookstores within 10 miles of a Trader Joe&rsquo;s zip code](./data/bookstores-trader-joes.csv), using IndieBound.org.

```
Select
    b.name 'Bookstore', b.city 'City', b.state 'State',
    CASE WHEN c.outside_2021 = 1 THEN 'Yes' ELSE ''  END as 'Outside 2021',
    w.walkscore 'Walkscore', w.description 'Walkscore Description', w.bike_score 'Bike Score', w.bike_description 'Bike Score Description', w.transit_score 'Transit Score', w.transit_description 'Transit Score Description'
from bookstores b join walkscore w on b.latitude = w.latitude and b.longitude = w.longitude
left join cities c on b.city = c.city and b.state = c.state
where b.state in ('ME', 'NH', 'VT', 'MA', 'RI', 'CT', 'NY', 'NJ', 'PA', 'DE', 'MD', 'WV', 'VA', 'NC', 'SC', 'GA', 'NM', 'AZ', 'UT')
order by
    field(b.state, 'ME', 'NH', 'VT', 'MA', 'RI', 'CT', 'NY', 'NJ', 'PA', 'DE', 'MD', 'WV', 'VA', 'NC', 'SC', 'GA', 'NM', 'AZ', 'UT') asc,
    walkscore desc,
    bike_score desc,
    transit_score desc;
```

## Development

### Usage

Use `pip3` to install `bs4`, `json`, `dotenv`, `mysql.connector`, `requests`.

Database & tables need to be created, with unique indexes across all fields.

Copy `.env.example` to `.env` and add database credentials.

Run `python3 trader_joes.py`.

Run `python3 bookstores.py`.

### To Do

* [ ] Walkability scores
* [ ] Co-op grocery stores https://www.localharvest.org/getmap.jsp?zip=05602

### Resources

* https://www.geeksforgeeks.org/how-to-parse-data-from-json-into-python/
* https://www.geeksforgeeks.org/python-web-scraping-tutorial/
* https://beautiful-soup-4.readthedocs.io/en/latest/index.html
* https://realpython.com/python-mysql/
* https://locations.traderjoes.com/
* https://www.indiebound.org/indie-store-finder?q=05602
* https://www.walkscore.com/professional/api-sign-up/free
* Looks more robust for working with results: https://www.geeksforgeeks.org/mysqldb-connection-python/
  * https://stackoverflow.com/a/15423453/1263204