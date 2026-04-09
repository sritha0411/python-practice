import math
def eggCartons(eggs):

	return math.ceil(eggs/12)

print(eggCartons(int(input())))