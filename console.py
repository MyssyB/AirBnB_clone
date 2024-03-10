#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    
    def do_help(self, arg):
        '''Displays help with commands'''
        return True
    
    def do_quit(self, quit):
        '''Quit command to exit the program'''
        return True
    
    def do_emptyline(self, arg):
        '''Method called on an input line when command is not recognized'''
        self.do_emptyline = 'ENTER'




    EOF = 'EOF'


if __name__ == '__main__':
     HBNBCommand().cmdloop()
