import os
import sys

counter = 500
foldercpp = os.path.join("src", "cpp")
folderheaderonly = os.path.join("src", "headeronly")

for i in range(counter):
    strnum = str(i)
    with open(os.path.join(foldercpp, "print"+strnum+".h"), "w") as f:
        f.write("#pragma once\n")
        f.write("void print"+strnum+"();\n")

    with open(os.path.join(foldercpp, "print"+strnum+".cpp"), "w") as f:
        f.write("#include <stdio.h>\n")
        f.write("#include \"print"+strnum+".h\"\n")
        f.write("void print"+strnum+"(){\n")
        for j in range(700):
            f.write("printf(\"value: %d\","+str(j)+");\n")
        f.write("}\n")

    with open(os.path.join(folderheaderonly, "print"+strnum+".h"), "w") as f:
        f.write("#pragma once\n")
        f.write("#include <stdio.h>\n")
        f.write("inline void print"+strnum+"(){\n")
        for j in range(700):
            f.write("printf(\"value: %d\","+str(j)+");\n")
        f.write("}\n")

with open(os.path.join(folderheaderonly, "main.cpp"), "w") as f:
    for i in range(counter):
        strnum = str(i)
        f.write("#include \"print"+strnum+".h\"\n")

with open(os.path.join(foldercpp, "main.cpp"), "w") as f:
    for i in range(counter):
        strnum = str(i)
        f.write("#include \"print"+strnum+".h\"\n")

with open(os.path.join(foldercpp, "main.cpp"), "a+") as f:
    f.write("void main(){\n")
    for i in range(counter):
        strnum = str(i)
        f.write("print"+strnum+"();\n")
    f.write("}\n")

with open(os.path.join(folderheaderonly, "main.cpp"), "a+") as f:
    f.write("void main(){\n")
    for i in range(counter):
        strnum = str(i)
        f.write("print"+strnum+"();\n")
    f.write("}\n")
