class Book:
    def __init__(self, isbn, title, author, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price


    def __str__(self):
        # format price with dollar sign
        formatPrice = "${:,.2f}".format(float(self.price))

        return f"{self.isbn} {self.title} {self.author} {formatPrice} \n"    


    def display(self):
        # format price with dollar sign
        self.price = "${:,.2f}".format(float(self.price))

        print(f"{self.isbn} {self.title} {self.author} {self.price}")

    
