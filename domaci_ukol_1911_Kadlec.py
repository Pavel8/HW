class Book:
    def __init__(self, title, release, publisher, genre, author, price):
        self.title = title
        self.release = release
        self.publisher = publisher 
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        return (f" title: {self.title}, release: {self.release}, publisher: {self.publisher}, genre: {self.genre}, author: {self.author}, price: {self.price}")

b1 = Book("Harry Potter", "2002", "nekdo", "fantasy", "J.K. Rowling", 299)
b2 = Book("Lord of the Rings", "1955", "nekdo dalsi", "fantasy", "Tolkien", 499)

print(b1)
print(b2)