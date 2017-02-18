import re

escaped_characters = ".?+*|()\\[]"
splitting_characters = ""


def convert_to_camel(key):
    splitted = re.split(splitting_characters, key)
    if len(splitted) > 1:
        converted = splitted[0]
        for i in range(1, len(splitted)):
            converted += splitted[i].capitalize()
        return converted
    else:
        return key

def parse(paths, camel_case_characters):
    global splitting_characters

    camel_case = str(camel_case_characters)
    splitting_characters = r"["
    for character in camel_case:
        if character in escaped_characters:
            splitting_characters += '\\'
        splitting_characters += character
    splitting_characters += ']'


    used_keys = {}
    for path in paths:
        f = open(path, 'r')
        for line in f.readlines():
            splitted = line.split("=")
            if len(splitted) == 2:
                value = splitted[1].strip()[1:-2]

                arguments = ""
                create_argument = False
                current_index = 0
                for index, character in enumerate(value):
                    if create_argument:
                        create_argument = False
                        arguments += "value" + str(current_index) + ": "

                        if character == '@':
                            arguments += "String"
                        elif character == 'i':
                            arguments += "Int"
                        elif character == 'd' or character == 'f':
                            arguments += "Double"

                        arguments += ', '
                    if character == '%':
                        create_argument = True
                        current_index += 1

                original_key = splitted[0].strip()[1: -1]

                if current_index > 0:
                    arguments = arguments[0:-2]

                used_keys[original_key] = [convert_to_camel(original_key), arguments, current_index]

    return used_keys