
from WarGame import WarGame
from Player import Player

def main():
	"""
	main funtion for running game
	"""
	# Create instance of WarGame object 
	game = WarGame()

	# Create two players
	player1 = Player()
	player2 = Player()

	# Deal cards to two players (26 cards each)
	game.deal_cards(player1, player2)

	# Play game
	game.play(player1, player2)

main()


