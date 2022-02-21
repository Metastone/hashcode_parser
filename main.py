#!/bin/python3

import argparse

from parse_description import *
from parse_hashcode_input import *
from pretty_printer import *

def main():
    parser = argparse.ArgumentParser(description="Hashcode parser")
    parser.add_argument("description", help="file containing the description of the hashcode input format")
    parser.add_argument("input", help="hashcode input file")
    args = parser.parse_args()

    description = parse_description(args.description)
    input_parsed = parse_hashcode_input(args.input, description)
    pretty_print_input_parsed(input_parsed)

if __name__ == "__main__":
    main()

