from abc import ABC, abstractmethod
from packaging import Packaging
from payment import Payment, PayType
from functools import total_ordering
from SameItem import SameItem
import itertools


candy_list=[]
cookie_list=[]
icecream_list=[]
sundae_list=[]


#module level dictionary for customer orders
customer_db = {}

def check_db(customer_name, order, cust_db):
    '''checks if customer is in database. If they are, adds order to existing customer. If not, adds customer, then adds order.'''
    if customer_name in cust_db.keys():
        cust_db[customer_name].order_history.append(order)
    else:
        customer_object = Customer(customer_name)
        cust_db[customer_name] = customer_object
        cust_db[customer_name].order_history.append(order)


#NEED HELP WITH:
# printing receipts in admin mode




#----------CLASSES--------------------CLASSES--------------------CLASSES--------------------CLASSES--------------------CLASSES--------------------CLASSES--------------------CLASSES----------
#----------CLASSES--------------------CLASSES--------------------CLASSES--------------------CLASSES--------------------CLASSES--------------------CLASSES--------------------CLASSES----------
#----------CLASSES--------------------CLASSES--------------------CLASSES--------------------CLASSES--------------------CLASSES--------------------CLASSES--------------------CLASSES----------
@total_ordering
class DessertItem(Packaging, ABC):
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

    def __str__(self):
        return 'Abstract Paarent Class for all Dessert Items'

    @Packaging.packaging.setter
    def packaging(self, new_packaging):
        self._Packaging__packaging = new_packaging
        return self._Packaging__packaging

    def _is_valid_operand(self, other_operand):
        return hasattr(other_operand, "calculate_cost")

    def __eq__(self, other_item):
        if not self._is_valid_operand(other_item):
            return NotImplemented
        return (self.calculate_cost() == other_item.calculate_cost())

    def __lt__(self, other_item):
        if not self._is_valid_operand(other_item):
            print('called not statement')
            return NotImplemented
        return (self.calculate_cost() < other_item.calculate_cost())

class Customer:
    
    next_customer_id = 0

    def __init__(self, name):
        self.name = name
        self.order_history = []
        self.customer_id = Customer.next_customer_id
        Customer.next_customer_id += 1





class Candy(DessertItem, SameItem):
    '''Represents candy items at the shop. Takes name, weight in lbs (int or float), and price per lb (int or lb)'''
    def __init__(self, name="Taffy", candy_weight=1, price_per_pound=1.75, tax_rate = 0.0725):
        DessertItem.__init__(self, name, tax_rate)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = "bag"
        
    def is_same_as(self, other:'Candy'):
        if self.name == other.name and self.price_per_pound == other.price_per_pound:
            return True
        else:
            return False

    def calculate_cost(self):
        ''' calculates item subtotal. takes item_cost as a float and formats it as a string, then returns it as float'''
        item_cost = self.candy_weight * self.price_per_pound
        return item_cost

    def calculate_tax(self):
        ''' calculates item tax. takes item_tax as a float and formats it as a string, then returns it as float'''
        item_tax = self.candy_weight * self.price_per_pound * self.tax_rate
        return item_tax

    def __str__(self):
        item_cost = "${:,.2f}".format(self.calculate_cost())
        item_tax = "${:,.2f}".format(self.calculate_tax())
        return f'{self.name} ({self.packaging})\n {self.candy_weight : <5} lbs @ ${self.price_per_pound}/lb:  {item_cost : >25} [Tax: {item_tax : <4}]'



class Cookie(DessertItem, SameItem):
    """Represents cookie items in the shop. Takes name, quanitity (int), and price per dozen (int or float)"""
    def __init__(self, name="Chocolate Chip", cookie_quantity=12, price_per_dozen=6.99, tax_rate = 0.0725):
        DessertItem.__init__(self, name, tax_rate)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "box"

    def is_same_as(self, other:'Cookie'):
        if self.name == other.name and self.price_per_dozen == other.price_per_dozen:
            return True
        

    def calculate_cost(self):
        ''' calculates item subtotal. takes item_cost as a float and formats it as a string, then returns it as float'''
        dozen = self.cookie_quantity / 12
        item_cost = dozen * self.price_per_dozen
        return item_cost

    def calculate_tax(self):
        ''' calculates item tax. takes item_tax as a float and formats it as a string, then returns it as float'''
        dozen = self.cookie_quantity / 12
        item_tax = dozen * self.price_per_dozen * self.tax_rate
        return item_tax

    def __str__(self):
        item_cost = "${:,.2f}".format(self.calculate_cost())
        item_tax = "${:,.2f}".format(self.calculate_tax())
        return f'{self.name} ({self.packaging})\n {self.cookie_quantity : <5} cookies @ ${self.price_per_dozen}/dozen: {item_cost : >19} [Tax: {item_tax : <4}]'



