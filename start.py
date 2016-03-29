"""
	Please feel free to use the code without citing or crediting me.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Author: Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: Start
	Module description: starts a single run of simulation
	
	The code agentizes the model developed by Gualdi and Mandel in their paper "On the emergence of scale-free production networks", available here http://arxiv.org/abs/1509.01483

"""
from __future__ import division
import run
import random
import matplotlib.pyplot as plt
from operator import add
import parameters

class Start(object):
	def __init__(self):
		self.run = run.Run()
	
	def create_economy(self):
		self.run.create_economy()

	def forward_in_time(self):
		self.run.time_steps()



start_instance = Start()
""" instantiate start """
start_instance.create_economy()
""" create economy """
start_instance.forward_in_time()
""" run it forward in time """




plt.plot(start_instance.run.economy.household.wealth)
plt.title('Household Wealth')
plt.show()

plt.plot(start_instance.run.wealth)
plt.title('Firms Wealth')
plt.show()

plt.plot(start_instance.run.wealth_cv)
plt.title('Firms Wealth CV')
plt.show()

plt.plot(start_instance.run.prices_mean)
plt.title('Mean Price')
plt.show()


plt.plot(start_instance.run.prices_cv)
plt.title('CV price')
plt.show()

