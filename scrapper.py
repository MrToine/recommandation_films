import os, requests, json 
from movie_class import *
from bs4 import BeautifulSoup
from rich.console import Console

class Scrapper:
    """
        Classe permettant de scrapper les données de allociné
        :mod:`url` contient l'url du scrapper
        :mod:`nb_pages` contient le nombre de pages à récupérer
    """
    def __init__(self, url, nb_pages):
        self.nb_pages = nb_pages
        self.url = url
        self.movies_set = 'movieset_database.json'
        
        self.console = Console()

        self.movies_datas = {}

        if not os.path.exists(self.movies_set):
            with open(self.movies_set, 'w') as file:
                json.dump({}, file)
                self.console.print('[yellow]Création base de données[/yellow]............................[green]ok[/green]')

    def parse(self):
        id = 0
        for i in range(1, self.nb_pages +1, 1):
            response = requests.get(self.url + str(i))
            response.raise_for_status()

            scrap = BeautifulSoup(response.content, 'html.parser')

            for movie in scrap.find_all('li', class_='mdl'):
                title_tag = movie.find('h2', class_='meta-title')
                title = title_tag.text.strip() if title_tag else 'N/A'

                date_tag = movie.find('span', class_='date')
                date = date_tag.text.strip() if date_tag else 'Inconnu'
                
                author_block = movie.find('div', class_='meta-body-item meta-body-direction')
                author = author_block.text.strip() if author_block else ''
                author = author[3:]
                author = author.replace('\n', ' ')

                categories_block = movie.find('div', class_='meta-body-item meta-body-info')
                categories = categories_block.text.strip()[24:]
                categories = categories.replace('|', '').replace('\n', ' ').strip()
                id += 1
            
                if title != 'N/A':
                    self.movies_datas[id] = {
                        'title' : title,
                        'date' : date,
                        'author' : author,
                        'categories' : categories
                    }
                
            self.console.print(f"Page : {i}............................[bold green]chargé[/bold green]")

        return self.movies_datas

    def write(self, dict_movies):
        with open(self.movies_set, 'w') as file:
            json.dump(dict_movies, file)
