import random
from rich.console import Console
from manager_class import *
from utils import clear_console

class Interface:
    def __init__(self):
        self.console = Console()


    def show_menu(self):
        self.console.print(
            '[justify center blue]Bienvenue sur [blue]Recommandation de film[/blue][/justify center blue]',
            '1 : [#FF9033]Charger la database (à faire avant toute chose)[/#FF9033]',
            '2 : Proposer un film aléatoire',
            '3 : Proposer un film aléatoire avec filtres',
            '[cyan]q[/cyan]: Quitter le programme'
            , sep='\n')
        choice = input('\n > ')

        return choice

    def load_database(self):
        manager = Manager('movieset_database.json')
        self.console.print(
            '[blue]💿 Charger la database[/blue]',
            )
        choice = int(input('Indiquez le nombre de pages à charger > '))
        if choice is not int(choice):
            self.console.print('[red]Veuillez indiquer un chiffre valide.[/red]')
            return None
        return manager.load_database(choice)

    def random_movie(self, movies):
        while True:
            clear_console()
            print(movies.get_by_id(str(random.randint(1, movies.lenght()))))
            wait = input('Entrer : Un autre\nr : Retour \n> ')
            match wait:
                case 'r':
                    break
    
    def random_movie_with_filters(self, movies):
        while True:
            clear_console()
            self.console.print(
                '🔎 [bold][#FFBA33]Propose moi un film[/#FFBA33][/bold]',
                'Indiquez les filtres séparés par une virgule (categories=,date=,author=)',
                sep='\n')
            filters = input('\n> ')
            filters = filters.split(',')
            size = len(filters)

            print(filters)

            match size:
                case 1:
                    filter = filters[0].split('=')
                    movies.get_by_filter(filter)
                    
                    while True:   
                        clear_console()
                        filter = filters[0].split('=')
                        movies.get_by_filter(filter)
                        wait = input('Entrer : Un autre\nr : Retour \n> ')
                        
                        match wait:
                            case 'r':
                                break

                case 2:
                    print('2 arguments')
                case 3:
                    print('3 arguments')
                case 'r':
                    break
                case _:
                    pass