from player import *
from troop import *
from troop_id_gen import *
from map import *



world_map = Map()
territory_split = world_map.split_deck(2)

id_generator = Troop_ID_Gen()
player1 = Player('Captain Furlo', territory_split[0], 20, id_generator)
player2 = Player('Captain Douche Nozzel', territory_split[1], 20, id_generator)

while player1.check_for_unactivated_troops() or player2.check_for_unactivated_troops():
	player1.place_unactivated_troop_rand()
	player2.place_unactivated_troop_rand()



#for troop in player1.troops:
#	print(troop)

#for troop in player2.troops:
#	print(troop)

print(world_map.world_status())