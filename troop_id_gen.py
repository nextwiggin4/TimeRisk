class Troop_ID_Gen(object):

	def __init__(self):
		self.unique_id = 0

	def get_unique_id(self):
		return_id = self.unique_id
		self.unique_id += 1
		return return_id