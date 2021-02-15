#!/usr/bin/python3

import os
import sys
import re

def main():
    while True:
        os.write(1,("$").encode())
        inp = myReadline()
        if inp.equals("exit"):
            break
        else:
            forkFunction(myTokenizer(inp))




#Method to turn the user's input into a string
def myReadline():
    global buf

    #Making sure the buffer exists
    if buf== None:
        buf = read(0,100)

    convString = ''
    i = 0
    while len(buf):

        #once we get to the end, we reset the buffer and return
        if buf[i] == '\n': 
            buf = buf[i+1: len(buf)]
            return convString

        convString += chr(buf[i])

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
        else:
            arg += input[i]

        i = i+1

    return argList


def forkFunction(argList):
    pid = os.getpid()

    rc = os.fork()

    if rc < 0:
        os.write(1, ("Fork error %d\n").encode())
        sys.exit(1)

    elif rc == 0:
        
