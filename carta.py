class Card:
    def __init__(self, seed: str, rank: str):
        self.__seed = seed
        if seed not in ['C', 'D', 'H', 'S']: # Clubs, Diamonds, Hearts, Spades
            raise ValueError("Il seme non è valido!")

        self.__rank = rank
        if rank not in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            raise ValueError("Il valore della carta non è valido!")

    @property
    def value(self) -> int:
        if self.__rank in ["J", "Q", "K"]:
            return 10
        elif self.__rank == "A":
            return 11
        else:
            return int(self.__rank)

    @property
    def rank(self) -> str:
        return self.__rank

    def __str__(self):
        if self.__seed == "C":
            s_seed = "Fiori"
        elif self.__seed == "D":
            s_seed = "Quadri"
        elif self.__seed == "H":
            s_seed = "Cuori"
        elif self.__seed == "S":
            s_seed = "Picche"
        while self.__rank in ["J", "Q", "K", "A"]:
            if self.__rank == "K":
                s_rank = "Re"
            elif self.__rank == "Q":
                s_rank = "Regina"
            elif self.__rank == "J":
                s_rank = "Jack"
            elif self.__rank == "A":
                s_rank = "Asso"
            return f"{s_rank} di {s_seed}"
        return f"{self.rank} di {s_seed}"
