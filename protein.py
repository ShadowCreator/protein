#!/usr/bin/env python3

import argparse
import sys
from itertools import chain, repeat, islice


def dnaToRna(sequenceToChange):
    for index, base in enumerate(sequenceToChange):
        if base == "a":
            sequenceToChange[index] = "u"
        elif base == "t":
            sequenceToChange[index] = "a"
        elif base == "g":
            sequenceToChange[index] = "c"
        elif base == "c":
            sequenceToChange[index] = "g"
        elif base == "-" or base == ",":
            sequenceToChange[index] = base
        else:
            print("Error: Sequence is incorrect, it contains:", base)
            sys.exit(1)
    return sequenceToChange


def rnaToDna(sequenceToChange):
    for index, base in enumerate(sequenceToChange):
        if base == "a":
            sequenceToChange[index] = "t"
        elif base == "u":
            sequenceToChange[index] = "a"
        elif base == "g":
            sequenceToChange[index] = "c"
        elif base == "c":
            sequenceToChange[index] = "g"
        elif base == "-" or base == ",":
            sequenceToChange[index] = base
        else:
            print("Error: Sequence is incorrect, it contains:", base)
            sys.exit(1)
    return sequenceToChange

aaDict = {
    'uuu': 'Phe',
    'uuc': 'Phe',
    'uua': 'Leu',
    'uug': 'Leu',
    'ucu': 'Ser',
    'ucc': 'Ser',
    'uca': 'Ser',
    'ucg': 'Ser',
    'uau': 'Tyr',
    'uac': 'Tyr',
    'uaa': 'STOP',
    'uag': 'STOP',
    'ugu': 'Cys',
    'ugc': 'Cys',
    'uga': 'STOP',
    'ugg': 'Trp',
    'cuu': 'Leu',
    'cuc': 'Leu',
    'cua': 'Leu',
    'cug': 'Leu',
    'ccu': 'Pro',
    'ccc': 'Pro',
    'cca': 'Pro',
    'ccg': 'Pro',
    'cau': 'Hls',
    'cac': 'Hls',
    'caa': 'Gln',
    'cag': 'Gln',
    'cgu': 'Arg',
    'cgc': 'Arg',
    'cga': 'Arg',
    'cgg': 'Arg',
    'auu': 'Ile',
    'auc': 'Ile',
    'aua': 'Ile',
    'aug': 'Met',
    'acu': 'Thr',
    'acc': 'Thr',
    'aca': 'Thr',
    'acg': 'Thr',
    'aau': 'Asn',
    'aac': 'Asn',
    'aaa': 'Lys',
    'aag': 'Lys',
    'agu': 'Ser',
    'agc': 'Ser',
    'aga': 'Arg',
    'agg': 'Arg',
    'guu': 'Val',
    'guc': 'Val',
    'gua': 'Val',
    'gug': 'Val',
    'gcu': 'Ala',
    'gcc': 'Ala',
    'gca': 'Ala',
    'gcg': 'Ala',
    'gau': 'Asp',
    'gac': 'Asp',
    'gaa': 'Glu',
    'gag': 'Glu',
    'ggu': 'Gly',
    'ggc': 'Gly',
    'gga': 'Gly',
    'ggg': 'Gly'
}


def addPunctuationToList(punctuation, oldList):
    return list(islice(chain.from_iterable(
        zip(repeat(punctuation), oldList)), 1, None))


def groupList(numberPerGroup, oldList):
    return list(zip(*(iter(oldList),) * numberPerGroup))


def rnaToAa(sequenceToChange, verbose, nowarnings):
    if verbose:
        print("Here's the sequence befande removing punctuation:",
              sequenceToChange)
    for x in sequenceToChange:
        if x == ",":
            sequenceToChange.remove(",")
        elif x == "-":
            sequenceToChange.remove("-")
    if verbose:
        print("Here's the sequence after removing punctuation:",
              sequenceToChange)
    if not nowarnings and (len(sequenceToChange) % 3):
        print("Warning: Sequence is not a multiple of three")
    sequenceToChange = groupList(3, sequenceToChange)
    for index, base in enumerate(sequenceToChange):
        sequenceToChange[index] = ''.join(base)
        sequenceToChange[index] = aaDict[sequenceToChange[index]]
    sequenceToChange = addPunctuationToList('-', sequenceToChange)
    return sequenceToChange


def checkTypes(outputType, inputType, verbose):
    # see codecomplete 2 for a better way of doing this using arrays
    if verbose:
        print("Here's the input type:", inputType)
        print("Here's the output type:", outputType)
    if outputType != "aa" and outputType != "mrna" and outputType != "dna":
        print("Error: Not DNA, mRNA and AA. Please change your output type")
        sys.exit(1)
    if inputType != "aa" and inputType != "mrna" and inputType != "dna":
        print("Error: Not DNA, mRNA and AA. Please change your input type")
        sys.exit(1)
    if inputType == "aa" and (outputType == "dna" or outputType == "mrna"):
        # verbose
        sys.exit(1)


def processSequence(outputType, inputType, sequence, verbose, nowarnings):
    if inputType == outputType:
        return ''.join(sequence).upper()
    elif inputType == "dna" and outputType == "mrna":
        sequence = dnaToRna(sequence)
        return ''.join(sequence).upper()
    elif inputType == "dna" and outputType == "aa":
        sequence = dnaToRna(sequence)
        sequence = rnaToAa(sequence, verbose, nowarnings)
        return ''.join(sequence)
    elif inputType == "mrna" and outputType == "dna":
        sequence = rnaToDna(sequence)
        return ''.join(sequence).upper()
    elif inputType == "mrna" and outputType == "aa":
        sequence = rnaToAa(sequence, verbose, nowarnings)
        return ''.join(sequence)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_type",
                        help="""this is the format the
                    input should be: DNA, mRNA or AA""")
    parser.add_argument("output_type",
                        help="""this is the format the output should be
                    : DNA, mRNA or AA""")
    parser.add_argument("sequence",
                        help="""this is a sequence of DNA, mRNA or AA with both - and , allowed
                    as separators but - is recomended""")
    parser.add_argument("-n", "--nowarnings", action="store_true",
                        help="turns off warnings")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increases output verbosity")
    args = parser.parse_args()
    output_type = args.output_type.lower()
    input_type = args.input_type.lower()
    sequence = list(args.sequence.lower())
    checkTypes(output_type, input_type, args.verbose)
    print(processSequence(output_type, input_type, sequence, args.verbose,
                          args.nowarnings))

if __name__ == '__main__':
    main()
