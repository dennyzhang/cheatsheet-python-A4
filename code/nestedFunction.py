#!/usr/bin/env python3
##-------------------------------------------------------------------
##  @copyright 2020 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: nested-function.py
## Author : Denny <https://www.dennyzhang.com/contact>
## Description :
## --
## Created : <2020-02-03>
## Updated: Time-stamp: <2020-02-03 16:00:38>
##-------------------------------------------------------------------
## https://realpython.com/primer-on-python-decorators/
def parent():
    print("Printing from the parent() function.")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    print(first_child())
    print(second_child())
