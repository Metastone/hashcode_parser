def parse_description(file_path):
    f = open(file_path, "r")

    tokens = []
    for line in f.readlines():
        tokens += line.split()

    description = []
    i = 0
    while i < len(tokens):
        if is_identifier(tokens[i]):
            name = tokens[i]
            print(name)
            i += 2
            if tokens[i] == "int":
                description += [(name, "int")]
            else:
                size = tokens[i]
                items = []
                while tokens[i] != "]":
                    i += 1
                description += [(name, size, items)]
        i += 1

    print(description)



def is_identifier(x):
    return x.replace('_', '').isalnum()
