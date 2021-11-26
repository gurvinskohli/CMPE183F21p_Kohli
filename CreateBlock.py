# This class is used througout the program to create a block when user desires to
# The blocks created are not added to the chain until the user states it
from importlib.abc import MetaPathFinder
import sys
import hashlib
import subprocess
import datetime
import statistics
import time

class CreateBlock:
	def __init__(self, *input):
		if input:
			for mess in input:
				self.BlockInput(mess)
		self.messages = []
		self.endMessage = None
		self.finish = None
		self.counter = None
		self.previousHashFunction = None
		self.hashFunction = None
		self.temp = 0
		self.newTemp = 0

# This is the return function of the CreateBlock class
	def __repr__(self):
		return 'Block Output - Hash Value: {}, previous Hash Value: {}, Creation Time: {}'.format( self.hashFunction, self.previousHashFunction, self.counter)

# This function determines the layout of the hash
	def Layout(self):
		return hashlib.sha256(bytearray(str(self.previousHashFunction) + self.messages.hashFunction, "utf-8")).hexdigest()

# This funcion is used throuout the program to input data to the block
	def BlockInput(self, input):
		if self.messages:
			input.Chaining(self.messages[-1])
		input.end()
		input.InvalidBlockTest()
		self.messages.append(input)

# This function is practically assisting the chaing but the chain class actually does it
	def Chaining(self, block):
		temp = self.previousHashFunction
		self.previousHashFunction = block.hashFunction
		newTemp = block.hashFunction

# This class does validation at the block level just like all other classes
	def InvalidBlockTest(self):
		for variable1, variable2 in self.messages:
			try:
				Variable1.InvalidBlockTest()
				if variable2 > 0 and msg.previousHashFunction == self.messages.hashFunction:
					raise CreateBlockException("There is a issue with the message of this block")

				elif variable2 < 0 and msg.previousHashFunction == self.messages.hashFunction:
					raise CreateBlockException("There is a issue with the message of this block")

				else
					raise CreateBlockException("An unkown error has occured, restart the program")

# This function is called to end a block and it returns approriprate output when the user enters the command pertaing to this
	def end(self):
		self.counter = time.time()
		self.hashFunction = self.Layout()
		self.endMessage = self.Layout()
		self.finish = self.Layout()
