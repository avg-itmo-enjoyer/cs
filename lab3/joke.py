#/usr/bin/python3
import sys
import re
import os

def joke(group, text):
    reg = re.compile(fr"((\w)\w+\-?\w+\s+\2\.\s*\2\.\s+{group})", re.IGNORECASE)
    return reg.sub("", text)
    

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Data file required")
        exit(1)
    elif len(sys.argv) > 2:
        print("Only one data file supported")
        exit(1)

    data_file = sys.argv[1]
    if not os.path.exists(data_file) or not os.path.isfile(data_file):
        print("File with given name doesn't exist")
        exit(2)
    
    group = input("Input group: ")
    text = ""
    with open(data_file, "r") as f:
        for line in f:
            text += line
    i = 0
    print(joke(group, text).strip())
