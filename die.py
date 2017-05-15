from random import randint


results = [0,0,0,0,0,0]

for x in range(0,1000000):

	results[randint(0,5)] += 1

print(results)