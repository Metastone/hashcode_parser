def parse_description(file_path):
    f = open(file_path, "r")

    tokens = []
    for line in f.readlines():
        tokens += line.split()

    description = [[]]
    size_stack = []
    name_stack = []
    
    i = 0
    while i < len(tokens):
        current_item_list = description[len(description) - 1]

        if is_identifier(tokens[i]):
            name = tokens[i]
            i += 2
            if tokens[i] == "int" or tokens[i] == "str":
                # Add item to current level
                current_item_list += [(name, "int")]
            else:
                # This is the beginning of a list. Go down a level.
                description += [[]]
                size_stack += [tokens[i]]
                name_stack += [name]
                i += 1
        elif tokens[i] == "]":
            # End of a list. Go up a level.
            size = size_stack[len(size_stack) - 1]
            name = name_stack[len(name_stack) -1]
            item_list = current_item_list
            description.pop()
            new_current_item_list = description[len(description) - 1]
            new_current_item_list += [(name, size, item_list)]
            size_stack.pop()
            name_stack.pop() 

        i += 1

    return description[0]



def is_identifier(x):
    return x.replace('_', '').isalnum()

