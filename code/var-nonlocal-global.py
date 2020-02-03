#!/usr/bin/env python3
##-------------------------------------------------------------------
##  @copyright 2020 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: var-nonlocal-global.py
## Author : Denny <https://www.dennyzhang.com/contact>
## Description :
## --
## Created : <2020-02-03>
## Updated: Time-stamp: <2020-02-03 15:32:04>
##-------------------------------------------------------------------
x = 1
class Solution:
    def myfun(self):
        y = 2
        def myfun():
            global x
            print("hello", x)
            nonlocal y
            x += 1
            y += 1
            print(x, y)
        myfun()
        global x
        x += 2
        y += 2
        print(x, y)

if __name__ == '__main__':
    s = Solution()
    s.myfun()
