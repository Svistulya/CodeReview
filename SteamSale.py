import requests
from bs4 import BeautifulSoup
import sqlite3 as sq

def scrape_page_games(soup, games):
    tab_elements = soup.find('div', {'class' : 'tab_content', 'id' : 'tab_specials_content'}).find_all('div', class_ = 'tab_item_content')
    for element in tab_elements:
        game_name = element.find('div',class_ = 'tab_item_name').text
        games.append(game_name)
def scrape_page_prices(soup, prices_b, prices_dis, prices_a):
    tab_elements = soup.find('div', {'class' : 'tab_content', 'id' : 'tab_specials_content'}).find_all('div', class_ = 'discount_block tab_item_discount')
    for element in tab_elements:
        game_price_before = element.find('div',class_ = 'discount_original_price').text
        game_discount = element.find('div',class_ = 'discount_pct').text
        game_price_after = element.find('div',class_ = 'discount_final_price').text
        
        prices_b.append(game_price_before)
        prices_dis.append(game_discount)
        prices_a.append(game_price_after)

base_url = 'https://store.steampowered.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get(base_url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')