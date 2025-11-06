from tavolo import BlackjackTable
from carta import Card
from mano import Hand
from mazzo import Deck

def main():
    player_hand = Hand()
    dealer_hand = Hand()

    table = BlackjackTable(player_hand, dealer_hand)
    table.game()

if __name__ == "__main__":
    main()