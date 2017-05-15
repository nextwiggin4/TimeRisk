from player import *
from troop import *
from troop_id_gen import *
from map import *
from dice import *

class Risk_Sim(object):

	def __init__(self, player_names):
		self.world_map = Map()
		territory_split = self.world_map.split_deck(len(player_names))
		self.players = []

		self.id_generator = Troop_ID_Gen()
		for i, name in enumerate(player_names):
			self.players.append(Player(name, territory_split[i], 20, self.id_generator))


		while any(self.players):
			for player in self.players:
				player.place_unactivated_troop_rand()



	def play_single_turn(self):
		print('this will play a single turn')

	def play_to_complete(self):
		print('this will play the simulation to complection')

	def play_to_turn_number(self, turn):
		print('this method will play the game to the specific turn {}'.format(turn))



game = Risk_Sim(['Captain Furlo', 'Captain Douche Nozzel',])

print(game.world_map.world_status())
#print(game.world_map.territory_connections())

game.players[0].get_new_armies()
#game.players[0].place_unactivated_troop_deterministic()

print(game.world_map.world_status())

#game.play_to_turn_number(100)
