def format_list(l, level):
    indentation = "    " * level
    list_content = ""
    for x in l:
        list_item = format_dict(x, level+1)
        list_content += f"{indentation}{{\n{list_item}{indentation}}}\n"
    return list_content

def format_item(item, level):
    indentation = '    ' * level
    if type(item[1]) is list:
        return f"(list size {len(item[1])})\n{indentation}[\n{format_list(item[1], level+1)}{indentation}]"
    return str(item[1])

def format_dict(d, level):
    formatted = ""
    for item in d.items():
        indentation = '    ' * level
        name = item[0]
        formatted += f"{indentation}{name} : {format_item(item, level)}\n"
    return formatted

def pretty_print_input_parsed(input_parsed):
    print(format_dict(input_parsed, 0))

