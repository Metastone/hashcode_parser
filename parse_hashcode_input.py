from collections import deque

def is_simple_item(item):
    return len(item) == 2

def is_list(item):
    return len(item) == 3

def parse_item(name, item, tokens, potential_list_sizes):
    if is_simple_item(item):
        value = parse_simple_item(tokens)
        potential_list_sizes[name] = value
        return value
    elif is_list(item):
        (list_size_id, list_description) = (item[1], item[2])
        list_size = int(potential_list_sizes[list_size_id])
        return parse_list(list_size, list_description, tokens, potential_list_sizes)

def parse_simple_item(tokens):
    return tokens.popleft()

def parse_list(list_size, list_description, tokens, potential_list_sizes):
    l = []
    for i in range(list_size):
        element_parsed = {}
        pot_list_sizes_sub_level = dict(potential_list_sizes)
        for item in list_description:
            name = item[0]
            element_parsed[name] = parse_item(name, item, tokens, pot_list_sizes_sub_level)
        l += [element_parsed]
    return l

def parse_hashcode_input(hashcode_file_path, description):
    hashcode_input = open(hashcode_file_path, "r")
    tokens = deque()
    for line in hashcode_input.readlines():
        tokens += line.split()

    input_parsed = {}
    potential_list_sizes = {}
    for item in description:
        name = item[0]
        input_parsed[name] = parse_item(name, item, tokens, potential_list_sizes)
    
    return input_parsed

