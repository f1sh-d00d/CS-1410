from abc import ABC, abstractmethod

class DessertItem(ABC):
    '''Parent class and blueprint for all dessert items'''
    def __init__(self, name="", tax_rate = 0.0725):
        self.name = name
        self.tax_rate = tax_rate

    @abstractmethod
    def calculate_cost(self):
        '''abstract method. ultimately will return the cost of an item'''
        pass
    

    def calculate_tax(self):
        '''abstract method. ultimately will return the tax of an item'''
        pass



class Candy(DessertItem):
    '''Represents candy items at the shop. Takes name, weight in lbs (int or float), and price per lb (int or lb)'''
    def __init__(self, name="Taffy", candy_weight=1, price_per_pound=1.75, tax_rate = 0.0725):
        DessertItem.__init__(self, name, tax_rate)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        ''' calculates item subtotal. takes item_cost as a float and formats it as a string, then returns it as float'''
        item_cost = self.candy_weight * self.price_per_pound
        return item_cost

    def calculate_tax(self):
        ''' calculates item tax. takes item_tax as a float and formats it as a string, then returns it as float'''
        item_tax = self.candy_weight * self.price_per_pound * self.tax_rate
        return item_tax
         
        

class Cookie(DessertItem):
    """Represents cookie items in the shop. Takes name, quanitity (int), and price per dozen (int or float)"""
    def __init__(self, name="Chocolate Chip", cookie_quantity=12, price_per_dozen=6.99, tax_rate = 0.0725):
        DessertItem.__init__(self, name, tax_rate)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        ''' calculates item subtotal. takes item_cost as a float and formats it as a string, then returns it as float'''
        dozen = self.cookie_quantity / 12
        item_cost = dozen *self.price_per_dozen
        return item_cost

    def calculate_tax(self):
        ''' calculates item tax. takes item_tax as a float and formats it as a string, then returns it as float'''
        dozen = self.cookie_quantity / 12
        item_tax = dozen * self.price_per_dozen * self.tax_rate
        return item_tax



class IceCream(DessertItem):
    """Represents Ice Cream items in the shop. Takes name, number of scoops (int), and price per scoop (int or float)"""
    def __init__(self, name='Chocolate', scoop_count=2, price_per_scoop=1.50, tax_rate = 0.0725):
        DessertItem.__init__(self, name, tax_rate)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        ''' calculates item subtotal. takes item_cost as a float and formats it as a string, then returns it as float'''
        item_cost = self.scoop_count * self.price_per_scoop
        return item_cost

    def calculate_tax(self):
        '''calculates item tax. takes item_tax as a float and formats it as a string, then returns it as float'''
        item_tax = self.scoop_count * self.price_per_scoop * self.tax_rate
        return item_tax


class Sundae(IceCream, DessertItem):
    """Child of Ice Cream and Dessert Item class. Represents Sundae items in shop. Takes name, number of scoops, price per scoop, name of topping, and topping price"""
    def __init__(self, name = "Caramel Sundae", scoop_count = 2, price_per_scoop = 1.50, topping_name="Caramel", topping_price=1, tax_rate = 0.0725):
        IceCream.__init__(self, name, scoop_count, price_per_scoop, tax_rate)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        ''' calculates item subtotal. takes item_cost as a float and formats it as a string, then returns it as float'''
        item_cost = (self.price_per_scoop * self.scoop_count) + self.topping_price
        return item_cost

    def calculate_tax(self):
        '''calculates item tax. takes item_tax as a float and formats it as a string, then returns it as float'''
        item_tax = (self.price_per_scoop * self.scoop_count * self.tax_rate) + (self.topping_price * self.tax_rate)
        return item_tax



class Order():
    """Represents orders in the shop. Starts with an empty of list of items in the order"""
    def __init__(self):
      self.order = []
   
    def add(self, item_variable):
        """Takes item as parameter and adds item to the order list"""
        self.order.append(item_variable)
   
    def item_count(self):
        """Returns length of order list to show number of items in order """
        return len(self.order)

    def order_cost(self):
        order_sub_total = 0
        for item in self.order:
            order_sub_total += item.calculate_cost()
        return order_sub_total

    def order_tax(self):
        order_total_tax = 0
        for item in self.order:
            order_total_tax += item.calculate_tax()
        return order_total_tax

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

    #PRINTS RECEIPT
    print("RECEIPT")
    for item in order_var.order:
        item_cost = "${:,.2f}".format(item.calculate_cost())
        item_tax = "${:,.2f}".format(item.calculate_tax())
        print(f"{item.name : <15} {item_cost : <10} [TAX: {item_tax : >1}]")
    print('--------------------')
    order_subtotal = "${:,.2f}".format(order_var.order_cost())
    order_final_tax = "${:,.2f}".format(order_var.order_tax())
    order_grand_total ="${:,.2f}".format(order_var.order_cost() + order_var.order_tax())
    item_count = order_var.item_count()
    print(f"ORDER SUBTOTAL: {order_subtotal : <10} [TAX: {order_final_tax : >1}]")
    print(f"ORDER TOTAL: {order_grand_total : >8}")
    print(f"TOTAL ITEMS IN ORDER: {item_count : >6}")


if __name__ == '__main__':
   main()