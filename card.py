class Card:
    def __init__(self, value, second_value, path):
        # self.suit = suit
        # self.name = name
        self.value = value
        self.second_value = second_value
        self.path = path
        self.on_deck = True
        self.visible = True

    # def get_suit(self):
    #     return self.suit
    #
    # def get_name(self):
    #     return self.name

    def get_value(self):
        return self.value

    def get_second_value(self):
        return self.second_value

# todo to delete if unused
    def get_path(self):
        return self.path

    def is_on_deck(self):
        return self.is_on_deck

    def set_on_deck(self, on_deck):
        self.on_deck = on_deck

    def is_visible(self):
        return self.visible

    def set_visible(self, visible):
        self.visible = visible
