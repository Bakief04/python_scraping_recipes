class MyClass:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.combine = self.make + " " + self.model
    def statement(self):
        print("hello I drive a " + self.combine)

car = MyClass("Toyota", "Camry")
car2 = MyClass("Ford", "Taurus")
car.statement()
print(car2.make + ' ' + car2.model)
print(car2.model)