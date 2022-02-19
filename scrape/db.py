from bs4 import BeautifulSoup
from dotenv import load_dotenv
import json
from mysql.connector import connect, Error
import os
import requests

load_dotenv()

try:
    with connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_DATABASE')
    ) as connection:
        print(connection)
except Error as e:
    print(e)

connection = connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_DATABASE')
    )