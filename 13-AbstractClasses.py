class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price

    def display(self):
        print(
            f'Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}')
