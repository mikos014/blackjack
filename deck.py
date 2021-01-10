import random
from card import Card


class Deck:
    def __init__(self, card_path):
        self.card_path = card_path
        self.cards = self.load_card_graph(card_path)
        self.back = None

    def shuffle(self):
        # TODO break, text about shuffling, setting is_on_deck = True in all cards
        random.shuffle(self.cards)

    def get_card(self):
        while True:
            index = random.randint(0, 51)
            if self.cards[index].is_on_deck():
                self.cards[index].set_on_deck(False)
                return self.cards[index]

    def get_card_back_graph_path(self):
        return self.card_path + "back.png"

    @staticmethod
    def load_card_graph(card_path):
        cards = [Card(2, None, card_path + "clubs/2.png"), Card(3, None, card_path + "clubs/3.png"),
                 Card(4, None, card_path + "clubs/4.png"), Card(5, None, card_path + "clubs/5.png"),
                 Card(6, None, card_path + "clubs/6.png"), Card(7, None, card_path + "clubs/7.png"),
                 Card(8, None, card_path + "clubs/8.png"), Card(9, None, card_path + "clubs/9.png"),
                 Card(10, None, card_path + "clubs/10.png"), Card(10, None, card_path + "clubs/jack.png"),
                 Card(10, None, card_path + "clubs/queen.png"), Card(10, None, card_path + "clubs/king.png"),
                 Card(11, 1, card_path + "clubs/ace.png"), Card(2, None, card_path + "diamonds/2.png"),
                 Card(3, None, card_path + "diamonds/3.png"), Card(4, None, card_path + "diamonds/4.png"),
                 Card(5, None, card_path + "diamonds/5.png"), Card(6, None, card_path + "diamonds/6.png"),
                 Card(7, None, card_path + "diamonds/7.png"), Card(8, None, card_path + "diamonds/8.png"),
                 Card(9, None, card_path + "diamonds/9.png"), Card(10, None, card_path + "diamonds/10.png"),
                 Card(10, None, card_path + "diamonds/jack.png"), Card(10, None, card_path + "diamonds/queen.png"),
                 Card(10, None, card_path + "diamonds/king.png"), Card(11, 1, card_path + "diamonds/ace.png"),
                 Card(2, None, card_path + "spades/2.png"), Card(3, None, card_path + "spades/3.png"),
                 Card(4, None, card_path + "spades/4.png"), Card(5, None, card_path + "spades/5.png"),
                 Card(6, None, card_path + "spades/6.png"), Card(7, None, card_path + "spades/7.png"),
                 Card(8, None, card_path + "spades/8.png"), Card(9, None, card_path + "spades/9.png"),
                 Card(10, None, card_path + "spades/10.png"), Card(10, None, card_path + "spades/jack.png"),
                 Card(10, None, card_path + "spades/queen.png"), Card(10, None, card_path + "spades/king.png"),
                 Card(11, 1, card_path + "spades/ace.png"), Card(2, None, card_path + "hearts/2.png"),
                 Card(3, None, card_path + "hearts/3.png"), Card(4, None, card_path + "hearts/4.png"),
                 Card(5, None, card_path + "hearts/5.png"), Card(6, None, card_path + "hearts/6.png"),
                 Card(7, None, card_path + "hearts/7.png"), Card(8, None, card_path + "hearts/8.png"),
                 Card(9, None, card_path + "hearts/9.png"), Card(10, None, card_path + "hearts/10.png"),
                 Card(10, None, card_path + "hearts/jack.png"), Card(10, None, card_path + "hearts/queen.png"),
                 Card(10, None, card_path + "hearts/king.png"), Card(11, 1, card_path + "hearts/ace.png")]

        return cards
