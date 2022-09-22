import unittest
from dessert_shop_3 import Candy, Cookie, IceCream, Sundae


class TestDesserts(unittest.TestCase):

  def test_candy(self):
    candy_corn = Candy("Candy Corn", 1.5, .25)
    self.assertEqual(candy_corn.name, "Candy Corn")
    self.assertEqual(candy_corn.candy_weight, 1.5)
    self.assertEqual(candy_corn.price_per_pound, .25)
    self.assertEqual(candy_corn.calculate_cost, 0.375)
    self.assertEqual(candy_corn.calculate_tax, 0.027187499999999996)
    
  
  def test_cookie(self):
    chocolate_chip = Cookie("Chocolate Chip", 6, 3.99)
    self.assertEqual(chocolate_chip.name, "Chocolate Chip")
    self.assertEqual(chocolate_chip.cookie_quantity, 6)
    self.assertEqual(chocolate_chip.price_per_dozen, 3.99)
    self.assertEqual(chocolate_chip.calculate_cost, 1.995)
    self.assertEqual(chocolate_chip.calculate_tax, 0.1446375)

  def test_icecream(self):
    pistachio = IceCream("Pistachio", 2, .79)
    self.assertEqual(pistachio.name, "Pistachio")
    self.assertEqual(pistachio.scoop_count, 2)
    self.assertEqual(pistachio.price_per_scoop, .79)
    self.assertEqual(pistachio.calculate_cost, 1.58)
    self.asserEqual(pistachio.calculate_tax, 0.11455)
    

  def test_sundae(self):
    fudge_sundae = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    self.assertEqual(fudge_sundae.name, "Vanilla")
    self.assertEqual(fudge_sundae.scoop_count, 3)
    self.assertEqual(fudge_sundae.price_per_scoop, .69)
    self.assertEqual(fudge_sundae.topping_name, "Hot Fudge")
    self.assertEqual(fudge_sundae.topping_price, 1.29)
    self.assertEqual(fudge_sundae.calculate_cost, 3.36)
    self.assertEqual(fudge_sundae.calculate_tax, 0.24359999999999998)
    
