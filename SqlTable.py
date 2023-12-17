import sqlite3 as sq
from SteamSale import scrape_page_games
from SteamSale import scrape_page_prices
from bs4 import BeautifulSoup
import requests

base_url = 'https://store.steampowered.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get(base_url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

con = sq.connect('SteamSale.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS SteamSale (
    name TEXT,
    price_before TEXT,
    dicount TEXT,
    price_after TEXT
    )
    """)

games = []
prices_b = []
prices_dis = []
prices_a = []
scrape_page_games(soup,games)
scrape_page_prices(soup, prices_b, prices_dis, prices_a)

for i in range(len(games)):
    cur.execute("INSERT INTO 'SteamSale' VALUES(?, ?, ?, ?)", ((games[i]), (prices_b[i]), (prices_dis[i]), (prices_a[i])))
    con.commit()
con.close()
