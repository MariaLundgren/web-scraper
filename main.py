from bs4 import BeautifulSoup 
import requests
import time

print('Write the title of the game you are looking for')
my_game = input('>')

def find_games():
    html_text = requests.get('https://co-op-game-review.herokuapp.com/').text 
    soup = BeautifulSoup(html_text, 'lxml')
    games = soup.find_all('div', class_ = 'card title-cards title-card-home hoverable')
    for game in games:
        rating = game.find('p', class_ = 'inline-elements').text
        if rating >= '3': 
            game_title = game.find('span', class_ = 'card-title title-name' ).text
            if my_game in game_title:
                print(f'Game Title: {game_title}')
                print(f'Average Rating: {rating}')

find_games()
                



