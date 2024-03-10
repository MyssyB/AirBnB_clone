#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    
    def do_quit(self, quit):
        '''to exit intepreter'''
        return True

    do_exit = do_quit








if __name__ == '__main__':
    HBNBCommand().cmdloop()
