import time
from src.utilityClasses.utilClass import printMessage
from src.ActionClasses.OsCommands import OsCommands
class program:
	def __init__(self):
		self.osCommands = OsCommands()
		global ListOfActions
		global exitList
		ListOfActions = ["who am i Command", 
						"present working directory Command", 
						"LS Command"]
		exitList = ['Exit', 'continue']
		self.osCommands.RunOption(3)

	def Start(self):
		while True:
			self.printCommands()
			opt = int(input('Give Option'))
			printMessage('Option selected is :')
			opt = opt - 1
			printMessage(ListOfActions[opt])
			self.osCommands.RunOption(3)
			self.osCommands.RunOption(opt)
			self.printCommands(1)
			opt = int(input('Choose Option'))

			if opt == 1:
				self.osCommands.RunOption(3)
				break
			elif opt == 2:
				printMessage('Continuing')
			else:
				printMessage('wrong option')
				self.osCommands.RunOption(3)
				break
			self.osCommands.RunOption(3)

	def printCommands(self, opt = 0):
		idx = 0
		printMessage('Select Commands by sequence\r\n')
		List = []
		if opt == 0:
			List = ListOfActions
		elif opt == 1:
			List = exitList

		for idx, loop in enumerate(List, start = 1):
			printMessage(str(idx) + '. ' + loop + '\r\n')
			time.sleep(.2)

	