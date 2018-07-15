from ISBN_Collection import *

class Book:
    def __init__(self, title, isbn, price=0.0):
        self.title = title
        self.isbn = isbn
        self.ratings = list()
        self.price = price

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def get_price(self):
        return self.price

    def set_isbn(self, new_isbn):

        if not ISBN_Collection.check_is_used_isbn(new_isbn):
            ISBN_Collection.add_isbn(new_isbn)
            ISBN_Collection.remove_isbn(self.isbn)
            self.isbn = new_isbn
            print("The ISBN of book " + self.title + " has been updated.")
        else:
            return

    def add_rating(self, rating):
        if isinstance(rating, int) and 0 <= rating and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        total_rating = 0
        num_ratings = 0

        for rating in self.ratings:
            total_rating += rating
            num_ratings += 1

        if num_ratings > 0:
            return total_rating / num_ratings
        else:
            return 0

    def __eq__(self, other_book):
        return isinstance(other_book, Book) and self.title == other_book.title and self.isbn == other_book.isbn \
               and self.price == other_book.price

    def __hash__(self):
        return hash((self.title, self.isbn, self.price))

    # Not in the spec, but it seems that Book should have a basic string representation.
    def __repr__(self):
        return "Book titled {}".format(self.title)