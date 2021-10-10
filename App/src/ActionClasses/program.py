import time
import sys
from OsCommands import OsCommands
class program:
	def __init__(self):
		self.osCommands = OsCommands()
		global ListOfActions
		global exitList
		ListOfActions = ["who am i Command", 
						"present working directory Command", 
						"LS Command"]
		exitList = ['Exit', 'continue']

	def Start(self):
		while True:
			self.printCommands()
			opt = input('Give Option')
			self.printMessage('Option selected is :')
			opt = opt - 1
			self.printMessage(ListOfActions[opt])
			sys.stdout.flush()
			self.osCommands.RunOption(opt)
			self.printCommands(1)
			opt = input('Choose Option')

			if opt == 1:
				break
			elif opt == 2:
				self.printMessage('Continuing')
			else:
				self.printMessage('wrong option')

				break

	def printCommands(self, opt = 0):
		idx = 0
		self.printMessage('Select Commands by sequence')
		List = []
		if opt == 0:
			List = ListOfActions
		elif opt == 1:
			List = exitList

		for idx, loop in enumerate(List, start = 1):
			self.printMessage(str(idx) + '. ' + loop)
			time.sleep(.2)

	def printMessage(self, message):
		sys.stdout.write(message)
	
	