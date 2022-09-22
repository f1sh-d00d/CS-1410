class DessertItem():
    '''Parent class and blueprint for all dessert items'''
    def __init__(self, name=""):
        self.name = name

class Candy(DessertItem):
    '''Represents candy items at the shop. Takes name, weight in lbs (int or float), and price per lb (int or lb)'''
    def __init__(self, name="Taffy", candy_weight=1, price_per_pound=1.75):
        DessertItem.__init__(self, name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

class Cookie(DessertItem):
    """Represents cookie items in the shop. Takes name, quanitity (int), and price per dozen (int or float)"""
    def __init__(self, name="Chocolate Chip", cookie_quantity=12, price_per_dozen=6.99):
        DessertItem.__init__(self, name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

class IceCream(DessertItem):
    """Represents Ice Cream items in the shop. Takes name, number of scoops (int), and price per scoop (int or float)"""
    def __init__(self, name='Chocolate', scoop_count=2, price_per_scoop=1.50):
        DessertItem.__init__(self, name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

class Sundae(IceCream, DessertItem):
    """Child of Ice Cream and Dessert Item class. Represents Sundae items in shop. Takes name, number of scoops, price per scoop, name of topping, and topping price"""
    def __init__(self, name = "Caramel Sundae", scoop_count = 2, price_per_scoop = 1.50, topping_name="Caramel", topping_price=1):
        IceCream.__init__(self, name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

class Order():
    """Represents orders in the shop. Starts with an empty of list of items in the order"""
    def __init__(self):
      self.order = []
   
    def add(self, item_variable):
        """Takes item as parameter and adds item to the order list"""
        self.order.append(item_variable)
   
    def item_count(self):
        """Returns length of order list to show number of items in order """
        print(f'Total number of items in order: {len(self.order)}')

def main():
   candy_corn = Candy("Candy Corn", 1.5, .25)
   gummy_bears = Candy("Gummy Bears", .25, .35)
   choc_chip = Cookie("Chocolate Chip", 6, 3.99)
   pistachio = IceCream("Pistachio", 2, .79)
   fudge_sundae = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
   oat_raisin = Cookie("Oatmeal Raisin", 2, 3.45)

   order_var = Order()
   order_var.add(candy_corn)
   order_var.add(gummy_bears)
   order_var.add(choc_chip)
   order_var.add(pistachio)
   order_var.add(fudge_sundae)
   order_var.add(oat_raisin)

   

   for item in order_var.order:
      print(item.name)
   
   order_var.item_count()

if __name__ == '__main__':
   main()