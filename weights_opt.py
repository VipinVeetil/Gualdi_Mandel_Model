"""
	Please feel free to use the code without citing or crediting me.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Author: Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: Weights Opt
	Module description: compute network weights to maximize output, given input prices
	input price along with input weights determine input quantitities
	input quantities along with production function parameters determine output
	
	The code agentizes the model developed by Gualdi and Mandel in their paper "On the emergence of scale-free production networks", available here http://arxiv.org/abs/1509.01483

"""

from __future__ import division
import economic_functions as ef
import parameters
import numpy as np
from scipy.optimize import minimize


class WeightsOptimization(object):
	def __init__(self):
		self.ef = ef.EconomicFunctions()
		self.CES_exponent = parameters.CES_exponent
		self.cobb_douglas_exponents = parameters.cobb_douglas_exponents
		self.method = parameters.weights_optimization_method


	def transform(self, x):
		y = x ** 2 / (1 + x **2)
		z = np.hstack((1-sum(y), y))
		return z

	def F(self, weights, input_prices):
		weights_tranformed = self.transform(weights)
		non_labor_inputs = weights_tranformed[1:] / input_prices[1:]
		CES_output = self.ef.CES(non_labor_inputs, self.CES_exponent)
		labor_input = weights_tranformed[0] / input_prices[0]
		cobb_douglas_quantities = [labor_input, CES_output]
		value  = self.ef.cobb_douglas(cobb_douglas_quantities, self.cobb_douglas_exponents)
		return -value
		
	def optimize(self, seed_weights, prices):
		opt = minimize(self.F,np.array(seed_weights), args=(np.array(prices),), method =  self.method)
		optimal_weights = self.transform(opt.x)
		for weight in optimal_weights:
			assert weight >= 0.000
		return optimal_weights
