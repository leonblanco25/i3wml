#!/bin/python3

import os
import subprocess

def active_window():
    # retrieves the current active window and returns the value

    xprop = r"xprop -root | grep _NET_ACTIVE_WINDOW | head -1 |awk '{print $5}' | sed 's/,//' | sed 's/^0x/0x0/'"
    output = subprocess.check_output(xprop, shell=True)
    return output
    

def cleanup(input):
    input = str(input).replace('b', '')
    input = str(input).replace(r'\n', '')
    input = str(input).replace(r"'", '')
    return input

#active = active_window()
#wid = cleanup(str(active))

#print("atcive: " + str(wid))
