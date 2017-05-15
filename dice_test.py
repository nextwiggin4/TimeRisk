from dice import *

d1 = Dice()

while True:
	turn = input("please select a trun to check: ")
	if turn == 'n':
		print(d1.next_roll())
	else:
		print(d1.roll_for_turn(int(turn)))
		print(d1.number_of_rols())
