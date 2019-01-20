from numpy import exp, array, random, dot
import matplotlib.pyplot as plt
import sys, json

class NeuralNetwork():
	
	def __init__(self):
		self.weight = 2 * random.random((5,1)) - 1

	def sigmoid(self,x):
		return 1 / (1+exp(-x))

	def sigmoid_derivative(self,x):
		return x * (1-x)

	def think(self,inputs):
		return self.sigmoid(dot(inputs,self.weight))

	def train(self,trainData_inputs,trainData_outputs,epochs):
		for epoch in range(epochs):
			predict = self.think(trainData_inputs)
			bias = trainData_outputs - predict
			adjustment = dot(trainData_inputs.T, bias * self.sigmoid_derivative(predict))
			self.weight += adjustment


neural = NeuralNetwork()

userData = sys.argv[1]
userData = json.loads(userData)

# print neural.weight










trainData_inputs = array([
	[0.0,0.0,0.0,1.0,0.9166666667],
	[1.0,0.0,1.0,0.0,0.2666666667],
	[0.0,1.0,0.0,0.0,0.45],
	[1.0,0.0,0.0,0.0,0.8166666667],
	[1.0,1.0,1.0,0.0,0.35],
	[0.0,0.0,1.0,0.0,0.6833333333],
	[1.0,0.0,0.0,1.0,0.3166666667],
	[0.0,1.0,0.0,0.0,0.75],
	[0.0,0.0,0.0,1.0,0.5],
	[0.0,1.0,1.0,1.0,0.9666666667],
])
trainData_outputs = array([[
	0.3833333333,
	0.4533333333,
	0.29,
	0.3633333333,
	0.67,
	0.3366666667,
	0.4633333333,
	0.35,
	0.3,
	0.7933333333,
]]).T

neural.train(trainData_inputs,trainData_outputs, 10000)

# print neural.weight

print neural.think(array([float(userData['sport']),float(userData['tobacco']),float(userData['alcohol']),float(userData['familyHistory']),float(userData['physicalAvg'])]))