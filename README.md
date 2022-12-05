# Slicetext
## Slicetext is a high-level, interpreted programming language created by Theo Kozak in his free time.

**RUNNING**

in a python terminal, run **import slicetext as slice**
to run a slice file, then run **slice.run("FILENAME.txt","optional:PATH_TO_DIRECTORY_FOR_FASTER_LOAD_TIME")**
the shell can be accessed with **slice.shell()**

**DOCUMENTATION**

*Declaring Variables:*

**var VARIABLE_NAME=VALUE[either str type, num type, or py type]**

*Printing:*

**printl:NAME_OF_VARIABLE_YOU_WANT_TO_PRINT;**

*If:*

**if BOOLEAN_CONDITION_PHRASED_LIKE_PYTHON{**
**CODE**
**}**

*Comments:*

**//COMMENT||**


*Import Modules*

**mod FILE_NAME.txt;**

alt keyword:

**require FILE_NAME.txt**

**EXAMPLES**

*Hello, World:*

**printl:"foo";**

*Output:*

"Hello, World"

*Logic*

**foo=17**
**bar=17**
**baz="yay"**
**if foo==bar{**
**printl:baz;**
**}**

*Output:*

"yay"
