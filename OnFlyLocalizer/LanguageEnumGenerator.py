import os


def generate_enum(path, localizations):
    full_path = path + "/" + "Language.swift"
    if not os.path.isfile(full_path):
        enum_file = open(full_path, 'w+')

        enum_file.write("import Foundation\n\n")
        enum_file.write("enum Language: String {\n")
        enum_file.write("\tprivate static let languageKey = \"AppleLanguages\"\n")
        enum_file.write("\tprivate static var currentLanguage: Language?\n\n")

        for localization in localizations:
            enum_file.write("\tcase " + localization + " = " + localization + "\n")
        enum_file.write("\tcase Undefined = \"\"\n\n")

        enum_file.write("\tfunc getCurrentLanguage() -> Language {\n")
        enum_file.write("\t\tif let language = currentLanguage {\n")
        enum_file.write("\t\t\treturn language\n")
        enum_file.write("\t\t}\n\n")
        enum_file.write("\t\tif let array = UserDefaults.standard.stringArray(forKey: languageKey), let label = array.first, let language = Language(rawValue: label) {\n")
        enum_file.write("\t\t\tcurrentLanguage = language\n")
        enum_file.write("\t\t\treturn language\n")
        enum_file.write("\t\t}\n\n")
        enum_file.write("\t\treturn .Undefined\n")
        enum_file.write("\t}\n\n")

        enum_file.write("\tfunc setCurrentLanguage(language: Language) {\n")
        enum_file.write("\t\tcurrentLanguage = language\n")
        enum_file.write("\t\tUserDefaults.standard.set([language.rawValue] forKey: languageKey)\n")
        enum_file.write("\t}\n\n")

        enum_file.write("}")

        enum_file.close()
