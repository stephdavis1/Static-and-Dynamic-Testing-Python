import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.ace = Card('hearts', 1)
        self.card2 = Card('hearts', 5)
        self.card3 = Card('hearts', 6)
        self.deck_of_cards = [self.ace, self.card2, self.card3]
        self.card_game = CardGame()

    def test_check_for_ace(self):
        self.assertTrue(self.card_game.check_for_ace(self.ace))
        self.assertFalse(self.card_game.check_for_ace(self.card2))

    def test_highest_card(self):
        self.hightest_card = self.card_game.highest_card(self.card2, self.card3)
        self.assertEqual(self.hightest_card.value, 6)

        self.hightest_card = self.card_game.highest_card(self.card3, self.card2)
        self.assertEqual(self.hightest_card.value, 6)

    def test_cards_total(self):
        self.assertEqual(self.card_game.cards_total(self.deck_of_cards),"You have a total of 12")
