
class Car():
    def __init__(self, model, year_of_release, manufacturer, engine_capacity, color, price):
        self.__model = model
        self.__year_of_release = year_of_release
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setYearOfRelease(self, year_of_release):
        self.__year_of_release = year_of_release

    def getYearOfRelease(self):
        return self.__year_of_release

    def setManufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def getManufacturer(self):
        return self.manufacturer

    def setEngineCapacity(self, engine_capacity):
        self.engine_capacity = engine_capacity
    def getEngineCapacity(self):
        return self.engine_capacity

    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price