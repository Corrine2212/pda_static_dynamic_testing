import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game = CardGame()
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 5)
        self.card3 = Card("Clubs", 7)
        self.card4 = Card("Diamonds", 4)
        self.cards = [self.card1, self.card2, self.card3, self.card4]

    def test_check_for_ace(self):
        self.assertTrue(self.game.check_for_ace(self.card1))
        self.assertFalse(self.game.check_for_ace(self.card2))

    def test_highest_card(self):
        highest = self.game.highest_card(self.card3, self.card4)
        self.assertEqual(highest, self.card3)

    def test_cards_total(self):
        total = self.game.cards_total(self.cards)
        self.assertEqual(total, "You have a total of 17")