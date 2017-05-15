from troop import *

class Territory(object):

	def __init__(self, unique_id, connection_ids):
		self.troops = []
		self.unique_id = unique_id
		self.connection_ids = connection_ids
		self.connections = []
		self.occupant = None

	def __str__(self):
		return 'the territory with the unique_id {}, it is connected to {}, has {} troops and it is occupied by {}'.format(self.unique_id, self.connection_ids, len(self.troops), self.occupant) 

	def add_troop(self, troop):
		self.troops.append(troop)

	def remove_troop(self, troop):
		self.troops = [t for t in self.troops if t != troop]

	def number_of_troops(self):
		return len(self.troops)

	def add_occupant(self, player):
		self.occupant = player


