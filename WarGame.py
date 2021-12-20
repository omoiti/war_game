import random
from Card import Card


class WarGame:
    """The class creates a WarGame object that contains the logic for playing the War card game"""
    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        """
        Creates a list of 52 card objects for a deck of cards

        Returns:
            list: List with 52 Card objects
        """
        card_array = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        rank_value_dict = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
                           "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
        for suit in suits:
            for rank, value in rank_value_dict.items():
                card_array.append(Card(rank, suit, value))
        return card_array

    def deal_cards(self, player1, player2):
        """
        Assigns player1 and player2 cards (26 cards each)

        Args:
            player1 (Player): Player 1 object
            player2 (Player): Player 2 object
        """
        # Deck is shuffled
        random.shuffle(self.deck)

        # Deck is split into half for each player
        player1.cards = self.deck[:len(self.deck) // 2]
        player2.cards = self.deck[len(self.deck) // 2:]

    def play(self, player1, player2):
        """
        Plays games between Player 1 and Player 2 until there is a winner
        Args:
            player1 (Player): Player 1 object
            player2 (Player): Player 2 object
        """
        winner = None
        while not winner:
            # Each player puts down one card
            print(
                f"{player1.name} draws a {player1.cards[0].rank} of {player1.cards[0].suit}")
            print(
                f"{player2.name} draws a {player2.cards[0].rank} of {player2.cards[0].suit}")

            # The value of each card is checked and player who has higher rank takes card
            if player1.cards[0].value > player2.cards[0].value:
                print("Player 1 wins round")
                # Player 1 adds both cards to bottom of deck
                player1.cards.append(player2.cards.pop(0))
                player1.cards.append(player1.cards.pop(0))
            elif player2.cards[0].value > player1.cards[0].value:
                print("Player 2 wins round")
                # Player 2 adds both cards to bottom of deck
                player2.cards.append(player1.cards.pop(0))
                player2.cards.append(player2.cards.pop(0))
            else:
                # Flag that denotes a time occurred
                tie = True
                # Variable used to track the amount of ties that occur for selecting the proper card index to compare
                tie_count = 1

                print(f"There is a tie!")

                # When there is a tie, 4 cards total are put down and the 4th card decides the tie
                while tie:
                    player1_idx = tie_count * \
                        3 if len(player1.cards) > tie_count * 3 else 0
                    player2_idx = tie_count * \
                        3 if len(player1.cards) > tie_count * 3 else 0
                    if len(player1.cards) >= 4 and len(player2.cards) >= 4 and player1.cards[player1_idx].value > player2.cards[player2_idx].value:
                        print(
                            f"Player 1 draws a {player1.cards[player1_idx].rank} of {player1.cards[player1_idx].suit}")
                        print(
                            f"Player 2 draws a {player2.cards[player2_idx].rank} of {player2.cards[player2_idx].suit}")
                        print(f"Player 1 wins round")
                        player1.cards.extend(player2.cards[0: player2_idx + 1])
                        player2.cards = player2.cards[player2_idx + 1:]
                        tie = False
                    elif len(player1.cards) >= 4 and len(player2.cards) >= 4 and player1.cards[tie_count * 3].value < player2.cards[player2_idx].value:
                        print(
                            f"Player 1 draws a {player1.cards[player1_idx].rank} of {player1.cards[player1_idx].suit}")
                        print(
                            f"Player 2 draws a {player2.cards[player2_idx].rank} of {player2.cards[player2_idx].suit}")
                        print("Player 2 wins round")
                        player2.cards.extend(player1.cards[0: player1_idx + 1])
                        player1.cards = player1.cards[player1_idx + 1:]
                        tie = False
                    elif player1.cards[player1_idx].value > player2.cards[-1].value:
                        print(
                            f"Player 1 draws a {player1.cards[player1_idx].rank} of {player1.cards[player1_idx].suit}")
                        print(
                            f"Player 2 draws a {player2.cards[-1].rank} of {player2.cards[-1].suit}")
                        print(f"Player 1 wins round")
                        player1.cards.extend(player2.cards[0:])
                        player2.cards = []
                        tie = False
                    elif player2.cards[tie_count * 3].value > player1.cards[-1].value:
                        print(
                            f"Player 1 draws a {player1.cards[-1].rank} of {player1.cards[-1].suit}")
                        print(
                            f"Player 2 draws a {player2.cards[player2_idx].rank} of {player2.cards[player2_idx].suit}")
                        print("Player 2 wins round")
                        player2.cards.extend(player1.cards[0:])
                        player1.cards = []
                        tie = False
                    else:
                        tie_count += 1
            # Print new line to denote an end of a round
            print(f"Player 1 has {len(player1.cards)} cards")
            print(f"Player 2 has {len(player2.cards)} cards")
            input("Press any character to continue...")
            print("\n")

            # Checks if there is a winner of the game (if a player has all 52 cards)
            if len(player1.cards) == 52:
                winner = player1
            elif len(player2.cards) == 52:
                winner = player2
            else:
                winner = None
        print(f"{winner.name} wins!")
