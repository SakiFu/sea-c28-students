#!/usr/bin/env python

import sys

filename = sys.argv[1]
new_file = sys.argv[2]

input = raw_input("A: Create a new file or B: Overwrite \
                   the existing one")


def clean(line):
    return line.strip(' ')

#map
#Create a new file
if input == 'A':
    f = open(filename, "r")
    lines = f.readlines()
    new_lines = map(clean, lines)
    f = open(new_file, "w")
    f.writelines(new_lines)

#Overwrite the existing one

if input == 'B':
    f = open(filename, "r")
    lines = f.readlines()
    new_lines = map(clean, lines)
    f = open(filename, "w")
    f.writelines(new_lines)

#List comprehention
#Create a new file
if input == 'A':
    f = open(filename, "r")
    lines = f.readlines()
    new_lines = [clean(x) for x in lines]
    f = open(new_file, "w")
    f.writelines(new_lines)

#Overwrite the existing one

if input == 'B':
    f = open(filename, "r")
    lines = f.readlines()
    new_lines = [clean(x) for x in lines]
    f = open(filename, "w")
    f.writelines(new_lines)
