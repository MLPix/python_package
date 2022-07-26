import random

class Recommender:
    '''
    Class for returning random movies from list
    '''
    
    def __init__(self, list_of_movies):
        self.list_of_movies = list_of_movies

    def random_recommendations(self):
        return random.choice(self.list_of_movies)
        