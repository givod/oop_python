class Book:

    BOOK_TYPES = ("HARDCOVER","PAPERBACK","EBOOK")

    #Class method
    @classmethod
    def getbooktypes(cls):
        return  cls.BOOK_TYPES

    __booklist = None

    #Static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def __init__(self,title, author, pages, price, booktype):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount


class NewsPaper:
    def __init__(self,title):
        self.title = title


b1 = Book(title, "author", "pages", "price")
print(isinstance(b1, Book))
