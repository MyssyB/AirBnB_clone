#!/usr/bin/python3
import cmd
from models import base_model


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

class BaseModel:
    '''creates a new instance of BaseModel'''
    
    def create(self):
        pass

    def show(self):
        pass

    def destroy(self):
        pass

    def all(self):
        pass

    def update(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
