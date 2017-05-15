from territory import *
from troop import *
from map import *

world_map = Map()

territory_split = world_map.split_deck(6)
print(len(territory_split[0]))

#for array in territory_split:
#	for territory in array:
#		print(territory)