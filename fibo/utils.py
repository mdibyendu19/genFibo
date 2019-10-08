import math


def generateFib(num):
	phi = (1 + math.sqrt(5)) / 2; 
	return int(round(math.pow(phi, int(num))/math.sqrt(5)))
