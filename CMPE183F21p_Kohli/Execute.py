# The Execute class executes all the classes and functions created
# This class also does input check and executes approriprate commands pertaing to user text input
from importlib.abc import MetaPathFinder
import sys
import hashlib
import subprocess
import datetime
import statistics
import time

if __name__ == "__main__":
	Execute()

def Execute():
	counter = 0
	bool = True
	decide = ""
	addFunction = Chain()
	functionCounter = 0
	addContainer = CreateBlock()
	containerCounter = 0


	while True:
		if bool
			Print( """
									   Welcome to PyChain!!

						           ₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱

						              Commands Permitted:"Enter transaction to block"
						                                "Chain the block"
							                        "View a block"
							                        "View chaining"
							                        "Start validation"

						           ₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱

								  	Note: To exit type "e"
				 """)
		bool = False

		decide = input("Please type your command to PyChain: ")

		if decide == "Start validation":
			if addFunction.InvalidBlockTest(): print("Validation Complete")

		elif decide == "Chain the block":
			if len(addContainer.messages) > 0:
				addFunction.input(block)
				addContainer = CreateBlock()
				functionCounter += 1
			else: print("There is no data in the block")

		elif decide == "Enter transaction to block":
			addContainer.BlockInput(Message(input("What's the transaction? ")))

		elif decide == "View chaining":
			containerCounter += 1
					print("₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱")
					print(ele)
					print("₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱₱")

		elif decide == "View a block":
			index = int(input("What's the index? "))
			if len(addFunction.chain) > 0:
				try: print(addFunction)
				except: print("Sorry the request was unsucessful")

		elif decide == "e"
			break
