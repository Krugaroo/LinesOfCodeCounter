from os import listdir
from os.path import isfile, isdir, abspath, join, splitext

import sys

rootDir = ""
rootDirSet = 0
FileTypes = ""
fileTypesSet = 0
totalLineCount = 0

def LoadArgs():
    global rootDir, FileTypes,rootDirSet,fileTypesSet

    print("Usage (to invoke without user input)")
    print("python LinesOfCodeCounter.py [root_dir] [file_types_to_count]")
    print("Example count lines of code in .c, .py and .h files with current directory as root")
    print("python LinesOfCodeCounter.py . .c,.py,.h")
    
    numArgs = len(sys.argv)

    print(repr(numArgs))
    args = sys.argv

    if numArgs >= 2:
        rootDir = args[1]
        rootDirSet = 1
        
    if numArgs >= 3:
        FileTypes = args[2]
        fileTypesSet = 1

def GetInput():
    global rootDir, FileTypes,rootDirSet,fileTypesSet
    
    print("Lines of Code (LOC) counter")

    if rootDirSet == 0:
        print("Enter root directory of the project (. for current):")
        rootDir = input('Root directory: ')

    if fileTypesSet == 0:
        print("Enter filetypes to include separated by commas (i.e. .c,.h etc or * for all):")
        FileTypes = input('Enter filetypes to include: ')

def MatchesFileType(inFileName):
    fileExt = splitext(inFileName)[1]
   
    for ext in FileTypes.split(","):
       if(ext == fileExt):
            return 1
    return 0

def LinesOfCodeInDir(inDirectory,level):
    directoryTotal = 0
    levelIndent = ""

    for x in range(0,level):
        levelIndent += " "

    #get list of all file and directories
    files = listdir(inDirectory)
    
    for filename in files:
        fullPath = join(abspath(inDirectory),filename)
        
        if (isfile(fullPath)) and (FileTypes=="*" or MatchesFileType(fullPath)):
            
            fileLineCount = 0

            try:
                fileLineCount = sum(1 for line in open(fullPath))
            except UnicodeDecodeError:
                print((levelIndent) + "FILE COULD NOT BE DECODED SKIPPED!")
                pass
            
            print((levelIndent) + (filename) + " line count: " + repr(fileLineCount))

            directoryTotal += fileLineCount
        elif (isdir(fullPath)):
            print((levelIndent) + "dir>" + (filename))
            
            #recurse into the directory
            directoryTotal += LinesOfCodeInDir(fullPath,level+1)
        
    return directoryTotal

LoadArgs()
GetInput()

print("Root directory path:")
print(repr(abspath(rootDir)))

print("dir>" + (rootDir))

totalLineCount = LinesOfCodeInDir(rootDir,0)

print("Total Lines of Code: " + repr(totalLineCount))
print("Kilo Lines of Code (KLOC): " + repr(totalLineCount/1000))
print("Million Lines of Code (MLOC): " + repr(totalLineCount/1000000))
