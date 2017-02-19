import os

CONFIGURATION_NAME = 'OnFlyLocalizer.conf'

TURN_TO_CAMEL_KEY = 'TurnToCamelCharacters'
CHANGE_R_SWIFT_STRING_KEY = 'ChangeRSwiftStrings'
LOCALIZATIONS_PATH_KEY = 'LocalizationsPath'
LOCALIZATIONS_TABLE_NAME_KEY = 'LocalizationsTable'
GENERATED_FOLDER_NAME_KEY = 'GeneratedFolderName'
PROCESSED_FILES_NAME_KEY = 'ProcessedFileName'
NEEDS_PROCESSING_FILES_NAME_KEY = 'PendingFilesFileName'
PROCESS_FILES_KEY = 'ProcessFiles'
PARSE_STRINGS_KEY = 'ParseStrings'
EVENT_BUS_NAME_KEY = 'EventBus'

def get_full_path_to_conf(path):
    if path[-1] == '/' or path[-1] == '\\':
        return path + CONFIGURATION_NAME
    else:
        return path + "/" + CONFIGURATION_NAME

def generate_default_configuration(path):
    conf = open(get_full_path_to_conf(path), 'w+')

    conf.write(TURN_TO_CAMEL_KEY + "=.-\n")
    conf.write(CHANGE_R_SWIFT_STRING_KEY + "=false\n")
    conf.write(LOCALIZATIONS_TABLE_NAME_KEY + "=Localizable\n")
    conf.write(GENERATED_FOLDER_NAME_KEY + "=LanguageOnFlyChange\n")
    conf.write(PROCESSED_FILES_NAME_KEY + "=processed.txt\n")
    conf.write(NEEDS_PROCESSING_FILES_NAME_KEY + "=PendingFiles.txt\n")
    conf.write(PROCESS_FILES_KEY + "=false\n")
    conf.write(PARSE_STRINGS_KEY + "=false\n")
    conf.write(EVENT_BUS_NAME_KEY + "=|\o/|+__+|/o\|\n")

    conf.close()

def read_configuration(path):
    file_path = get_full_path_to_conf(path)
    if not os.path.isfile(file_path):
        generate_default_configuration(path)

    configuration = {}

    conf = open(file_path, 'r')

    for line in conf.readlines():
        splitted = line.split('=')
        if len(splitted) == 2:
            configuration[splitted[0]] = splitted[1].strip()

    conf.close()

    return configuration

def synchronize_configuration(path, conf):
    file = open(get_full_path_to_conf(path), 'w+')

    for key in conf:
        file.write(key + "=" + str(conf[key]) + "\n")

    file.close()
