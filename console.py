#!/usr/bin/python3
"""
consol prjct,
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter class,"""
    prompt = '(hbnb) '
    def do_EOF(self, ag):
        """'ctrl + d'end of file (to exit)"""
        print()
        return True

    def help_quit(self):
        """
        show the msg,
        """
        print("Quit command to exit the program")
        print()

    def emptyline(self):
        """do nothing (emtyline)"""
        pass

    def do_quit(self, ag):
        """
        to ext the prgram,
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
