#Problems in slicetext in order of importance:1.printing in files 4.whi loop 5.functions 6.modules-running
import os.path
import slicetext as slice
import platform
import warnings
char=[]
func=[]
inif=False
ifs=False
ist=None
wp=[]
platform=platform.system()
var={"char":char,"konami":"up up down down left right left right B A start","inif":inif,"func":func,"platform":platform,"null":None,"true":True,"false":False}
def Lexer(txt):
    """
    Lex a string of text with the Slicetext lexer. The result automaticaly goes to the parser.
    """
    global char
    wasnumeric=False
    num=[]
    ns=""
    we=False
    for i in range(len(txt)):
        pos=txt[i]
        symbols={
            "var":"VARIABLE_INIT",
            "print:":"PRINT_VAR",
            "if":"IF",
            "whi":"WHILE"
        }
        if(pos=="/"and txt[i+1]=="/"):
            char.append("//")
        if(pos=="|"and txt[i+1]=="|"):
            char.append("||")
        # if(pos.isnumeric() or pos=="."or pos=="+" or pos=="-" or pos=="/" or pos=="*" or pos=="(" or pos==")"):
        #     if(wasnumeric==False):
        #         wasnumeric=True
        #     num.append(pos)
        #     if(len(txt)-1==i):
        #         char.append(ns.join(num))
        if((pos=="m"and txt[i+1]=="o"and txt[i+2]=="d")or(pos=="r"and txt[i+1]=="e"and txt[i+2]=="q"and txt[i+3]=="u"and txt[i+4]=="i"and txt[i+5]=="r"and txt[i+6]=="e")):
            if(pos=="m"):
                c=(txt[txt.find("mod")+4:txt.find(";")])
            else:
                c=(txt[txt.find("require")+8:txt.find(";")])
            if('''os.path.exists(slice.cdr+"\\Mods\\"+c)''' != True):
                with open(slice.cdr+"\\Mods\\"+c) as f:
                    fr=f.read()
                index=txt.find(";")+1
                txt=txt[:index]+"\n"+fr+"\n"+txt[index+1:]
                txt=txt.replace(txt[i:txt.find(";")+1],"")
                Lexer(txt)
        elif(pos=="="and(txt[i-1]=="="or txt[i+1]=="=")and we==False):
            we=True
            char.append(symbols["=="])
        elif((pos=="v")and (txt[i+1]=="a") and (txt[i+2]=="r")):
            vn=txt[txt.find("var")+4:txt.find("=")]
            char.append(symbols["var"])
            char.append(vn)
            char.append(txt[txt.find("=")+1:txt.find(";")])
        if((pos=="p")and(txt[i+1]=="r")and(txt[i+2]=="i")and(txt[i+3]=="n")and(txt[i+4]=="t")and(txt[i+5=="l"])and(txt[i+6]==":")):
            try:
                char.append(symbols["print:"])
                char.append(txt[txt.find("printl:")+7:txt.find(";")])
            except(KeyError,ValueError,TypeError,RuntimeError,SyntaxError,IndexError):
                print('>SyntaxError: ";" not found')
        elif(pos=='"'):
            start=txt.index('"')
            end=txt.index('"',start+1)
            char.append(txt[start:end+1])
        elif((pos=="i"and txt[i+1]=="f")or(pos=="w" and txt[i+1]=="h" and txt[i+2]=="i")):
            if(pos=="i"):
                char.append(symbols["if"])
                char.append(str(txt[i+3:txt.find("{")]))#attention
            elif(pos=="w"):
                char.append("WHILE")
                char.append(str(txt[i+6:txt.find("{")]))#attention
            char.append(str(txt[i+3:txt.find("{")]))#attention
        elif(pos=="}"):
            char.append("}")
        if(pos=="h"and txt[i+1]=="e"and txt[i+2]=="l"and txt[i+3]=="p"and txt[i+4]==";"):
            char.append("HELP")
        if(pos=="f"and txt[i+1]=="u"and txt[i+2]=="n"and txt[i+3]=="c"):
            char.append("FUNCTION_DEF")
            char.append(txt[txt[i+6]:txt.find("(")])
            char.append(txt[txt.find("(")+1:txt.find(")")])
        if(pos=="@"):
            char.append("RUN")
            char.append(txt[txt.find("@")+1:txt.find("(")])
            char.append(txt[txt.find("(")+1:txt.find(")")])
        if(i==len(txt)-1 or txt[i+1]=="\n"):
            if(num!=[]):
                char.append(ns.join(num))
                num=[]
            Parser(char)
            wp.append(char)
            char=[]
        else:
            if(pos.isalpha()):
                wasnumeric=False
            if(num!=[]):
                char.append(ns.join(num))
                num=[]
            try:
                char.append(symbols[pos])
            except:
                continue
        if(num!=[]):
                char.append(ns.join(num))
                num=[]
        we=False
