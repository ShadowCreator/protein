#!/usr/bin/env python3

#######TODO
#Refactor?

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("output type", help="this is the format the output should be: DNA, mRNA or AA")
parser.add_argument("input type", help="this is the format the input should be: DNA, mRNA or AA")
parser.add_argument("sequence",
                    help="this is a sequence of DNA, mRNA or AA and it's type can be infered")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")

args = parser.parse_args()
output = args.output_type.lower()
input_type = args.input_type.lower()
sequence = list(args.sequence.lower())

### Ensure correct output and input types are being used
if args.verbose:
    print("Here's the output type:", output_type)
    print("Here's the input type:", output_type)
if output_type != "aa" or output_type != "mrna" or output_type != "dna":
    #verbose only: print("Not DNA, mRNA or AA. Please change your output type")
    sys.exit(1)
if input_type != "aa" or input_type != "mrna" or input_type != "dna":
    #verbose only: print("Not DNA, mRNA or AA. Please change your input type")
    sys.exit(1)

### Remove punctuation
if args.verbose:
    print("Here's the sequence before removing punctuation:", sequence)
for x in sequence:
    if x == ",":
        sequence.remove(",")
    elif x == "-":
        sequence.remove("-")
if args.verbose:
    print("Here's the sequence after removing punctuation:", sequence)
