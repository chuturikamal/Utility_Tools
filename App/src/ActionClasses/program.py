import time
import sys
from src.utilityClasses.utilClass import utilClass
from src.ActionClasses.OsCommands import OsCommands
class program:
	def __init__(self):
		self.osCommands = OsCommands()
		global ListOfActions
		global exitList
		self.util = utilClass()
		ListOfActions = ["who am i Command", 
						"present working directory Command", 
						"LS Command"]
		exitList = ['Exit', 'continue']

	def Start(self):
		while True:
			self.printCommands()
			opt = int(input('Give Option'))
			self.util.printMessage('Option selected is :')
			opt = opt - 1
			self.printMessage(ListOfActions[opt])
			
			self.osCommands.RunOption(opt)
			self.printCommands(1)
			opt = int(input('Choose Option'))

			if opt == 1:
				break
			elif opt == 2:
				self.util.printMessage('Continuing')
			else:
				self.util.printMessage('wrong option')
				break
			self.osCommands.RunOption(3)

	def printCommands(self, opt = 0):
		idx = 0
		self.util.printMessage('Select Commands by sequence\r\n')
		List = []
		if opt == 0:
			List = ListOfActions
		elif opt == 1:
			List = exitList

		for idx, loop in enumerate(List, start = 1):
			self.util.printMessage(str(idx) + '. ' + loop + '\r\n')
			time.sleep(.2)

	