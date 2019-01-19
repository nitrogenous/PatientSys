from numpy import exp, array, random, dot
import matplotlib.pyplot as plt

class NeuralNetwork():
	
	def __init__(self):
		self.weight = 2 * random.random((3,1)) - 1

	def sigmoid(self,x):
		return 1 / (1+exp(-x))

