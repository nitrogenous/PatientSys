from numpy import exp, array, random, dot
import matplotlib.pyplot as plt
import sys, json

class NeuralNetwork():
	
	def __init__(self):
		self.weight = 2 * random.random((3,1)) - 1

	def sigmoid(self,x):
		return 1.0 / (1.0+exp(-x))

	def sigmoid_derivative(self,x):
		return x * (1.0-x)

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
	[1.0, 0.75, 1.00], 
	[0.0, 0.30, 0.50], 
	[0.0, 0.60, 0.75],
	[1.0, 0.45, 1.00],
	[0.0,0.30,0.75],
	[1.0,0.30,0.75],
	[0.0,0.45,0.50],
	[1.0,0.75,0.50],
	[0.0,0.75,0.75],
	[1.0,0.90,1.0],
])
trainData_outputs = array([[
	0.9166666667,
	0.2666666667,
	0.45,
	0.8166666667,
	0.35,
	0.6833333333,
	0.3166666667,
	0.75,
	0.5,
	0.9666666667,
]]).T

neural.train(trainData_inputs, trainData_outputs, 100000)

# print neural.weight

print neural.think(array([float(userData['gender']), float(userData['age']), float(userData['weight'])]))