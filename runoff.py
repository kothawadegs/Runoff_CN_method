#  This code calculates the runoff based on storm rainfall. 
#  Method of computing Runoff : SCS-Curve Number Method
#  Author : Gajanan Kothawade

#  load required packages:
from __future__ import division
import math
import numpy as np 
import pandas as pd

class SCS():

	def curve_number(self):
		self.CN = 92		
		return self.CN

	def surface_retention(self):
		self.S = (25400/self.CN) - 254
		return self.S

	def initial_abstraction(self):
		#max_ret = lambda*S    for Indian conditions, initial abstraction is 0.3 * S
		self.max_ret = 0.3 * self.S
		return self.max_ret

	def read_precip_data(self,a=10):
		# method to read and return the precipitation data
		# read your actual precipitation data here:
		self.precipitation = a
		return self.precipitation

	def runoff(self):
		numerator = (self.precipitation - self.max_ret)**2
        	denominator = self.precipitation - 0.27
        	if self.precipitation <= self.max_ret:
            		Q = 0
        	else:
            		Q = numerator/denominator
        	return Q
		

