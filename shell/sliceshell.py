import importlib.util
from slicetext import cdr
slice2=importlib.util.spec_from_file_location("slicetextrun",cdr+"\\runslice\\slicetextrun.py")
slice=importlib.util.module_from_spec(slice2)
slice2.loader.exec_module(slice)
print("Welcome to Slicetext Shell, running Slicetext v0.8")
while True:
    try:
        into=input(">>")
        slice.Lexer(into)
    except:
        continue