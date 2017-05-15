from territory import *

class Troop(object):
	
	def __init__(self, unique_id, player):
		self.unique_id = unique_id
		self.generation = 0
		self.player = player
		self.active = False
		self.current_territory = None

	def __str__(self):
		return 'My unique_id is {}, my CO is {}, I am in {} and I am reporting for duty'.format(self.unique_id, self.player, self.current_territory) 

	#this function must be called for the troop to become active
	def add_to_territory(self, territory):
		self.active = True
		self.current_territory = territory
		self.current_territory.add_troop(self)

	#this function will be called by the player, change will proagate to the territory
	def change_territory(self, territory):
		self.current_territory.remove_troop(self)
		self.current_territory = territory
		self.current_territory.add_troop(self)

	#if a troop dies during a turn, it is removed from the territory
	def die(self):
		self.active = False
		self.current_territory.remove_troop(self)

		