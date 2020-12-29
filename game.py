from dealer import Dealer
from deck import Deck
from player import Player


class Game:
    def __init__(self, p_card_l1, p_card_l2, p_card_l3, p_card_l4, p_card_l5,
                        d_card_l1, d_card_l2, d_card_l3, d_card_l4, d_card_l5,
                        player_score_label, dealer_score_label):

        self.player_card_labels = [p_card_l1, p_card_l2, p_card_l3, p_card_l4, p_card_l5]
        self.dealer_card_labels = [d_card_l1, d_card_l2, d_card_l3, d_card_l4, d_card_l5]

        self.player_score_label = player_score_label
        self.dealer_card_labels = dealer_score_label
        #   cards
        self.deck_of_cards = Deck()
        self.deck_of_cards.shuffle()

        #   players
        self.player = Player()
        self.dealer = Dealer()

    def get_cards(self):
        pass
