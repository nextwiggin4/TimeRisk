from random import randint

class Dice(object):

	def __init__(self):
		#self.turn is the internal index
		self.turn = 0
		#create an empty array
		self.results = []
		self.results.append(self.roll())

	def roll_for_turn(self, turn):
		#self.turn = turn
		try:
			return self.results[turn]
		except IndexError:
			for x in range(0,turn-len(self.results) + 1):
				self.results.append(self.roll())
			return self.results[turn]			

	def next_roll(self):
		self.turn += 1
		try:
			return self.results[self.turn]
		except IndexError:
			self.results.append(self.roll())
			return self.results[self.turn]

	def set_turn_index(self, turn):
		self.turn = turn

	def number_of_rols(self):
		return len(self.results)

	def roll(self):
		return randint(0,5)