import unittest
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae


class TestDesserts(unittest.TestCase):

  def test_candy(self):
    candy_corn = Candy()
    self.assertEqual(candy_corn.name, "Taffy")
    self.assertEqual(candy_corn.candy_weight, 1)
    self.assertEqual(candy_corn.price_per_pound, 1.75)
    candy_corn = Candy("Peanut M&Ms", 2, 2)
    self.assertEqual(candy_corn.name, "Peanut M&Ms")
    self.assertEqual(candy_corn.candy_weight, 2)
    self.assertEqual(candy_corn.price_per_pound, 2)
  
  def test_cookie(self):
    chocolate_chip = Cookie()
    self.assertEqual(chocolate_chip.name, "Chocolate Chip")
    self.assertEqual(chocolate_chip.cookie_quantity, 12)
    self.assertEqual(chocolate_chip.price_per_dozen, 6.99)
    chocolate_chip = Cookie("Snickerdoodle",6, 12)
    self.assertEqual(chocolate_chip.name, "Snickerdoodle")
    self.assertEqual(chocolate_chip.cookie_quantity, 6)
    self.assertEqual(chocolate_chip.price_per_dozen, 12)

  def test_icecream(self):
    choc_cone = IceCream()
    self.assertEqual(choc_cone.name, "Chocolate")
    self.assertEqual(choc_cone.scoop_count, 2)
    self.assertEqual(choc_cone.price_per_scoop, 1.50)
    choc_cone = IceCream("Rocky Road", 1, 2)
    self.assertEqual(choc_cone.name, "Rocky Road")
    self.assertEqual(choc_cone.scoop_count, 1)
    self.assertEqual(choc_cone.price_per_scoop, 2)

  def test_sundae(self):
    fudge_sunday = Sundae()
    self.assertEqual(fudge_sunday.name, "Caramel Sundae")
    self.assertEqual(fudge_sunday.scoop_count, 2)
    self.assertEqual(fudge_sunday.price_per_scoop, 1.50)
    self.assertEqual(fudge_sunday.topping_name, "Caramel")
    self.assertEqual(fudge_sunday.topping_price, 1)
    fudge_sunday = Sundae("Banana Split", 3, 1, "Banana & Fudge", 2.29)
    self.assertEqual(fudge_sunday.name, "Banana Split")
    self.assertEqual(fudge_sunday.scoop_count, 3)
    self.assertEqual(fudge_sunday.price_per_scoop, 1)
    self.assertEqual(fudge_sunday.topping_name, "Banana & Fudge")
    self.assertEqual(fudge_sunday.topping_price, 2.29)