class IceCream(DessertItem):
    """Represents Ice Cream items in the shop. Takes name, number of scoops (int), and price per scoop (int or float)"""
    def __init__(self, name='Chocolate', scoop_count=2, price_per_scoop=1.50, tax_rate = 0.0725):
        DessertItem.__init__(self, name, tax_rate)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "bowl"

    def calculate_cost(self):
        ''' calculates item subtotal. takes item_cost as a float and formats it as a string, then returns it as float'''
        item_cost = self.scoop_count * self.price_per_scoop
        return item_cost

    def calculate_tax(self):
        '''calculates item tax. takes item_tax as a float and formats it as a string, then returns it as float'''
        item_tax = self.scoop_count * self.price_per_scoop * self.tax_rate
        return item_tax

    def __str__(self):
        item_cost = "${:,.2f}".format(self.calculate_cost())
        item_tax = "${:,.2f}".format(self.calculate_tax())
        return f'{self.name} ({self.packaging})\n {self.scoop_count : <5} scoops @ ${self.price_per_scoop}/scoop: {item_cost : >20} [Tax: {item_tax : <5}]'


class Sundae(IceCream, DessertItem):
    """Child of Ice Cream and Dessert Item class. Represents Sundae items in shop. Takes name, number of scoops, price per scoop, name of topping, and topping price"""
    def __init__(self, name = "Caramel Sundae", scoop_count = 2, price_per_scoop = 1.50, topping_name="Caramel", topping_price=1, tax_rate = 0.0725):
        IceCream.__init__(self, name, scoop_count, price_per_scoop, tax_rate)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "boat"

    def calculate_cost(self):
        ''' calculates item subtotal. takes item_cost as a float and formats it as a string, then returns it as float'''
        item_cost = (self.price_per_scoop * self.scoop_count) + self.topping_price
        return item_cost

    def calculate_tax(self):
        '''calculates item tax. takes item_tax as a float and formats it as a string, then returns it as float'''
        item_tax = (self.price_per_scoop * self.scoop_count * self.tax_rate) + (self.topping_price * self.tax_rate)
        return item_tax

    def __str__(self):
        item_cost = "${:,.2f}".format(self.calculate_cost())
        item_tax = "${:,.2f}".format(self.calculate_tax())
        return f'{self.name} Sundae ({self.packaging})\n {self.scoop_count : <5} scoops of {self.name} ice cream @ ${self.price_per_scoop}/scoop\n {self.topping_name :<10} topping @ {self.topping_price}:{item_cost : >22} [Tax: {item_tax : <5}]'


class Order(Payment):
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

    @Payment.pay_type.setter
    def PayType(self, new_pay_type):
        self._pay_method = new_pay_type

    


#----------MENU PROMPTS--------------------MENU PROMPTS--------------------MENU PROMPTS--------------------MENU PROMPTS--------------------MENU PROMPTS--------------------MENU PROMPTS----------
#----------MENU PROMPTS--------------------MENU PROMPTS--------------------MENU PROMPTS--------------------MENU PROMPTS--------------------MENU PROMPTS--------------------MENU PROMPTS----------
#----------MENU PROMPTS--------------------MENU PROMPTS--------------------MENU PROMPTS--------------------MENU PROMPTS--------------------MENU PROMPTS--------------------MENU PROMPTS----------
def user_prompt_candy():
    '''creates candy object based on user input and adds it to the order'''
    new_item = Candy(input('please put in what kind of candy: '), float(input('please input how any lbs of candy: ')), float(input('please enter price per pound: ')))
    if len(candy_list) > 0:
        for item in candy_list:
            if item.is_same_as(new_item):
                item.candy_weight += new_item.candy_weight
            else:
                candy_list.append(new_item)
    else:
        candy_list.append(new_item)


def user_prompt_cookie():
    '''creates cookie object based on user input and adds it to the order'''
    new_item = Cookie(input('please enter type of cookie: '), int(input('please enter number of cookies: ')), float(input('please input price per dozen: ')))
    if len(cookie_list) > 0:
        for item in cookie_list:
            if item.is_same_as(new_item):
                item.cookie_quantity += new_item.cookie_quantity
            else:
                cookie_list.append(new_item)
    else:
        cookie_list.append(new_item)



def user_prompt_icecream():
    '''creates ice cream object based on user input and adds it to the order'''
    icecream_list.append(IceCream(input('enter type of ice cream: '), int(input('enter number of scoops: ')), float(input('enter price per scoop: '))))




def user_prompt_sundae():
    '''creates sundae object based on user input and adds it to the order'''
    sundae_list.append(Sundae(input('please input type of ice cream: '), int(input('please enter number of scoops: ')), float(input('please enter price per scoop: ')), input('please enter type of topping: '), float(input('please enter topping price: '))))



