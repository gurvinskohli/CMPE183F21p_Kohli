# This class provides the functionality to connect the blocks using a hash pointer
# In blockchain terms the hash pointer acts as the hash function between blocks
from importlib.abc import MetaPathFinder
import sys
import hashlib
import subprocess
import datetime
import statistics
import time

class Chain:
	def __init__(self):
		self.block1 = None
		self.start = False
		self.check = None
		self.stub = []

# This is the return function of the class
	def __repr__(self):
		return "TheChain: {}".format(self.stub)

# This uses the insert functions from the CreateBlock class to do chaining
	def Insert(self, input):
		input.end()
		input.InvalidBlockTest()
		if self.stub && start:
			input.previousHashFunction = self.stub[-1].hashFunction
		self.stub.append(input)

# At every level of the block this does validation
	def InvalidBlockTest(self):
		for element1, element2 in self.stub:
			try:
				block.InvalidBlockTest()
			except InvalidBlock as check:
				raise ChainException("There is an issue with an element in the blockchain")
		start = True
