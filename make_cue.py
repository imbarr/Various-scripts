from mutagen.flac import FLAC
import sys
from os.path import dirname, basename, join, isfile, isdir
from os import listdir


def listdir_full_path(d):
    return [join(d, f) for f in listdir(d)]


def get(flac, key):
    return flac[key][0].replace("\"", "'")


def get_or_else(flac, key, alternative='Unknown'):
    return get(flac, key) if key in flac else alternative


def is_defined(flacs, item):
    return item in flacs[0] and all((item in t and t[item] == flacs[0][item]) for t in flacs)


def make_cue(files):
    if files:
        print(dirname(files[0]))
        flacs = [FLAC(f) for f in files]
        with open(join(dirname(files[0]), "[Generated] List.cue"), 'w+', encoding='utf8') as f:
            if is_defined(flacs, 'genre'):
                f.write("REM GENRE \"" + get(flacs[0], 'genre') + "\"\n")
            if is_defined(flacs, 'date'):
                f.write("REM DATE \"" + get(flacs[0], 'date') + "\"\n")
            f.write("REM COMMENT \"Auto-generated\"\n")
            if is_defined(flacs, 'albumartist'):
                f.write("PERFORMER \"" + get(flacs[0], 'albumartist') + "\"\n")
            if is_defined(flacs, 'album'):
                f.write("TITLE \"" + get(flacs[0], 'album') + "\"\n")
            for i, (file, flac) in enumerate(zip(files, flacs), 1):
                f.write("FILE \"" + basename(file) + "\" WAVE\n")
                f.write("  TRACK " + ("0" + str(i) if i < 10 else str(i)) + " AUDIO\n")
                f.write("    TITLE \"" + get_or_else(flac, 'title') + "\"\n")
                f.write("    PERFORMER \"" + get_or_else(flac, 'artist') + "\"\n")
                f.write("    INDEX 01 00:00:00\n")


def make_cue_all(file):
    if isdir(file):
        make_cue([t for t in listdir_full_path(file) if t.endswith(".flac")])
        for i in listdir_full_path(file):
            if isdir(i):
                make_cue_all(i)
    else:
        print("Directory not found.")


make_cue_all(sys.argv[1])
