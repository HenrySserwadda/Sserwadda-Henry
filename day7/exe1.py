#create a class called car with brand , model, price then make brand public
#model protected, price private, Display all values appropriately
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand #public variable
        self._model = model #protected variable
        self.__price = price #private variable

    def display_car_info(self):
        print(f"Brand: {self.brand}, Model: {self._model}, Price: {self.__price}")

car1 = Car("Toyota", "Corolla", 20000)
car1.display_car_info()        