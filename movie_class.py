import json

class Movie:
    def __init__(self, title, date, author, categories):
        self.title = title
        self.date = date
        self.author = author
        self.categories = categories

    def __str__(self):
        return f"🎥 {self.title} 🎥\n\n📅 Sortie le : {self.date}\n👨 Par : {self.author}\n✨ Genres : {self.categories}"
        
