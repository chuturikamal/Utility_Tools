from os import system, name

from src.utilityClasses.utilClass import printMessage

class OsCommands:

    def __init__(self):
        self.commands = ['whoami', 'pwd', 'ls', 'clear']

    def RunOption(self, opt):
        printMessage('Command '+self.commands[0]+' Initiated')
        command = ''
        if(opt == 0):
            command = self.commands[0]
        elif(opt == 1):
            command = self.commands[1]
        elif(opt == 2):
            command = self.commands[2]
        elif(opt == 3):
            command = self.commands[3]
        self.RunCommand(command)

    def RunCommand(self, command): 
        printMessage('\033[0;31;0m')
        system(command)
        printMessage("\033[0m")
