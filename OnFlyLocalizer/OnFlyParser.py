import ntpath
import re
from argparse import ArgumentParser

from OnFlyLocalizer.Configuration import *
from OnFlyLocalizer.FileProcessor import process_file
from OnFlyLocalizer.FilesListReader import read_file
from OnFlyLocalizer.LocalizedStringGenerator import generate
from OnFlyLocalizer.LocalizedStringsParser import parse

parser = ArgumentParser()
parser.add_argument("-s", "--source-path", dest="spath", type=str, help="Option to pass path to folder source code")
parser.add_argument("-p", "--prefix", dest="prefix", type=str, help="Prefix for code", default="", nargs='?')

args = parser.parse_args()
if args.spath[-1] == '/' or args.spath == '\\':
    args.spath = args.spath[0: -1]

configuration = read_configuration(args.spath)

should_process_files = bool(configuration[PROCESS_FILES_KEY])

if should_process_files:
    generation_folder = str(configuration[GENERATED_FOLDER_NAME_KEY])
    generation_path = args.spath + '/' + generation_folder

    processed_files_path = generation_path + '/' + str(configuration[PROCESSED_FILES_NAME_KEY])
    processed_files = read_file(processed_files_path)

    pending_files_path = generation_path + '/' + str(configuration[NEEDS_PROCESSING_FILES_NAME_KEY])
    pending_files = read_file(pending_files_path)

    table_name = configuration[LOCALIZATIONS_TABLE_NAME_KEY]
    localization_path = configuration[LOCALIZATIONS_PATH_KEY]
    last_update_timestamp = int(configuration[LAST_UPDATE_TIMESTAMP_KEY])

    configuration_modified = False
    search_for_path = False
    should_parse_strings = False

    generated_file_name = args.prefix + "LocalizedStrings"
    localizable_file_name = table_name + ".strings"

    if localization_path is None:
        localization_path = args.spath
        search_for_path = True
    else:
        if localization_path[0] == '/' or localization_path[0] == '\\':
            localization_path = localization_path[1: -1]

        localization_path = args.spath + localization_path

    paths = []
    localizations = []

    should_change_r_string = bool(configuration[CHANGE_R_SWIFT_STRING_KEY])

    configuration[PROCESS_FILES_KEY] = False
    configuration_modified = True

    for root, subFolder, files in os.walk(localization_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name == localizable_file_name:
                paths.append(file_path)
                localizations.append(ntpath.basename(root).split(".")[0])

                last_modification_timestamp = os.path.getmtime(file_path)
                if last_modification_timestamp > last_update_timestamp:
                    configuration_modified = True
                    should_parse_strings = True
                    configuration[LAST_UPDATE_TIMESTAMP_KEY] = last_modification_timestamp

                if search_for_path:
                    loc_path = os.path.abspath(os.path.join(root, os.pardir))
                    common = os.path.commonprefix([args.spath, loc_path])
                    relative = os.path.relpath(loc_path, common)
                    configuration[LOCALIZATIONS_PATH_KEY] = relative

                    configuration_modified = True

                    search_for_path = False

            if "Controller" in file_name or "View" in file_name or file_name in pending_files:
                process_file(file_path, str(configuration[EVENT_BUS_NAME_KEY]))

            if should_change_r_string:
                if file_name.endswith(".swift") and "R.generated.swift" not in file_name:
                    f = open(file_path, 'r+')
                    text = f.read()
                    text = re.sub(r'R.string.' + table_name.lower(), generated_file_name, text)
                    f.seek(0)
                    f.write(text)
                    f.truncate()
                    f.close()

    if should_parse_strings:
        used_keys = parse(paths, configuration[TURN_TO_CAMEL_KEY])
        generate(generation_path, generated_file_name, used_keys, table_name)

    if configuration_modified:
        synchronize_configuration(args.spath, configuration)