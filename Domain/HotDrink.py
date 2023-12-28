from Domain.product import Product
class HotDrink(Product):
    def __init__(self, price=-1, place=-1, name="Неизвестно", id=-1, temperature=-1):
        super().__init__(price, place, name, id)
        self.temperature = temperature

    def __str__(self):
        return "\nPrice = " + str(self.price) + "\n" + "Place = " + str(self.place) + "\n" + "Name = " + self.name + "\n" + "ID = " + str(self.id) + "\n" + "Temperature = " + str(self.temperature) + "\n"

