class Player:
    def __init__(self):
        self.cards = []

    # todo delete if unused
    def get_cards(self):
        return self.cards

    def set_card(self, card):
        self.cards.append(card)

    def count_points(self):
        points = 0
        for card in self.cards:
            points += card.get_value()
        return points
