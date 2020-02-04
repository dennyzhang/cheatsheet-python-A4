#!/usr/bin/env python3
##-------------------------------------------------------------------
##  @copyright 2020 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: example_signal.py
## Author : Denny <https://www.dennyzhang.com/contact>
## Description :
## --
## Created : <2020-02-10>
## Updated: Time-stamp: <2020-02-10 14:22:25>
##-------------------------------------------------------------------
# https://docs.python.org/2/library/signal.html
import signal, os
import time
def handler(signum, frame):
    print("Signal handler: ", signum)

def trapSignal():
    signal.signal(signal.SIGINT, handler)
    # a 5-second alarm
    signal.alarm(5)
    time.sleep(100)
    # disable alarm
    signal.alarm(0)

if __name__ == '__main__':
    trapSignal()
