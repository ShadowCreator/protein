#!/usr/bin/env python3

#######TODO
#Respect verbose with error messages and Remove debug in favour of it
#Refactor?

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("output", help="this is the format the output should be: DNA, mRNA or AA")
parser.add_argument("sequence",
                    help="this is a sequence of DNA, mRNA or AA and it's type can be infered")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
parser.add_argument("-d", "--debug", action="store_true",
                    help="show debugging messages")

args = parser.parse_args()
output = args.output.lower()
sequence = list(args.sequence.lower())

### Ensure correct output is being used
if args.debug:
    print("Here's the output type:", output)
if output != "aa" and output != "mrna" and output != "dna":
    #verbose only: print("Not DNA, mRNA or AA. Please change your output")
    sys.exit(1)

### Remove punctuation
if args.debug:
    print("Here's the sequence before removing punctuation:", sequence)
for x in sequence:
    if x == ",":
        sequence.remove(",")
    elif x == "-":
        sequence.remove("-")
if args.debug:
    print("Here's the sequence after removing punctuation:", sequence)

### Find what the input sequence type is
# How fast is having a "not" in there?
# Create isType functions to make the testing of input sequences more rigerious and correct
    if "m" in sequence:
        input = "aa"
    elif "u" in sequence and "t" not in sequence:
        input = "mrna"
    elif "t" in sequence and "u" not in sequence:
        input = "dna"
    else:
        sys.exit(1)
if args.debug:
    print("Input:", input)
