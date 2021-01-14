from player import Player


class Dealer(Player):

    def count_points(self, aces_as_one_point=False):
        points = 0
        for card in self.cards:
            if card.is_visible():
                if aces_as_one_point and (card.get_second_value() is not None):
                    points += card.get_second_value()
                else:
                    points += card.get_value()
        return points

    def play(self, game):
        points = super().count_points()
        while points < 17:
            game.show_next_card(player_request=False)
            points = super(Dealer, self).count_points()

