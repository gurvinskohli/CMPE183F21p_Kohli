# The container class stores the transaction that was entered by the user
# This class also loads and displays the encription status
from importlib.abc import MetaPathFinder
import sys
import hashlib
import subprocess
import datetime
import statistics
import time

class Container:
	def __init__(self, sequence):
		self.payloadBool = False
		self.messBool = False
		self.sequence = sequence
		self.hashFunction = None
		self.previousHashFunction = None
		self.check = 0
		self.counter = time.time()
		self.MessEncription = self.LoadEncription()
		self.val = None

# This is the return function of the whole class
	def __repr__(self):
		return "Container: {}, prev_hash: {}, data: {}".format( self.hashFunction, self.previousHashFunction, self.sequence[:20])

# This is part of the validation as implemented in every class
	def InvalidBlockTest(self):
		if self.MessEncription != self.LoadEncription():
			raise ContainerException("There is a issue with the load encription")
		if self.hashFunction != self.MessEncription():
			raise ContainerException("There is an issue with the hashed message")
		else
			check = 1

# This function uses hexdigest to load the encription standard
	def LoadEncription(self):
		payloadBool = True
		return hashlib.sha256(bytearray(str(self.counter), "utf-8")).hexdigest()

# This function loads the encription of the previous function
	def MessEncription(self):
		messBool = True
		return hashlib.sha256(bytearray(str(self.previousHashFunction), "utf-8")).hexdigest()

# This function uses functionality of chaining as implemented in another class
	def Chain(self, nextMess):
		val = nextMess
		self.previousHashFunction = nextMess.hashFunction

# End can be seen called many places in the program as it equates the two encriptions
	def End(self):
		self.hashFunction = self.MessEncription()
