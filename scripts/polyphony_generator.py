# Polyphonic-objects generator
import os

LOCATION = '..'
MAINFILE = 'cookdsp.jsfx-inc'
OUTPATH = os.path.join(LOCATION, "cookdsp", "pobjects.jsfx-inc")
DOCFILE = 'Pobjects_doc.md'

objnames = {"delay": [], "sdelay": [], "moog": [], "comb": [], "allpass": [],
            "lop": [], "hip": [], "bp": [], "butlp": [], "buthp": [],
            "butbp": [], "butbr": [], "apass": [], "biquad": [],
            "follow": [], "zcross": [], "yin": [], "onset": [],
            "phasor": [], "sine": [], "random": [], "masr": [],
            "compress": [], "gate": [], "expand": [], "eq": [], "grains": [],
            "disto": [], "harmon": [], "wgverb": [], "blosc": [], "chorus": [],
            "flanger": [], "waveguide": []
            }

# Open cookdsp main file
with open(r"%s" % os.path.join(LOCATION, MAINFILE), 'r') as f:
    lines = f.readlines()
# Parse main file lines
for line in lines:
    if line.startswith("import") and "pobjects.jsfx-inc" not in line:
        # Open library file
        file = line.strip().replace("import ", "")
        sourcename = os.path.split(file)[1]
        file = os.path.join(LOCATION, file)
        with open(file, 'r') as f:
            text = f.read()
        # Parse library file to find function names
        for line in text.splitlines():
            if line.startswith("function "):
                fn1 = len("function ")
                try:
                    fn2 = line.index("(")
                except:
                    continue
                fname = line[fn1:fn2]
                if not fname.startswith("_"):
                    for obj in objnames:
                        if fname.startswith(obj):
                            arglist = line[fn2:].replace("(", "").replace(")", "").split(" ")
                            if '' in arglist:
                                arglist.remove('')
                            num = len(arglist)
                            objnames[obj].append((fname, num))

objlist = sorted(objnames.keys())

objlist = ["`P%s`" % obj for obj in objlist]
objstr = ""
for i, obj in enumerate(objlist):
    objstr = objstr + obj + ", "
    if i % 8 == 7:
        objstr += "\n"
with open(DOCFILE, "r") as f:
    text = f.read()
docstr = text % objstr

# Open export file (pobjects.jsfx-inc)
f = open(OUTPATH, "w")
init = "@init\n\n"
f.write(init)
f.write(docstr)

# Create functions for listed polyphonic-objects
for obj in objnames:
    objname = obj
    for i, str in enumerate(objnames[obj]):
        if str[0] == objname:
            break
    objinit = objnames[obj].pop(i)
    initargs = objinit[1]
    argnames = objnames[obj]

    # Initializer
    args = " ".join(["lst%d" % (x+1) for x in range(initargs)])
    creator = "function P%s"
    arguments = "(%s)\n(\n"
    alloc = """    this.num = lst1[0];
    this.outlist = memalloc(this.num + 1);
    this.outlist[0] = this.num;
"""
    head = creator % objname + arguments % args + alloc
    objects = ""
    for i in range(40):
        i1 = i + 1
        curargs = ", ".join(["lst%d[%d]" % ((x+1),i1) for x in range(initargs)])
        objects = objects + "    this.num > %d ? this.%d.%s(%s);\n" % (i, i, objname, curargs)
    close = ");\n"
    f.write(head + objects + close)

    # Methods
    for arg in argnames:
        name, num = arg[0], arg[1]
        if name.endswith("_do"): ### do function
            close = "    this.outlist;\n);\n\n"
            if num == 1:
                creator = "function P%s_do(signal)\n(\n    num = signal[0];\n"
                head = creator % objname
                objects = ""
                for i in range(40):
                    i1 = i + 1
                    objects = objects + "    this.num > %d ? this.outlist[%d] = this.%d.%s_do(signal[(%d %% num) + 1]);\n" % (i, i1, i, objname, i)
                f.write(head + objects + close)
            else:
                creator = "function P%s_do()\n(\n"
                head = creator % objname
                objects = ""
                for i in range(40):
                    i1 = i + 1
                    objects = objects + "    this.num > %d ? this.outlist[%d] = this.%d.%s_do();\n" % (i, i1, i, objname)
                f.write(head + objects + close)
        elif "read" in name: ### *read* function
            close = "    this.outlist;\n);\n\n"
            args = " ".join(["lst%d" % (x+1) for x in range(num)])
            creator = "function P%s(%s)\n(\n"
            head = creator % (name, args)
            objects = ""
            for i in range(40):
                i1 = i + 1
                curargs = ", ".join(["lst%d[%d]" % ((x+1),i1) for x in range(num)])
                objects = objects + "    this.num > %d ? this.outlist[%d] = this.%d.%s(%s);\n" % (i, i1, i, name, curargs)
            f.write(head + objects + close)
        else: ### every other function
            args = " ".join(["lst%d" % (x+1) for x in range(num)])
            creator = "function P%s(%s)\n(\n"
            head = creator % (name, args)
            objects = ""
            for i in range(40):
                i1 = i + 1
                curargs = ", ".join(["lst%d[%d]" % ((x+1),i1) for x in range(num)])
                objects = objects + "    this.num > %d ? this.%d.%s(%s);\n" % (i, i, name, curargs)
            close = ");\n"
            f.write(head + objects + close)

