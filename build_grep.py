#!/usr/bin/python3

import sys
import re
import os
from pathlib import Path

def eval_exp():
    """
    Eval grep expression
    """

    # return on no arguments to grep
    if 0 == len(sys.argv):
        return


    # for returning exit code
    flag = False

    # try except for path not found      
    try:
        if sys.argv[1] != '-r' and len(sys.argv) >= 2:
            
            # reading in binary to avoid missing out on any characters even tho invisible
            fread = open(sys.argv[2], 'rb')        

            # for i in fread.readlines():
            #     print(i, end="")
            
        # evaluate empty expression - part 1
        if sys.argv[1] == "":
            print(fread.read().decode(), end="")

            fread.close()

        
        # check match for a single character - part 2
        elif len(sys.argv[1]) == 1:            
            for i in fread.readlines():
                i = i.decode()  # convert from bytes to string

                if re.search(sys.argv[1], i):
                    flag = True
                    print(i, end="")

            fread.close()            

        # part 3
        elif sys.argv[1] == "-r":            
            term = sys.argv[2]

            # recursively run through only files
            for root, _, files in os.walk("."):
                for file in files:
                    current_path = Path(root) / file

                    with open(current_path, 'rb') as f:
                        for line in f.readlines():
                            line = line.decode() # convert to string
                            if re.search(term, line):
                                print(f"{current_path}:{line}", end="")                            

    except Exception as e:        
        print(e)
        print("file or directory not found")
        exit(1)

    else:        

        if flag:
            exit(0) # return code 0 for match

        else:
            exit(1)     # return code 1 for no match

if __name__ == "__main__":
    eval_exp()