#!/usr/bin/python3

import sys
import re
import os
import subprocess
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
        if sys.argv[1] not in ['-r', '-v'] and len(sys.argv) >= 2:
            
            # reading in binary to avoid missing out on any characters even tho invisible
            fread = open(sys.argv[2], 'rb')        

            # for i in fread.readlines():
            #     print(i, end="")
            
            # evaluate empty expression - part 1
            if sys.argv[1] == "":
                print(fread.read().decode(), end="")

                fread.close()

        
            # check match for a single character - part 2
            # match for word
            else:            
                for i in fread.readlines():
                    i = i.decode()  # convert from bytes to string

                    if re.search(sys.argv[1], i):
                        flag = True
                        print(i, end="")

                fread.close()            

        # part 3
        elif sys.argv[1] == "-r":                        
            term = sys.argv[2]

            if not sys.stdin.isatty():                       
                output = sys.stdin.readlines()                                                
                for line in output:             
                    print(line)
                    if re.search(term, line):
                        print(f"{line}", end="")

            else:
                paths = sys.argv[3:]
                all_files = list()
                
                # recursively run through only files                            
                for k in paths:
                    if os.path.isdir(k):  
                        paths.remove(k)                  
                        root = k
                        for root, _, files in os.walk(root):
                            for file in files:                    
                                current_path = Path(root) / file
                                # print(current_path)
                                all_files.append(current_path.__str__())

                all_files = paths + all_files            
                for file in all_files:
                    with open(file, 'rb') as f:
                        for line in f.readlines():
                            line = line.decode() # convert to string
                            if re.search(term, line):
                                print(f"{file}:{line}", end="")                

        # part 4        
        elif sys.argv[1] == "-v":
            term = sys.argv[2]            
            # Read input from the pipe
            if not sys.stdin.isatty():
                output = sys.stdin.readlines()                                
                for line in output:                    
                    if not re.search(term, line):
                        print(f"{line}", end="")

            else:
                print("heubl")
                all_files = sys.argv[3:]
                for file in all_files:
                    with open(file, 'rb') as f:
                        for line in f.readlines():
                            line = line.decode() # convert to string
                            if not re.search(term, line):
                                print(f"{file}:{line}", end="")
            
            # all_files = sys.argv[3:]

    except BaseException as e:        
        print(e)
        exit(1)

    else:        
        if flag:
            exit(0) # return code 0 for match
        else:
            exit(1)     # return code 1 for no match

if __name__ == "__main__":
    eval_exp()