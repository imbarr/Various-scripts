import sys
from os.path import dirname, basename, join, isfile, isdir
from os import listdir

BOM = b'\xef\xbb\xbf'


def listdir_full_path(d):
    return [join(d, f) for f in listdir(d)]


def repair_all(file):
    if isdir(file):
        for i in listdir_full_path(file):
            repair_all(i)
    elif isfile(file):
        if basename(file).endswith(".cue"):
            repair(file)
    else:
        print("File not found.")


def repair(file):
    with open(file, 'rb') as f:
        s = f.read()
    if not s.startswith(BOM):
        print(file)
        with open(rep_name(file), 'wb') as out:
            out.write(BOM + s.decode('cp1251').replace('.wav', '.flac').encode('utf8'))


def rep_name(file):
    return join(dirname(file), "[Repaired] " + basename(file))


repair_all(sys.argv[1])
