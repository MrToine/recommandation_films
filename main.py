from scrapper import *
from movie_class import *
from manager_class import *
from interface_class import *
from utils import clear_console
from rich.console import Console

interface = Interface()
console = Console()
movies = None

while True:
    clear_console()
    choice = interface.show_menu()

    match choice:
        case '1':
            movies = interface.load_database()
        case '2': 
            if movies != None:
                interface.random_movie(movies)
            else:
                console.print('[red]Le fichier database n\'a pas été chargé. (Option 1)[/red]')
        case '3':
            if movies != None:
                interface.random_movie_with_filters(movies)
            else:
                console.print('[red]Le fichier database n\'a pas été chargé. (Option 1)[/red]')
        case 'q':
            break