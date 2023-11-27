#!/usr/bin/python3

import sys
import re

def eval_exp():
    """
    Eval grep expression
    """

    # return on no arguments to grep
    if 0 == len(sys.argv):
        return

    # try except for path not found      
    try:
        if len(sys.argv) >= 2:
            
            # reading in binary to avoid missing out on any characters even tho invisible
            fread = open(sys.argv[2], 'rb')        

            # for i in fread.readlines():
            #     print(i, end="")
            
        # evaluate empty expression
        if sys.argv[1] == "":
            print(fread.read().decode(), end="")

    except Exception as e:        
        print(e)
        print("file or directory not found")

    else:
         fread.close()   

if __name__ == "__main__":
    eval_exp()