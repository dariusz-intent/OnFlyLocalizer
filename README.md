# OnFlyLocalizer
Developers who have meet task of on the fly change of application language in mobile environment probably know,
that usually it's not that trivial task to do, especially if such requirement appeared out of nowhere in the middle 
of the project development process.
This library main purpose is to simplify process of language change by providing code generation scripts, parsing scripts and 
also some Swift classes to put everything together.

# Installation
Library is avliable in CocoaPods, just add following lines to your pod:
```
  pod 'OnFlyLocalizer'
```
and then run:
```
  pod update
```
When everything is downloaded, navigate to Pods/OnFlyLocalizer/OnFlyLocalizer in Terminal and run:
```
  sudo chmod +x localizer.sh
```
Unfortunately it's necessary step, if you don't do this - xCode will not execute this script.
After this add "Run Script" phase to your xCode project and add following line in it:
```
  "$PODS_ROOT/OnFlyLocalizer/OnFlyLocalizer/localizer.sh" "YOUR TARGET NAME HERE"
```
Build project and if everythin went right - you should get **OnFlyLocalizer.conf** file in your target top-level catalog.

# Configuration
As was mentioned in previous section - first build will give you only configuration file.
This file is used to configure work of script. It looks basically in a following way:
```
TurnToCamelCharacters=.-
ChangeRSwiftStrings=false
PendingFilesFileName=PendingFiles.txt
LocalizationsTable=Localizable
GeneratedFolderName=LanguageOnFlyChange
ProcessedFileName=processed.txt
ProcessFiles=False
ParseStrings=true
EventBus=|\o/|+__+|/o\|
LocalizationsPath=Others
```
As you can see it's simple key-value file, in which you can configure how script will behave and work.
Let me go over all keys and explain exactly what they're doing.

## TurnToCamelCharacters
You can provide here all characters that will turn case of next letter after it to upper. It's used for translation of 
key of the string in Localization file to name of function.
The default scheme is ".-", i.e. if you have something like 
```
  "klappa.kappacino-inc.O_O" = "O_O";
```
in your Localization strings - it will be turned into following function in generated file:
```
  func klappaKappacinoIncO_O() -> String
```
You can pass arbitrary characters to this field.

## ChangeRSwiftStrings
Basically, if you're using awesome library called R.swift you're probably using R.string for your strings.
The one downside with this approach is that R.string doesn't work very well with localization on-the-fly, 
so you might want to change it. If this field is set to "true" script will repalce all occurences of R.string 
in the project to the generated file. Note, that in this case better to don't change default TurnToCamelCharacters, 
because it will result in errors in changing of strings.

## PendingFilesFileName
Name of file that have list of files that you would like to process (i.e. add localizations).
By default, library goes for processing of files that have "View" or "Controller" in its names.
If you tend to call file with your ViewController like "AwesomiumKlappaInternationalScreen" - 
library will not recognize this as something that might need localization and will just skip it.
If you have such file - add it's name **(not path, just name with extension)** to PendingFiles in a new line and run build.

## LocalizationsTable
Name of file that you keep your strings in. I usually go for "Localizable.strings", but you might want another name. 
If you do - put it in this parameter.

## GeneratedFolderName
Folder in which script will throw all generated files.

## ProcessedFileName
Files that already were processed and doesn't require processing or you don't want to be processed.
If you want to exlclude some files from processing - add its name to file specified in this field.

## ProcessFiles
Field specifies if script will iterate over all files in project and process them.
Note that it's quite big operation and script by default will set this flag to "false".
Make sure that everything is configured as you wanted to, change this field to "true" and run build.
When script will finish - it will set this property to "false" once again to avoid parsing on next build.

## ParseStrings
This field specifies if you want to parse strings and regenerate file with functions.
If set to "true" - it will regenerate file. 

## EventBus
This field specifies from where script have to take EventBus instance to register for Language change event.
The default value have no changes to compile - so provide this correct value for EventBus instance.
Note that it should be one instance.
You may use some kind of DI or singleton for this, just make sure that EventBus will be accessible for file.

## LocalizationsPath
Optional field. You may specify here **relative** path to folder with localized strings. 
If you will not specify it - script will find it by itself and write it here to speed up work.

# Contribution
If you have any issues with the library - make sure to create an issue on repo. Feeback is much appreciated.

