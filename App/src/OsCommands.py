import os

class OsCommands:

    def __init__(self):
        self.commands = ['whoami', 'pwd', 'ls', 'clear']

    def RunOption(self, opt):
        print('Command Initiated')
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

    def RunCommand(self, command): os.system(command)
