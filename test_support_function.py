import unittest
import support_function
import bill

class TestSupportFunction(unittest.TestCase):

    def test_bill_num(self):
        self.assertEqual(support_function.bill_num(5),5)
        self.assertEqual(support_function.bill_num(0), 0)
        self.assertEqual(support_function.bill_num(-5), -1)
        self.assertEqual(support_function.bill_num(12), -1)
        self.assertRaises(AssertionError, support_function.bill_num, "ciao")
        self.assertRaises(AssertionError, support_function.bill_num, [1,2,3])
        self.assertRaises(AssertionError, support_function.bill_num, True)


    def test_city_choice(self):
        self.assertEqual(support_function.city_choice("Milano"),"Milano")
        self.assertEqual(support_function.city_choice("milano"),-1)
        self.assertEqual(support_function.city_choice("Tutte"),"Tutte")
        self.assertEqual(support_function.city_choice("Catania"),-1)
        self.assertEqual(support_function.city_choice(False),-1)
        self.assertEqual(support_function.city_choice(33),-1)


    def test_bet_choice(self):
        self.assertEqual(support_function.bet_choice("Ambo"),"Ambo")
        self.assertEqual(support_function.bet_choice("ambo"),-1)
        self.assertEqual(support_function.bet_choice("Cinquina"),"Cinquina")
        self.assertEqual(support_function.bet_choice("tombola"),-1)
        self.assertEqual(support_function.bet_choice(False),-1)
        self.assertEqual(support_function.bet_choice(33),-1)


    def test_ticket_number_generation(self):
        self.assertAlmostEqual(support_function.ticket_number_generation(0),-1)
        self.assertAlmostEqual(support_function.ticket_number_generation(5),1)
        self.assertAlmostEqual(support_function.ticket_number_generation(15),-1)

if __name__ == '__main__':
    unittest.main()