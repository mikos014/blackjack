class Player:
    def __init__(self):
        self.cards = []
        self.current_card_index = 0
        self.number_of_aces = 0
        self.points = 0
        self.money = 100

    def get_cards(self):
        return self.cards

    def set_card(self, card):
        self.cards.append(card)
        self.current_card_index += 1
        if card.get_second_value() is not None:
            self.number_of_aces += 1

    def get_current_card_index(self):
        return self.current_card_index

    def get_number_of_aces(self):
        return self.number_of_aces

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points

    def get_money(self):
        return self.money

    def add_to_current_money(self, money):
        self.money += money

    def subtract_from_current_money(self, money):
        self.money -= money

    def count_points(self, aces_as_one_point=False):
        points = 0
        for card in self.cards:
            if aces_as_one_point and (card.get_second_value() is not None):
                points += card.get_second_value()
            else:
                points += card.get_value()
        return points

    def prepare_to_new_round(self):
        self.cards = []
        self.current_card_index = 0
        self.number_of_aces = 0
        self.points = 0
