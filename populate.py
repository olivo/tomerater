from EmailUtil import *
from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.get_most_read_book())

# Extra tests
# Trying to add the user with email marvin@mit.edu should fail and print an error message.
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

# Trying to add a book with an already used ISBN should print an error message.
extra_book1 = Tome_Rater.create_book("The Big Short", 12345678)
extra_novel1 = Tome_Rater.create_novel("Lord of the Rings", "J.R.R. Tolkien", 9781536831139)
extra_nonfiction1 = Tome_Rater.create_non_fiction("Artificial Intelligence: A Modern Approach", "AI", "advanced", 1929452)

# Trying to add a book with an ISBN that has become available due to an ISBN update should allow the creation of the book.
extra_nonfiction1 = Tome_Rater.create_non_fiction("Artificial Intelligence: A Modern Approach", "AI", "advanced", 12345)
print(extra_nonfiction1)

# Checking that EmailUtil parses emails properly.
print("Parsing email: alan@turing.com")
print("Validity: " + str(EmailUtil.check_is_valid_email("alan@turing.com")))
print("Parsing email: marvin@mit.ed")
print("Validity: " + str(EmailUtil.check_is_valid_email("mabin@mit.ed")))
print("Parsing email: davidcomputation.org")
print("Validity: " + str(EmailUtil.check_is_valid_email("davidcomputation.org")))

# Checking equality
print("Expected equality of TomeRater: " + str(Tome_Rater == Tome_Rater))
print("Expected inequality of TomeRater: " + str(Tome_Rater == TomeRater()))

print("Two most read books: ")
print(Tome_Rater.get_n_most_read_books(2))

print("Two most prolific readers: ")
print(Tome_Rater.get_n_most_prolific_readers(2))

# Adding books with prices.
extra_nonfiction2 = Tome_Rater.create_non_fiction("Clean Code", "Software Engineering", "advanced", 6789, 43.27)
extra_novel2 = Tome_Rater.create_novel("Ender's Game", "Orson Scott Card", 11121314, 11.05)
extra_book2 = Tome_Rater.create_book("Introduction to High-Frequency Finance", 15161718, 132.00)

# Adding books with prices to users.
Tome_Rater.add_book_to_user(extra_nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(extra_novel2, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(extra_nonfiction2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(extra_book2, "marvin@mit.edu", 3)
Tome_Rater.add_book_to_user(extra_novel2, "david@computation.org", 3)
Tome_Rater.add_book_to_user(extra_book2, "david@computation.org", 3)

# Getting the most expensive books.
Tome_Rater.print_catalog()
print("The two most expensive books:")
print(Tome_Rater.get_n_most_expensive_books(2))

# Getting the worth of different users.
print("Alan Turing's book worth: " + str(Tome_Rater.get_worth_of_user("alan@turing.com")))
print("Marvin Minsky's book worth: " + str(Tome_Rater.get_worth_of_user("marvin@mit.edu")))
print("David Marr's book worth: " + str(Tome_Rater.get_worth_of_user("david@computation.org")))
