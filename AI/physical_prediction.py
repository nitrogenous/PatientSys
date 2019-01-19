from numpy import exp, array, random, dot
import matplotlib.pyplot as plt

class NeuralNetwork():
	
	def __init__(self):
		self.weight = 2 * random.random((3,1)) - 1

	def sigmoid(self,x):
		return 1 / (1+exp(-x))

	def sigmoid_derivative(sef,x):
		return x * (1-x)

	def train(self,trainData_inputs,trainData_outputs,epochs):
	for epoch in range(epochs):
		predict = self.think(trainData_inputs)
		bias = trainData_outputs - predict
		adjustment = dot(trainData_inputs.T, bias * self.sigmoid_derivative(predict))
		self.weight += adjustment