from territory import *
#from troop import *
from random import randint


class Map(object):

	def __init__(self):
		self.territories = []
		self.territories.append(Territory(0,(1,3,4)))
		self.territories.append(Territory(1,(0,2,4,5)))
		self.territories.append(Territory(2,(1,5)))
		self.territories.append(Territory(3,(0,4)))
		self.territories.append(Territory(4,(0,1,3,5)))
		self.territories.append(Territory(5,(1,2,4)))
		#using a seried of loops, add the reference for each connectiong territory
		for territory in self.territories:
			#for each terriotry that exisits
			for connection in territory.connection_ids:
				#itirate through each connection id
				for connection_territory in self.territories:
					#compare the connection id to each territories id. If they match, add the terriotry refrence to the connected territory
					if connection == connection_territory.unique_id:
						territory.connections.append(connection_territory)

	def split_deck(self, number_of_players):
		temp_terr_list = self.territories[:]
		return_list = []
		player = 0
		for i in range(number_of_players):
			return_list.append([])
		while len(temp_terr_list) > 0:
			temp_terr = temp_terr_list[randint(0,len(temp_terr_list)-1)]
			return_list[player%number_of_players].append(temp_terr)
			player += 1
			temp_terr_list.remove(temp_terr)

		return return_list

	def world_status(self):
		return_string = 'the status is: \n'
		for territory in self.territories:
			return_string += str(territory)
			return_string += '\n'

		return return_string

	def territory_connections(self):
		return_string = "the worlds connections: \n"
		for territory in self.territories:
			return_string += 'the territory with id {} is connected to '.format(territory.unique_id)
			for connection in territory.connections:
				return_string += " {},".format(connection.unique_id)
			return_string += "\n"

		return return_string