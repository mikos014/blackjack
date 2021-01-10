from PIL import ImageTk, Image

from dealer import Dealer
from deck import Deck
from config import *
from player import Player


class Game:
    def __init__(self, player_card_labels, dealer_card_labels, player_score_label, dealer_score_label,
                 instruction_label):
        self.player_card_labels = player_card_labels
        self.dealer_card_labels = dealer_card_labels

        self.player_score_label = player_score_label
        self.dealer_score_label = dealer_score_label
        self.instruction_label = instruction_label

        #   cards
        self.deck_of_cards = Deck(card_path)
        self.deck_of_cards.shuffle()

        #   players
        self.player = Player()
        self.dealer = Dealer()

    def show_initial_cards(self):
        # for i in range(2):
        self.show_next_card(player_request=True)
        self.show_next_card(player_request=False, visible=False)
        self.show_next_card(player_request=True)
        self.show_next_card(player_request=False)

    def show_next_card(self, player_request, visible=True):
        card = self.deck_of_cards.get_card()
        card.set_visible(visible)

        if player_request:
            current_player = self.player
        else:
            current_player = self.dealer

        current_player.set_card(card)
        self.show_on_screen(player_request, card)

        current_player.set_points(self.count_scoring(current_player))
        self.update_score_table(player_request)
        self.check_if_is_21_or_more()

    def show_on_screen(self, on_player_side, card):
        card_i = Image.open(card.get_path()).resize(card_size, Image.ANTIALIAS)
        card_i_tk = ImageTk.PhotoImage(card_i)
        if on_player_side:
            self.player_card_labels[self.player.get_current_card_index() - 1].configure(image=card_i_tk)
            self.player_card_labels[self.player.get_current_card_index() - 1].image = card_i_tk
        else:
            if card.is_visible():
                self.dealer_card_labels[self.dealer.get_current_card_index() - 1].configure(image=card_i_tk)
                self.dealer_card_labels[self.dealer.get_current_card_index() - 1].image = card_i_tk

    def count_scoring(self, current_player):
        points = current_player.count_points()
        if points > 21:
            if current_player.get_number_of_aces() > 0:
                return current_player.count_points(aces_as_one_point=True)
            else:
                return points
        else:
            return points

    def update_score_table(self, player_request):
        if player_request:
            self.player_score_label.config(text="You = " + str(self.player.get_points()))
        else:
            self.dealer_score_label.config(text="Dealer = " + str(self.count_scoring(self.dealer)))

    def check_if_is_21_or_more(self):
        player_points = self.player.get_points()
        dealer_points = self.dealer.get_points()
        if player_points > 20 or dealer_points > 20:
            if player_points == 21 or dealer_points > 21:
                self.instruction_label.config(text="You won ! Press 'DEAL' to try again.")
            elif player_points > 21 or dealer_points == 21:
                self.instruction_label.config(text="Dealer won. Press 'DEAL' to try again.")
            self.update_score_table(player_request=False, with_invisible_card=True)
            self.show_dealer_hidden_card()
            # end game

    def player_on_stand(self):
        self.dealer.play()
        # dealer's turn

    def show_dealer_hidden_card(self):
        cards = self.dealer.get_cards()
        cards[0].set_visible(True)
        card_i = Image.open(cards[0].get_path()).resize(card_size, Image.ANTIALIAS)
        card_i_tk = ImageTk.PhotoImage(card_i)
        self.dealer_card_labels[0].configure(image=card_i_tk)
        self.dealer_card_labels[0].image = card_i_tk
