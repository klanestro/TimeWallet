#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hour_work.py
#  
#  Copyright 2012 Talisman <KlanestroTalisman@gmail.com>

from Hour_Object import *

def make_a_hour_offer(n = 1):
	""" this gets data from the user and creates a new hour object
	offer is that you have hours that you have worked
	n = the number of hours in question"""
	
	h = Hour()
	h.denomination = n
	print "what is the event and what did you do?"
	h.event = raw_input()
	print "What is the value of your hours?"
	h.veq = int(raw_input())  """ Hour.veq is Value Event Quality.. See
									the Mental Bank Concept,- Talisman"""

	
	return h

print make_a_hour_offer()

