import cmd2

class Shell(cmd2.Cmd):
    def __init__(self):
        super().__init__(startup_script="shell_start_up.txt")
        self.prompt = '[you]'
        self.intro = cmd2.style('Bienvenue', bold = True)


    def do_greeting(self ,_):
        '''Greet the user'''
        self.poutput(self.intro)


shell = Shell()
shell.cmdloop()
