#!/usr/bin/python3
"""
consol prjct,
"""
import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter class,"""
    prompt = '(hbnb) '
    cls_s = ["BaseModel"]

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

    def do_create(self, ag):
        """
        creat a new inst of Basemodel, save to 'json',
        """
        if not ag:
            print("** class name missing **")
        elif ag not in self.cls_s:
            print("** class doesn't exist **")
        else:
            q = eval(f"{ag}()")
            q.save()
            print(q.id)

    def do_show(self, ag):
        """
        print str representation of an inst,
        """
        ag_s = shlex.split(ag)
        if not ag_s:
            print("** class name missing **")
        elif ag_s[0] not in self.cls_s:
            print("** class doesn't exist **")
        elif len(ag_s) < 2:
            print("** instance id missing **")
        else:
            ky = f"{ag_s[0]}.{ag_s[1]}"
            odict = storage.all()
            if ky in odict:
                print(odict[ky])
            else:
                print("** no instance found **")

    def do_destroy(self, ag):
        """
        del an inst based on the cls,
        """
        ag_s = shlex.split(ag)
        if not ag_s:
            print("** class name missing **")
        elif ag_s[0] not in self.cls_s:
            print("** class doesn't exist **")
        elif len(ag_s) < 2:
            print("** instance id missing **")
        else:
            k_y = ag_s[0] + "." + ag_s[1]
            o_dict = storage.all()
            if k_y not in o_dict:
                print("** no instance found **")
                return
            del o_dict[k_y]
            storage.save()

    def do_all(self, ag):
        """
        print str all inst,
        """
        ag_s = shlex.split(ag)
        o_dict = storage.all()
        if len(ag_s) == 0:
            for ky, vl in o_dict.items():
                print(str(vl))
        elif ag_s[0] not in self.cls_s:
            print("** class doesn't exist **")
        else:
            for ky, vl in o_dict.items():
                if ky.split('.')[0] == ag_s[0]:
                    print(str(vl))

    def do_update(self, ag):
        """
        update an inst based on cls,
        """
        ag_s = shlex.split(ag)
        if not ag_s:
            print("** class name missing **")
        elif ag_s[0] not in self.cls_s:
            print("** class doesn't exist **")
        elif len(ag_s) < 2:
            print("** instance id missing **")
        else:
            k_y = ag_s[0] + "." + ag_s[1]
            o_dict = storage.all()
            if k_y not in o_dict:
                print("** no instance found **")
            elif len(ag_s) < 3:
                print("** attribute name missing **")
            elif len(ag_s) < 4:
                print("** value missing **")
            else:
                attrname = ag_s[2]
                attrval = ag_s[3]
                try:
                    attrval = eval(attrval)
                except Exception:
                    pass
                ob_j = o_dict[k_y]
                setattr(ob_j, attrname, attrval)
                ob_j.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
