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
            
        # evaluate empty expression - part 1
        if sys.argv[1] == "":
            print(fread.read().decode(), end="")

        
        # check match for a single character - part 2
        elif len(sys.argv[1]) == 1:
            flag = False
            for i in fread.readlines():
                i = i.decode()  # convert from bytes to string

                if re.search(sys.argv[1], i):
                    flag = True
                    print(i, end="")
            
            if flag:
                exit(0) # return code 0 for match
                
            else:
                exit(1)     # return code 1 for no match

    except Exception as e:        
        print(e)
        print("file or directory not found")

    else:
         fread.close()   

if __name__ == "__main__":
    eval_exp()