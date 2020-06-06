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
        output = str(output).strip('b\'')
        output = str(output).strip('\'')
        list_cleanup(output, list)


def list_create(input, list):
    stripped_line = input. strip()
    line_list = str(stripped_line). split("\\n")
    list. append(line_list)



def debug():

    ws = []
    wind = []

    wind_list(ws)
    for i in ws:
        print(i)
    print(ws[1][1])

    for i in range(11):
        del ws[i][-1]

    for i in ws:
        print(i)
#debug()
