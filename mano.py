from carta import Card


class Hand:
    def __init__(self):
        self.__hand = []

    def add_card(self, card: Card) -> None:
        self.__hand.append(card)

    def clean_hand(self) -> None:
        self.__hand = []

    @property
    def cards(self):
        return self.__hand

    def __str__(self):
        return ', '.join(str(card) for card in self.__hand)
