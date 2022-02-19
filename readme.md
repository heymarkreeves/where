# Places

## Criteria

1. Trader Joe&rsquo;s
2. Indie bookstore(s) within 10 miles
3. *Co-op grocery store*
4. *Walk Score in vicinity of indie bookstore*

## Development

### Usage

Use `pip3` to install `bs4`, `json`, `dotenv`, `mysql.connector`, `requests`.

Database & tables need to be created, with unique indexes across all fields.

Copy `.env.example` to `.env` and add database credentials.

Run `python3 trader_joes.py`.

Run `python3 bookstores.py`.

### To Do

* [ ] Walk scores
* [ ] Co-op grocery stores https://www.localharvest.org/getmap.jsp?zip=05602

### Resources

* https://www.geeksforgeeks.org/how-to-parse-data-from-json-into-python/
* https://www.geeksforgeeks.org/python-web-scraping-tutorial/
* https://beautiful-soup-4.readthedocs.io/en/latest/index.html
* https://realpython.com/python-mysql/
* https://locations.traderjoes.com/
* https://www.indiebound.org/indie-store-finder?q=05602
* https://www.walkscore.com/professional/api-sign-up/free