def Parser(char):
    global inif
    global ist
    global ifs
    global wp
    ss=False
    w=False
    b=False
    ifr=None
    en=False
    inc=False
    ifc=False
    cds=""
    cdr=slice.cdr
    for i in range(len(char)):
        pos=char[i]
        if(pos=="//"):
            inc=True
        if(inif==False and b==True):
            ifr=[]
            char=[]
        if(pos=="IF"or pos=="WHILE"):
            if(pos=="WHILE"):
                w=True
            ifs=True
            inif=True
            state=char[i+1]
            try:
                ist=eval(state,var)
            except(SyntaxError,ValueError,RuntimeError):
                print(">SyntaxError: Unexceptable Condition in If statement")
            ifs=False
        if(pos=="}"):
            inif=False
        if((inif==False or (inif==True and ist==True))and inc==False and ifc==False):
            if(inif==True and en==True and w==True):
                ifr=wp[wp.index("WHILE"):wp.index("}")]
            if(pos=="FUNCTION_DEF"):
                cds=char[i+1]
                func.append([char[i+1]])
                cons=list(char[i+2])
                for con in cons:
                    var[con]=None
                ifc=True
            if(char[i-2]=="VARIABLE_INIT"):
                with warnings.catch_warnings():
                    warnings.simplefilter("error")
                    try:
                        var[char[i-1]]=eval(str(pos),var)
                    except:
                        print(">InvalidMathAssignmentError: Unexceptable math variable assignment. Perhaps you forgot an operator?")
            if(pos=="PRINT_VAR"):
                c=char[i+1]
                if(c=="*"):
                    n=True
                    c=c.replace("*","",1)
                    print(c)
                else:
                    n=False
                try:
                    if(n==False):
                        print(eval(c,var))
                    else:
                        print(eval(c,var),end="")
                except(ValueError,TypeError,RuntimeError,KeyError,IndexError):
                    try:
                        print(f">VarNotFoundError: var {str(char[i+1])} not found")
                    except(IndexError):
                        try:
                            s=var[char[i]].replace('"',"")
                            print(s)
                        except:
                            print(">SyntaxError: invalid printl statement")
            if(pos=="mv"):
                if(char[i+2]=="++"):
                    var[char[i+1]]+=1
            if(pos=="$kill"):
                exit()
            if(pos=="RUN"):
                a=func[char[i+1]]
                print(a)
            if(pos=="MOD"):
                if(char[i+1]=="windows"):
                    if(platform!="Windows"):
                        print(f">PlatformError:OS windows required. You are running {str(platform())}.")
                        return
                else:
                    if(os.path.exists(cdr+"Mods\\"+char[i+1])):
                        with open(cdr+"Mods\\"+char[i+1]) as f:
                            fr=f.read()
                        Lexer()
                        print("yes")
            if(pos=="HELP"):
                f=open(cdr+"README.txt","r")
                fs=f.read()
                f.close()
                print(fs)
            if(pos=="]"):
                ifc=False
                func[func.index(cds)][1]=wp[wp.index("[")+1:wp.index("]")]
            if(w==False):
                inif=False
                ist=None
                ifs=False
            if(pos=="||"):
                inc=False
                cds=""
            if(pos==len(char)and w==False):
                b=True
                en=True
        if(w==True):
            b=False
            if(eval(state,var)==True):
                try:
                    if(ifr!=None):
                        for i in ifr:
                            char.append(i)
                    else:
                        ifr=wp[wp.index("WHILE"):wp.index("}")]
                        for i in ifr:
                            char.append(i)
                except(ValueError,SyntaxError,RuntimeError)as e:
                    print(f">WhileLoopError:A {e} happend when proccessing this while loop")
    char=[]
