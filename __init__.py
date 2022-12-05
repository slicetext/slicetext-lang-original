import importlib.util
import os.path
cdr=""
def finds(fn,path="C:\\Users\\"):
    """
    Finds a file called the value of fn.
        Do a more specific search with the path parameter.
    """
    filename = fn
    dir_to_search = path

    for root, dirs, files in os.walk(dir_to_search):
        # print(root, dirs, files)
        for name in files:
            if(name == filename):
                return os.path.abspath(os.path.join(root, name))
cdr=finds("sliceshell.py")
cdr=cdr[:-20]
slice7=importlib.util.spec_from_file_location("slicetextrun",cdr+"\\runslice\\slicetextrun.py")
slice8=importlib.util.module_from_spec(slice7)
slice7.loader.exec_module(slice8)
slice3=importlib.util.spec_from_file_location("sliceshell",cdr+"\\shell\\sliceshell.py")
slice4=importlib.util.module_from_spec(slice3)

def shell():
    """
    Launch a Slicetext shell.
    """
    slice3.loader.exec_module(slice4)
def run(file,path="C:\\Users\\"):
    """
    Run a Slicetext file.
    """
    fftxt=finds(file,path)
    exten=file[file.find("."):]
    if(exten!=".slice"):
        print(f">FileTypeError: {exten} is an invalid slice file extention.")
        return
    if(fftxt!=None):
        f=open(fftxt)
        fs=f.read()
        print(fs)
        fsl=fs.split("\n")
        for i in fsl:
            slice8.Lexer(i)
        f.close()
    else:
        print(f">FileNotFoundError: {file} was not found.")
def logo():
    art="""
     _|_
     _|
    / |
    \_|
      |\ 
     _|/
      |
      |
      |
    """
    print(art)
    os.startfile(f"{cdr}slicelogo.jpeg")