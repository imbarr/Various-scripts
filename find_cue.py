import sys
from os.path import dirname, basename, join, isfile, isdir
from os import listdir


def listdir_full_path(d):
    return [join(d, f) for f in listdir(d)]
    
def find_cue(file, string):
    if isdir(file):
        for i in listdir_full_path(file):
            find_cue(i, string)
    elif isfile(file):
        if file.endswith(".cue"):
            try:
                with open(file, "r", encoding='utf8') as f:
                    if f.read().lower().find(string) != -1:
                        print(file)
            except:
                pass
    else:
        print("Error: file not found.")

find_cue(sys.argv[1], sys.argv[2].lower())  
