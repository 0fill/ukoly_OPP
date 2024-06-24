
class Book():
    def __init__(self, title, year_of_release, publisher, genre, author, price):
        self.__title = title
        self.__year_of_release = year_of_release
        self.publisher = publisher
        self.genre = genre
        self.__author = author
        self.price = price

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_year_of_release(self, year_of_release):
        self.__year_of_release = year_of_release

    def get_year_of_release(self):
        return self.__year_of_release

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price