import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = self.create_cards()

    def shuffle(self):
        # TODO break, text about shuffling, setting is_on_deck = True in all cards
        random.shuffle(self.cards)
        pass

    def get_card(self):
        while True:
            index = random.randint(0, 51)
            if self.cards[index].get_is_on_deck():
                self.cards[index].set_is_on_deck(False)
                return self.cards[index]

    @staticmethod
    def create_cards():
        cards = [Card(2, None, "assets/clubs/2.png"), Card(3, None, "assets/clubs/3.png"),
                 Card(4, None, "assets/clubs/4.png"), Card(5, None, "assets/clubs/5.png"),
                 Card(6, None, "assets/clubs/6.png"), Card(7, None, "assets/clubs/7.png"),
                 Card(8, None, "assets/clubs/8.png"), Card(9, None, "assets/clubs/9.png"),
                 Card(10, None, "assets/clubs/10.png"), Card(10, None, "assets/clubs/jack.png"),
                 Card(10, None, "assets/clubs/queen.png"), Card(10, None, "assets/clubs/king.png"),
                 Card(11, 1, "assets/clubs/ace.png"), Card(2, None, "assets/diamonds/2.png"),
                 Card(3, None, "assets/diamonds/3.png"), Card(4, None, "assets/diamonds/4.png"),
                 Card(5, None, "assets/diamonds/5.png"), Card(6, None, "assets/diamonds/6.png"),
                 Card(7, None, "assets/diamonds/7.png"), Card(8, None, "assets/diamonds/8.png"),
                 Card(9, None, "assets/diamonds/9.png"), Card(10, None, "assets/diamonds/10.png"),
                 Card(10, None, "assets/diamonds/jack.png"), Card(10, None, "assets/diamonds/queen.png"),
                 Card(10, None, "assets/diamonds/king.png"), Card(11, 1, "assets/diamonds/ace.png"),
                 Card(2, None, "assets/spades/2.png"), Card(3, None, "assets/spades/3.png"),
                 Card(4, None, "assets/spades/4.png"), Card(5, None, "assets/spades/5.png"),
                 Card(6, None, "assets/spades/6.png"), Card(7, None, "assets/spades/7.png"),
                 Card(8, None, "assets/spades/8.png"), Card(9, None, "assets/spades/9.png"),
                 Card(10, None, "assets/spades/10.png"), Card(10, None, "assets/spades/jack.png"),
                 Card(10, None, "assets/spades/queen.png"), Card(10, None, "assets/spades/king.png"),
                 Card(11, 1, "assets/spades/ace.png"), Card(2, None, "assets/hearts/2.png"),
                 Card(3, None, "assets/hearts/3.png"), Card(4, None, "assets/hearts/4.png"),
                 Card(5, None, "assets/hearts/5.png"), Card(6, None, "assets/hearts/6.png"),
                 Card(7, None, "assets/hearts/7.png"), Card(8, None, "assets/hearts/8.png"),
                 Card(9, None, "assets/hearts/9.png"), Card(10, None, "assets/hearts/10.png"),
                 Card(10, None, "assets/hearts/jack.png"), Card(10, None, "assets/hearts/queen.png"),
                 Card(10, None, "assets/hearts/king.png"), Card(11, 1, "assets/hearts/ace.png")]
        return cards
