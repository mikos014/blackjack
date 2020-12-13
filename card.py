class Card:
    def __init__(self, value, second_value, path):
        self.value = value
        self.second_value = second_value
        self.path = path
        self.is_on_deck = True

    def get_value(self):
        return self.value

    def get_path(self):
        return self.path

    def get_is_on_deck(self):
        return self.is_on_deck

    def set_is_on_deck(self, is_on_deck):
        self.is_on_deck = is_on_deck
