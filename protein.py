#!/usr/bin/env python3

import argparse
import sys

def dnaToRna(sequencetochange):
    for index, base in enumerate(sequencetochange):
        if base == "a":
            sequencetochange[index] = "u"
        elif base == "t":
            sequencetochange[index] = "a"
        elif base == "g":
            sequencetochange[index] = "c"
        elif base == "c":
            sequencetochange[index] = "g"
        elif base == "-" or base == ",":
            sequencetochange[index] = base
        else:
            # verbose message
            sys.exit(1)
    return sequencetochange

def rnaToDna(sequencetochange):
    for index, base in enumerate(sequencetochange):
        if base == "a":
            sequencetochange[index] = "t"
        elif base == "u":
            sequencetochange[index] = "a"
        elif base == "g":
            sequencetochange[index] = "c"
        elif base == "c":
            sequencetochange[index] = "g"
        elif base == "-" or base == ",":
            sequencetochange[index] = base
        else:
            # verbose message
            sys.exit(1)
    return sequencetochange

def rnaToAa(sequencetochange):
    # remove punctuation
    if args.verbose:
        print("Here's the sequence befande removing punctuation:", sequence)
    for x in sequence:
        if x == ",":
            sequence.remove(",")
        elif x == "-":
            sequence.remove("-")
    if args.verbose:
        print("Here's the sequence after removing punctuation:", sequence)
    
    # add punctuation after each aa
return sequencetochange

parser = argparse.ArgumentParser()
parser.add_argument("input_type", help="this is the format the input should be: DNA, mRNA or AA")
parser.add_argument("output_type", help="this is the format the output should be: DNA, mRNA or AA")
parser.add_argument("sequence",
                    help="this is a sequence of DNA, mRNA or AA whith both - and , allowed as separators but - is recomended")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")

args = parser.parse_args()
output_type = args.output_type.lower()
input_type = args.input_type.lower()
sequence = list(args.sequence.lower())

# ensure correct output and input types are being used
# see codecomplete 2 for a better way of doing this using arrays
if args.verbose:
    print("Here's the output type:", output_type)
    print("Here's the input type:", input_type)
if output_type != "aa" and output_type != "mrna" and output_type != "dna":
    #verbose only: print("Not DNA, mRNA and AA. Please change your output type")
    sys.exit(1)
if input_type != "aa" and input_type != "mrna" and input_type != "dna":
    #verbose only: print("Not DNA, mRNA and AA. Please change your input type")
    sys.exit(1)
if (input_type == "dna" or input_type == "mrna") and output_type == "aa":
    #verbose
    sys.exit(1)

# do the transformation
if output_type == input_type:
    sequence = sequence
elif input_type == "dna" and output_type == "mrna":
    sequence = dnaToRna(sequence)
elif input_type == "dna" and output_type == "aa":
    sequence = dnaToRna(sequence)
    sequence = rnaToAa(sequence)
elif input_type == "mrna" and output_type == "dna":
    sequence = rnaToDna(sequence)
elif input_type == "mrna" and output_type == "aa":
    sequence = rnaToAa(sequence)

sequence = ''.join(sequence).upper()
print(sequence)
