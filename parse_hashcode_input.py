def is_simple_item(item):
    return len(item) == 2

def is_list(item):
    return len(item) == 3

def parse_item(item, tokens, potential_list_sizes):
    if is_simple_item(item):
        return parse_simple_item(tokens)
    elif is_list(item):
        (list_size_id, list_description) = (item[1], item[2])
        list_size = int(potential_list_sizes[list_size_id])
        return parse_list(list_size, list_description, tokens)

def parse_simple_item(tokens):
    return tokens.pop(0)

def parse_list(list_size, list_description, tokens):
    l = []
    for i in range(list_size):
        element_parsed = {}
        for item in list_description:
            name = item[0]
            element_parsed[name] = parse_item(item, tokens, element_parsed)
        l += [element_parsed]
    return l

def parse_hashcode_input(hashcode_file_path, description):
    hashcode_input = open(hashcode_file_path, "r")
    tokens = []
    for line in hashcode_input.readlines():
        tokens += line.split()

    input_parsed = {}
    for item in description:
        name = item[0]
        input_parsed[name] = parse_item(item, tokens, input_parsed)
    
    return input_parsed

