class ISBN_Collection:

    used_isbns = set()
    __used_isbn_error_message = "ISBN {} is already associated with another book."

    def add_isbn(isbn):
        ISBN_Collection.used_isbns.add(isbn)

    def remove_isbn(isbn):
        ISBN_Collection.used_isbns.remove(isbn)

    def is_used_isbn(isbn):
        return isbn in ISBN_Collection.used_isbns

    def check_is_used_isbn(isbn):
        if ISBN_Collection.is_used_isbn(isbn):
            print(ISBN_Collection.__used_isbn_error_message.format(isbn))
            return True

        return False