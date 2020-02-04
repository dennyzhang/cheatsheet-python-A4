#!/usr/bin/env python3
##-------------------------------------------------------------------
##  @copyright 2020 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/
##
## File: funcAsParameter.py
## Author : Denny <https://www.dennyzhang.com/contact>
## Description :
## --
## Created : <2020-02-10>
## Updated: Time-stamp: <2020-02-23 12:34:00>
##-------------------------------------------------------------------
def isOne(num):
    return num == 1

def callFun(func, n):
    v = func(n)
    print(v)

# pass function as a parameter
callFun(isOne, 1)
callFun(isOne, 2)

# Lambda wrapper function
isTwo = lambda x: x == 2

callFun(isTwo, 1)
callFun(isTwo, 2)
