#!/usr/bin/env python
# coding=utf-8
def stackOutput(string, pushed=0, stack=[], newstring='', output=[]):
    if pushed==len(string):
        while len(stack)>0:
            newstring+=stack.pop()
        output.append(newstring)
    else:
        if len(stack)>0:
            newstringCopy=newstring
            stackCopy=stack[:]
            newstring+=stack.pop()
            stackOutput(string,pushed,stack,newstring,output)
            
            newstring=newstringCopy
            stack=stackCopy[:]
            stack.append(string[pushed])
            stackOutput(string,pushed+1,stack,newstringCopy,output)
        else:
            stack.append(string[pushed])
            stackOutput(string,pushed+1,stack,newstring,output)
            
    return output
            
            
def driver():
    allValidSequence = stackOutput(string=input(), pushed=0, stack=[], newstring='', output=[])
    try:
        while True:
            if input() in allValidSequence:
                print('YES')
            else:
                print('NO')
    except EOFError:
        pass

driver()       
