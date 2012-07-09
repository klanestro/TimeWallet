#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Hour_Object.py
#  
#  Copyright 2012 Talisman <KlanestroTalisman@gmail.com>

class Hour:
	""" This class is supposed to be a virtual hour worth something"""
	def __init__(self,demand,
					value_event_quality = None,
					event = 'Anonymous',
					assumed_value = 100,
					actual_value = None,
					validated = False,
					denomination = 1):
						
		self.demand = demand
			#  this unit represents the need of the hour to be traded 1-10
	 
		self.veq = value_event_quality
		# this unit is a mezurement of the quality of the hour to something
		# like building a buiseness or a house"""
	 
		self.assumed_value = assumed_value 
		#		assumed_value : what is it worth to you to purchase an hour or labor for an hour ?

		self.actual_value = actual_value 
		#	actual_value : what did you pay or recieve for the validation of the hour

	
		self.validated = validated 
		#  this is if the hour has been labored and the payed"""
	
		self.denomination = denomination
		# how many hours are we talking about"""
	
		self.currency_conversion = currency_conversion
		# if you had to trade an hour, what whould you trade it for"""

	

