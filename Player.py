class Player:
	""" This class defines a Player object"""
	num_players = 1
	def __init__(self):
		self.name = f"Player {str(Player.num_players)}"
		self.cards = None
		Player.num_players += 1