def admin_mode():
    admin_selection = input('\n1: Shop Customer List \n2: Customer Order History \n3: Best Customer \n4: Exit Admin Mode \n\nEnter Prompt: ')
  
    if admin_selection == '1':
        for customer in customer_db.keys():
            print(f'Customer: {customer : <15} Customer ID: {customer_db[customer].customer_id}\n')
        admin_mode()
        
   
    elif admin_selection == '2':
        order_num = 0
        cust_select = input("Enter Customer Name: ")
        for order in customer_db[cust_select].order_history:
            order_num += 1
            print(f'\n--Order #{order_num}--')
            for item in order.order:
                print(item)
            order_subtotal = "${:,.2f}".format(order.order_cost())
            order_final_tax = "${:,.2f}".format(order.order_tax())
            order_grand_total ="${:,.2f}".format(order.order_cost() + order.order_tax())
            print(f'Order Subtotal: {order_subtotal}')
            print(f'Order Tax: {order_final_tax}')
            print(f'Order Total: {order_grand_total}')

        admin_mode()
   
    elif admin_selection == '3':
        longest_history = max(len(customer.order_history) for customer in customer_db.values())
        for customer in customer_db.values():
            print(len(customer.order_history))
            if len(customer.order_history) == longest_history:
                print(f'Best customer is {customer.name}!\n')
        admin_mode()
        
    elif admin_selection == '4':
        main_menu()
   
    else:
        print('Input not recognized\n')
        admin_mode()



def main_menu():
    '''sets format for the main menu and presents it to the user. calls functions for object creation, adds dessert items to order object'''
    prompt_selection = input("\n1: Candy\n2: Cookie\n3: Ice Cream\n4: Sundae\n5: Admin Module \nWhat would you like to add to the order? (1-4, Enter for done): ")

    #runs main menu of program
    if prompt_selection == "1":
        user_prompt_candy()
        main_menu()
    elif prompt_selection == "2":
        user_prompt_cookie()
        main_menu()
    elif prompt_selection == "3":
        user_prompt_icecream()
        main_menu()
    elif prompt_selection == "4":
        user_prompt_sundae()
        main_menu()
    elif prompt_selection == "5":
        admin_mode()
    elif prompt_selection == "":
        finalize()
        restart_prompt = input('Press Y and Enter to start a new order: ')
        if restart_prompt.lower() == "y":
            main()
        else:
            '''for customer, orders in customer_db.items():
                for item in orders:
                    print(customer, item)''' #keeping that to test the customer database later
            quit
    else:
        print("Input Not Recognized")
        main_menu()



#----------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT----------
#----------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT----------
#----------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT--------------------PRINT RECEIPT----------

#this used to by print_receipt(), but now covers a more comprehensive series of actions 
def finalize(): 
    '''calculates totals and prints receipt. also asks for customers name and adds it to their order history'''
    
    #creates instance of order class
    order_var = Order()

    #appends dessert items to order list
    for item in candy_list:
        order_var.order.append(item)
    for item in cookie_list:
        order_var.order.append(item)
    for item in icecream_list:
        order_var.order.append(item)
    for item in sundae_list:
        order_var.order.append(item)
  
    #gets custoemr name and adds order to their history
    custy_name = input('\n\nplease input customer name: ')
    customer_instance = Customer(custy_name)
    check_db(custy_name, order_var, customer_db)
    
    

  
    #asks for payment type
    pay_select = int(input('\n1: Cash\n2: Card\n3: Phone\nEnter payment method: '))

    #Verifys payment type and sets type appropriately
    if pay_select == 1:
        order_var.pay_type = PayType.CASH
    elif pay_select == 2:
        order_var.pay_type = PayType.CARD
    elif pay_select == 3:
        order_var.pay_type = PayType.PHONE
    else:
        print('\ninvalid payment method')
        finalize()

    order_var.order.sort()
    
    #PRINTS RECEIPT
    print("\n\nRECEIPT")
    print('--------------------')
    for item in order_var.order:
        print(item)
    
    print('--------------------')
    order_subtotal = "${:,.2f}".format(order_var.order_cost())
    order_final_tax = "${:,.2f}".format(order_var.order_tax())
    order_grand_total ="${:,.2f}".format(order_var.order_cost() + order_var.order_tax())
    item_count = order_var.item_count()
    print(f"ORDER SUBTOTAL: {order_subtotal : <10} [TAX: {order_final_tax : >1}]")
    print(f"ORDER TOTAL: {order_grand_total : >8}")
    print(f"TOTAL ITEMS IN ORDER: {item_count : >6}")
    print('--------------------')
    print(f'Paid with {order_var.pay_type.name}')
    print('--------------------')
    print(f'Customer: {custy_name : <15} Customer ID: {customer_instance.customer_id}')




#MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE
#MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE
#MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE----MAIN C0DE

def main():
    global cookie_list
    global candy_list
    global icecream_list
    global sundae_list
    cookie_list = []
    candy_list = []
    icecream_list = []
    sundae_list = []
    main_menu()

if __name__ == '__main__':
    main()

