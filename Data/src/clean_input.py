# read file inputtillnow.txt

import os
import sys
import re
import string

file = open("inputtillnow.txt", "r")
lines = file.readlines()
out = open("cleaned_input.txt", "w")
for line in lines:
    # get the last word of the line
    last_word = line.split()[-1]
    # remove punctuation
    last_word = last_word.translate(str.maketrans('', '', string.punctuation))
    # remove whitespace
    last_word = last_word.strip()
    # convert to lowercase
    last_word = last_word.lower()
    # if the last word is "y", "n" of a number then write it to out
    if last_word == "y" or last_word == "n" or last_word.isdigit():
        out.write(last_word + "\n")


file.close()
out.close()
