
"""
	Please feel free to use the code without citing or crediting me.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Author: Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: parameters
	Module description: parameters of the model
	
	The code agentizes the model developed by Gualdi and Mandel in their paper "On the emergence of scale-free production networks", available here http://arxiv.org/abs/1509.01483

"""

from __future__ import division


number_of_firms = 100
time_steps = 100
CES_exponent = 0.8
cobb_douglas_exponents = [0.3, 0.7]
labor = 1000
barabasi_albert_graph_parameter = 2
weights_optimization_method = 'Nelder-Mead'
percent_firms_change_weights = 1