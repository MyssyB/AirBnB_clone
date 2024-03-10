#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, line):
        '''EOF defines the end of file'''
        return True
    
    def emptyline(self):
        return cmd.Cmd.emptyline(self)

    def do_quit(self, quit):
        '''Quit command to exit the program'''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
