#!/usr/bin/python

# extract all digits from input file and output the sum to stdin

import sys
import re

if (len(sys.argv) != 2):
    print("You must provide the input file to sum the digits from!")
else:
    digits = []
    infile = open(sys.argv[1])

    for line in infile.readlines():
        matchObj = re.findall('[0-9]+', line)
        if matchObj:
            for nums in matchObj:
                digits.append(nums)

    infile.close()
    summ = 0
    for nums in digits:
        summ += int(nums)

    print summ
