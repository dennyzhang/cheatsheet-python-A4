#!/usr/bin/env python3
##-------------------------------------------------------------------
##  @copyright 2020 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: exampleCycleReference.py
## Author : Denny <https://www.dennyzhang.com/contact>
## Description :
## --
## Created : <2020-02-10>
## Updated: Time-stamp: <2020-02-10 14:36:33>
##-------------------------------------------------------------------
import gc

class ClassA():
    def __init__(self):
        print("object id: ", hex(id(self)))
        
def test():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2

if __name__ == '__main__':
    gc.disable()
    test()
