from Book import *
from EmailUtil import *
from Fiction import *
from ISBN_Collection import *
from Non_Fiction import *
from User import *

class TomeRater:
    def __init__(self):
        self.users = dict()
        self.books = dict()

    def create_book(self, title, isbn, price=0.0):
        if not ISBN_Collection.check_is_used_isbn(isbn):
            ISBN_Collection.add_isbn(isbn)
            return Book(title, isbn, price)

        return None

    def create_novel(self, title, author, isbn, price=0.0):
        if not ISBN_Collection.check_is_used_isbn(isbn):
            ISBN_Collection.add_isbn(isbn)
            return Fiction(title, author, isbn, price)

        return None

    def create_non_fiction(self, title, subject, level, isbn, price=0.0):
        if not ISBN_Collection.check_is_used_isbn(isbn):
            ISBN_Collection.add_isbn(isbn)
            return Non_Fiction(title, subject, level, isbn, price)

        return None

    def add_book_to_user(self, book, email, rating = None):
        if email not in self.users:
            print("No user with email {}".format(email))
            return

        user = self.users[email]

        user.read_book(book, rating)
        book.add_rating(rating)

        self.books[book] = self.books.get(book, 0) + 1

    # Note: Changed 'books' to 'user_books' in order to work with populate.py
    def add_user(self, name, email, user_books = None):

        if email in self.users:
            print("User with email {} is already registered!".format(email))
            return

        if EmailUtil.check_is_valid_email(email):
            user = User(name, email)

            if user is None:
                return

            self.users[email] = user

            if user_books:
                for book in user_books:
                    self.add_book_to_user(book, email)

    def __highest_rated_object(self, collection):
        highest_rated_element = None
        highest_rating = -1

        for element in collection:
            rating = element.get_average_rating()

            if rating > highest_rating:
                highest_rating = rating
                highest_rated_element = element

        return highest_rated_element

    def highest_rated_book(self):
        return self.__highest_rated_object(self.books.keys())

    def most_positive_user(self):
        return self.__highest_rated_object(self.users.values())

    # Note: changed 'most_read_book' to 'get_most_read_book' to comply with populate.py
    def get_most_read_book(self):
        most_read_book = None
        most_read_count = -1

        for book, read_count in self.books.items():
            if read_count > most_read_count:
                most_read_book = book
                most_read_count = read_count

        return most_read_book

    def get_n_top_elements_by_value(self, elements, n):
        sorted_elements = sorted(elements, key = lambda x: x[1], reverse = True)

        return [x for (x,y) in sorted_elements[: min(len(sorted_elements), n)]]

    def get_n_most_prolific_readers(self, n):
        return self.get_n_top_elements_by_value([(x, len(x.books)) for x in self.users.values()], n)

    def get_n_most_read_books(self, n):
        return self.get_n_top_elements_by_value([(x, self.books[x]) for x in self.books], n)

    def get_n_most_expensive_books(self, n):
        return self.get_n_top_elements_by_value([(x, x.get_price()) for x in self.books], n)

    def get_worth_of_user(self, user_email):
            if user_email not in self.users:
                print("User with email {} not found".format(user_email))
                return 0.0

            return self.users[user_email].get_worth()

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def __eq(self, other):
        return isinstance(other, TomeRater) and self.users == other.users and self.books == other.books

    def __repr__(self):
        return "{Users: " + str(self.users) + ", Books: " + str(self.books) + "}"