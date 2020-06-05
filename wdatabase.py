#!/bin/python3

import os
import subprocess



def wind_list(list):
    command = "wmctrl -l | awk '{if ($2==\"0\") print $1}' |tr \\n \" \""
    line = command

    for i in range(11):
        line = str(line).replace('0', str(i))
        output = subprocess.check_output(line, shell=True)
        line = command
        #print(output)   # checking what comes back from bash
        list_cleanup(output, list)


def list_cleanup(input, list):
    stripped_line = input. strip()
    line_list = str(stripped_line). split("\\n")
    #line_list = str(line_list).strip('b')
    #line_list = str(line_list).replace(r'\n', '')
    #line_list = str(line_list).replace('\'', '')
    #print (line_list) # checking what gets added to list
    list. append(line_list)



def debug():

    ws = []

    wind_list(ws)
    for i in ws:
         print(i)
    print(ws[0][1])


#debug()
