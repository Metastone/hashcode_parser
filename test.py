from description_parser import *
from parse_hashcode_input import *

description = parse_description("2015.desc")
hashcode_input = parse_hashcode_input("2015.in", description)
print(hashcode_input)

