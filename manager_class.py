import os, json
import random
from scrapper import *
from movie_class import *
from rich.console import Console

class Manager:
    def __init__(self, file):
        self.file = file
        self.data_lenght = None
        self.console = Console()

        if not os.path.exists(self.file):
            with open(self.file, 'w') as file:
                json.dump({}, file)
        else:
            self.console.print('[green]Le fichier database à été chargé.[/green]')
    
    def _read_file(self):
        with open(self.file, 'r') as file:
            return json.load(file)
    
    def load_database(self, nb_pages):
        scrap = Scrapper('https://www.allocine.fr/films/?page=', nb_pages)
        dict = scrap.parse()
        scrap.write(dict)
        return Manager('movieset_database.json')
        
    def lenght(self):
        file = self._read_file()
        return len(file)

    def get_by_id(self, movie_id):
        datas = self._read_file()
        movie_datas = datas.get(movie_id, {})
        if movie_datas:
            return Movie(movie_datas['title'], movie_datas['date'], movie_datas['author'], movie_datas['categories'])
        return None

    def get_by_filter(self, filter):
        datas = self._read_file()
        movies_list = []
        
        if len(filter) > 0:
            for key, index in datas.items():
                for item, value in index.items():
                    if filter[0] in item:
                        if filter[0] == 'author':
                            filter[1] = value.title()
                        if filter[1] in value:
                            movies_list.append(key)
            if len(movies_list) > 0:
                print(self.get_by_id(str(random.choice(movies_list))))
            else:
                self.console.print('[red]Aucun film trouvé.[/red]')
