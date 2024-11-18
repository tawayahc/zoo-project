import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(10), 50)
       
    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(56), 150)

    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(90), 100)

    def test_negative_age(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), -1)

if __name__ == '__main__':
    unittest.main()