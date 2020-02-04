#!/usr/bin/env python3
##-------------------------------------------------------------------
##  @copyright 2018 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: example-file.py
## Author : Denny <https://www.dennyzhang.com/contact>
## Description :
## --
## Created : <2018-07-16>
## Updated: Time-stamp: <2020-02-04 09:59:24>
##-------------------------------------------------------------------
def convert_list(listfile, datafile):
    with open(listfile, 'r') as f:
        for row in f:
            Data = row.split('|')
            print(Data[2].strip())

def write_file():
    f = open('myfile', 'w')
    f.write('hi there\n')  # python will convert \n to os.linesep
    f.close()  # you can omit in most cases as the destructor will call it

    open("/tmp/test.txt", "ab").write("\ntest:")
    open("/tmp/test.txt", "wab").write("\ntest:")

def make_dir():
    newpath = '/tmp/mytest'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
