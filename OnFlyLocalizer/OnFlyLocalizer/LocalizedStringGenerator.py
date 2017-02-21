def generate(path, name, keys, table_name):
    generated_file = open(path + "/" + name + ".swift", 'w+')
    generated_file.write("import Foundation\n\n")

    generated_file.write("class " + name + " {\n")

    generated_file.write("\tstatic var currentBundle: Bundle?\n")
    generated_file.write("\tstatic var currentLanguageCode: String?\n\n")

    generated_file.write("\tstatic func getBundle() -> Bundle {\n")
    generated_file.write("\t\tlet code = Language.getCurrentLanguage().rawValue\n\n")
    generated_file.write("\t\tif let bundle = currentBundle, let currentLanguageCode = currentLanguageCode, currentLanguageCode == code {\n")
    generated_file.write("\t\t\treturn bundle\n")
    generated_file.write("\t\t}\n\n")
    generated_file.write("\t\tif let path = Bundle.main.path(forResource: code, ofType: \".lproj\"), let bundle = Bundle(path: path) {\n")
    generated_file.write("\t\t\tcurrentBundle = bundle\n")
    generated_file.write("\t\t\tcurrentLanguageCode = code\n")
    generated_file.write("\t\t\treturn bundle\n")
    generated_file.write("\t\t}\n\n")
    generated_file.write("\t\treturn Bundle.main\n")
    generated_file.write("\t}\n\n")

    for key in keys:
        value = keys[key]
        generated_file.write("\tstatic func " + value[0] + "(" + value[1] + ") -> String {\n")
        string = "getBundle().localizedString(forKey: \"" + key + "\", value: \"" + key + "\", table: \"" + table_name + "\")"
        if value[2] > 0:
            string = "String(format: " + string + ", "
            for i in range(value[2]):
                string += "value" + str(i + 1) + ", "
            string = string[0: -2] + ")"

        generated_file.write("\t\treturn " + string + "\n")
        generated_file.write("\t}\n\n")

    generated_file.write("}")
    generated_file.close()