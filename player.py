from troop_id_gen import *
from troop import *
from random import choice as ran_choice
import operator

class Player(object):

	def __init__(self, name, initial_territories, starting_troop_number, troop_gen):
		self.name = name
		self.troops = []
		self.unactivated_troops = []
		self.dead_troops = []
		self.troop_gen = troop_gen
		#this is an array of all territories this playwer will recieve
		self.territories = initial_territories
		for terrtory in self.territories:
			terrtory.add_occupant(self)
		#create an initial allotment of troops and add them to the troop array
		#the unique_id won't be very unique here
		for i in range(starting_troop_number):
			self.unactivated_troops.append(Troop(self.troop_gen.get_unique_id(), self))
		#add a single troop to each of the inital territories
		for terrtory in self.territories:
			self.activate_troop(terrtory)


	def __str__(self):
		return self.name

	def __bool__(self):
		return len(self.unactivated_troops) > 0

	def place_unactivated_troop_rand(self):
		if self:
			self.activate_troop(ran_choice(self.territories))

	def place_unactivated_troop_deterministic(self):
		#this method will place troops in territories based on a ditirmisitc algorithm.
		border_danger = {}
		if self:
			for terrtory in self.territories:
				border_danger[terrtory.unique_id] = 0
				for connected_territory in terrtory.connections:
					if connected_territory.occupant != self:
						border_danger[terrtory.unique_id] += connected_territory.number_of_troops()
				border_danger[terrtory.unique_id] -= terrtory.number_of_troops()
		most_at_risk = max(border_danger, key = border_danger.get)
		#print(border_danger)
		for terrtory in self.territories:
			if terrtory.unique_id == most_at_risk:
				self.activate_troop(terrtory)


	def activate_troop(self, terrtory):
		self.unactivated_troops[0].add_to_territory(terrtory)
		self.troops.append(self.unactivated_troops[0])
		self.unactivated_troops.remove(self.unactivated_troops[0])

	def get_new_armies(self):
		new_troops = len(self.territories) // 3
		if new_troops < 3:
			new_troops = 3
		for i in range(new_troops):
			self.unactivated_troops.append(Troop(self.troop_gen.get_unique_id(), self))
		while self:
			self.place_unactivated_troop_deterministic()

	def attack(self):
		print('this method will determin who to attack with how many troops')

	def fortify_territory(self):
		print('this method will fortify territories')

	def add_territory(self, terrtory):
		self.territories.append(terrtory)
		terrtory.add_occupant(self)

	def lose_territory(self, terrtory):
		#when the territory is lost, the player that adds it will call this method and reset the occupant
		self.territories.remove(terrtory)