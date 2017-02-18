import os
import re


def process_file(path, bus_name):
    original = open(path, 'r')
    new_file = open(path + "_", 'w+')

    triggered = False
    names = []
    pattern = re.compile(r'.*class(.*)\:.*')
    whitespaces = re.compile(r'(\s*).*')

    tabulation = ""
    for line in original.readlines():
        if len(tabulation) == 0 and triggered:
            tabulation = whitespaces.search(line).group(1)

        if "}" in line and triggered:
            new_file.write(tabulation + bus_name + ".register(subscriber: self, forEvent: 0)\n")
            triggered = False
            tabulation = ""

        if pattern.match(line):
            names.append(pattern.search(line).group(1))

        new_file.write(line + "\n")

        if "func awakeFromNib()" in line or "func viewDidLoad" in line:
            triggered = True

    new_file.write("\n")
    for name in names:
        new_file.write("extension " + name + ": Subscriber {\n")
        new_file.write("\tfunc eventFired(eventCode: Int, associatedObject: Any?) {\n")
        new_file.write("\t\tif eventCode == 0 {\n")
        new_file.write("\t\t\tlocalize()\n")
        new_file.write("\t\t}\n")
        new_file.write("\t}\n")
        new_file.write("}\n")

    new_file.close()
    original.close()

    os.remove(path)
    os.rename(path + "_", path)
    os.remove(path + "_")