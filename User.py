from EmailUtil import *

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = dict()

    def get_email(self):
        return self.email

    def change_email(self, address):
        if EmailUtil.check_is_valid_email(address):
            self.email = address
            print("The email of user " + self.name + " has been updated")

    def get_average_rating(self):

        total_rating = 0
        num_ratings = 0

        for book in self.books:
            if self.books[book]:
                total_rating += self.books[book]
                num_ratings += 1

        if num_ratings > 0:
            return total_rating / num_ratings
        else:
            return 0

    def get_worth(self):
        total_worth = 0.0

        for book in self.books:
            total_worth += book.get_price()

        return total_worth

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def __repr__(self):
        return "User {}, email: {}, books read: {}".format(self.name, self.email, str(len(self.books)))

    def __eq__(self, other_user):
        return isinstance(other_user, User) and self.name == other_user.name and self.email == other_user.email