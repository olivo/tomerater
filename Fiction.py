from Book import *

class Fiction(Book):
    def __init__(self, title, author, isbn, price=0.0):
        super().__init__(title, isbn, price)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)