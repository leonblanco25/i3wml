#!/bin/python3

import os
import subprocess


def wind_list(list):
    command = "wmctrl -l | awk '{if ($2==\"0\") print $1}' |tr \\n \" \""
    line = command  

    #print(command)
    for i in range(11):
        #print(i)
        line = str(line).replace('0', str(i))
        #print(line)
        output = subprocess.check_output(line, shell=True)
        #print("wind " +str(i) + " :" + str(output))
        line = command
        list_cleanup(output, list)
        
    
def list_cleanup(input,list):
        stripped_line = input. strip()
        line_list = stripped_line. split()
        line_list = str(line_list).replace('b', '')
        line_list = str(line_list).replace(r'\n', '')
        line_list = str(line_list).replace(r"'", '')
        window. append(line_list)



rows, cols = (9,9)
#window = [[0 for i in range(cols)] for j in range(rows)]
window = []

#wind_list()

#for row in window:
#    print(row)
