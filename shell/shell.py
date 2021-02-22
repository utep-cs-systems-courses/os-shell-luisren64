#!/usr/bin/python3

import os
import sys
import re

def main():
    while True:
        os.write(1,("$").encode())
        input = myTokenizer(myReadline())
        if input[0] == 'exit' or input[0] == 'Exit':
            break
        else:
            forkFunction(myTokenizer(inp))




#Method to turn the user's input into a string
def myReadline():
    input = os.read(0,100)

    convString = ''
    i = 0
    while i < len(input):

        #checking if we've reached the newline character
        if chr(input[i]) == '\n':
            return input

        convString += chr(input[i])
        i = i+1

    #if the input is empty, the resulting string is as well    
    return convString
        

def myTokenizer(input):
    argList = []
    arg = ''
    i = 0
    while (1 < len(input)):

        if input[i] ==' ':
            #We've found the end of the first command. Append it to the list
            argList.append(arg)
            arg = ''
        #This is the last command in the line. Append it
        elif (i+1)==len(input):
            argList.append(arg)
        else:
            arg += input[i]

        i = i+1

    return argList


def forkFunction(args):
    pid = os.getpid()

    rc = os.fork()

    if rc < 0:
        os.write(1, ("Fork error %d\n").encode())
        sys.exit(1)

    elif rc == 0: #child process created
        os.write(1,("Child: My pid==%d. Parent's pid=%d\n" %
                    (os.getpid(),pid)).encode())

        for dir in re.split(":",os.environ['PATH']):
            program = "%s/%s" % (dir,args[0])
            try:
                os.execve(program,args, os.environ)
            except FileNotFoundError:
                pass

            os.write(2, ("Child: Error; Could not exec %s\n" % args[0]).encode())
            sys.exit(1)

    else:
        os.write(1, ("Parent: My pid=%d. Child pid=%d\n" %
                     (pid,rc)).encode())
        childPidCode = os.wait()
        os.write(1 ("Parent : Child %d terminated with exit code %d\n" %
                    childPidCode).encode())
                
