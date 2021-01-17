from PIL import ImageTk, Image

from dealer import Dealer
from deck import Deck
from config import *
from player import Player


class Game:
    def __init__(self, player_card_labels, dealer_card_labels, player_score_label, dealer_score_label,
                 instruction_label, b_deal, b_hit, b_stand):
        self.player_card_labels = player_card_labels
        self.dealer_card_labels = dealer_card_labels

        self.player_score_label = player_score_label
        self.dealer_score_label = dealer_score_label
        self.instruction_label = instruction_label

        self.b_deal = b_deal
        self.b_hit = b_hit
        self.b_stand = b_stand

        #   cards
        self.deck_of_cards = Deck(card_path)
        #   players
        self.player = Player()
        self.dealer = Dealer()

    def init_game(self):
        self.deck_of_cards.shuffle()
        self.prepare_players()
        self.clean_table()
        self.b_deal.unbind('<Button-1>')
        self.b_deal.config(state='disabled')
        self.b_hit.bind('<Button-1>', lambda event: self.get_next_card(player_request=True))
        self.b_hit.config(state='normal')
        self.b_stand.bind('<Button-1>', lambda event: self.player_on_stand())
        self.b_stand.config(state='normal')
        self.instruction_label.config(text="")
        self.get_next_card(player_request=True, init=True)
        self.get_next_card(player_request=False, init=True, visible=False)
        self.get_next_card(player_request=True, init=True)
        self.get_next_card(player_request=False)

    def prepare_players(self):
        self.player.prepare_to_new_round()
        self.dealer.prepare_to_new_round()

    def clean_table(self):
        for player_label in self.player_card_labels:
            player_label.place_forget()
        for dealer_label in self.dealer_card_labels:
            dealer_label.place_forget()

    def get_next_card(self, player_request, init=False, visible=True):
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
        if not init:
            self.check_if_is_21_or_more()

    def show_on_screen(self, on_player_side, card):
        card_i = Image.open(card.get_path()).resize(card_size, Image.ANTIALIAS)
        card_i_tk = ImageTk.PhotoImage(card_i)
        if on_player_side:
            index = self.player.get_current_card_index() - 1
            self.player_card_labels[index].configure(image=card_i_tk)
            self.player_card_labels[index].image = card_i_tk
            self.player_card_labels[index].place(x=player_card_layout[index][0], y=player_card_layout[index][1])
        else:
            index = self.dealer.get_current_card_index() - 1
            if not card.is_visible():
                card_i = Image.open(card_path + "back.png").resize(card_size, Image.ANTIALIAS)
                card_i_tk = ImageTk.PhotoImage(card_i)
            self.dealer_card_labels[index].configure(image=card_i_tk)
            self.dealer_card_labels[index].image = card_i_tk
            self.dealer_card_labels[index].place(x=dealer_card_layout[index][0], y=dealer_card_layout[index][1])

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
            self.dealer_score_label.config(text="Dealer = " + str(self.dealer.get_points()))

    def check_if_is_21_or_more(self):
        player_points = self.player.get_points()
        dealer_points = self.dealer.get_points()
        if player_points > 20 or dealer_points > 20:
            if player_points == 21 and dealer_points == 21:
                self.instruction_label.config(text="PUSH !")
            elif player_points == 21 or dealer_points > 21:
                self.instruction_label.config(text="You won ! Press 'DEAL' to try again.")
            elif player_points > 21 or dealer_points == 21:
                self.instruction_label.config(text="Dealer won. Press 'DEAL' to try again.")
            # end game
            self.end_game()

    def player_on_stand(self):
        self.dealer_turn()
        if self.player.get_points() < 21 and self.dealer.get_points() < 21:
            self.check_who_win()
        else:
            self.check_if_is_21_or_more()

    def end_game(self):
        self.update_score_table(player_request=False)
        self.show_dealer_hidden_card()
        self.b_deal.bind('<Button-1>', lambda event: self.init_game())
        self.b_deal.config(state='normal')
        self.b_hit.config(state='disabled')
        self.b_hit.unbind('<Button-1>')
        self.b_stand.config(state='disabled')
        self.b_stand.unbind('<Button-1>')

    def show_dealer_hidden_card(self):
        cards = self.dealer.get_cards()
        cards[0].set_visible(True)
        card_i = Image.open(cards[0].get_path()).resize(card_size, Image.ANTIALIAS)
        card_i_tk = ImageTk.PhotoImage(card_i)
        self.dealer_card_labels[0].configure(image=card_i_tk)
        self.dealer_card_labels[0].image = card_i_tk
        self.dealer.set_points(self.count_scoring(self.dealer))
        self.update_score_table(player_request=False)

    def dealer_turn(self):
        self.show_dealer_hidden_card()
        while self.dealer.is_sure_to_get_card():
            self.get_next_card(player_request=False)

    # extra method to check who has more points but under 21
    def check_who_win(self):
        self.end_game()
        if self.player.get_points() > self.dealer.get_points():
            self.instruction_label.config(text="You won ! Press 'DEAL' to try again.")
        elif self.player.get_points() < self.dealer.get_points():
            self.instruction_label.config(text="Dealer won. Press 'DEAL' to try again.")
        else:
            self.instruction_label.config(text="PUSH !")
