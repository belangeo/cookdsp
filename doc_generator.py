# encoding: utf-8
import os, markdown, zipfile, datetime

VERSION = "0.5"
LOCATION = r'/home/olivier/.config/REAPER/Effects/belangeo'
MAINFILE = 'cookdsp.jsfx-inc'
EXAMPLES = 'cookdsp_examples'
REPOFOLDER = os.getcwd()
POBJECTSEXAMPLES = os.path.join(REPOFOLDER, "Pobjects_examples")

FOLDEROUT = './cookdspdoc'
EXAMPLEFOLDER = os.path.join(FOLDEROUT, EXAMPLES)
RELEASE = "cookdsp_%s_%s" % (VERSION, str(datetime.date.today()))
RELEASEFOLDER = os.path.join(FOLDEROUT, RELEASE)
TUTORIALS = "tutorials"
TUTORIALSFOLDER = os.path.join(FOLDEROUT, TUTORIALS)
TUTORIALEXAMPLE = 'cookdsp_tutorials'
TUTORIALSPATH = os.path.join(TUTORIALS, TUTORIALEXAMPLE)
TUTORIALEXAMPLEFOLDER = os.path.join(TUTORIALSFOLDER, TUTORIALEXAMPLE)

PRETTYTEMPLATE = './resources/prettify-template.js'
PRETTIFY = './resources/prettify.js'
COOKDSP_ICON = './resources/CookDSP-Icon.png'

os.system("rm -rf %s" % FOLDEROUT)
os.system("rm -rf %s" % RELEASEFOLDER)

os.mkdir(FOLDEROUT)
os.mkdir(EXAMPLEFOLDER)
os.mkdir(RELEASEFOLDER)
os.mkdir(TUTORIALSFOLDER)
os.mkdir(TUTORIALEXAMPLEFOLDER)

os.system('cp %s/* %s' % (POBJECTSEXAMPLES, EXAMPLEFOLDER))
os.system('cp "%s" %s' % (os.path.join(REPOFOLDER, MAINFILE), FOLDEROUT))
os.system('cp "%s" %s' % (os.path.join(REPOFOLDER, MAINFILE), RELEASEFOLDER))
os.system('cp "%s" %s' % (os.path.join(REPOFOLDER, MAINFILE), LOCATION))
os.system('cp -r "%s" %s' % (os.path.join(REPOFOLDER, "cookdsp"), FOLDEROUT))
os.system('cp -r "%s" %s' % (os.path.join(REPOFOLDER, "cookdsp"), RELEASEFOLDER))
os.system('cp -r "%s" %s' % (os.path.join(REPOFOLDER, "cookdsp"), LOCATION))

functionnames = []

def zipdir(path, zipname):
    zipf = zipfile.ZipFile(zipname, 'w')
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file))
    zipf.close()

index = open(os.path.join(FOLDEROUT, 'index.html'), 'w')
index_head = """
<link rel="stylesheet" type="text/css" href="cookdsp.css">
<h1 align="center">JSFX - CookDSP Library</h1>
<h5 align="center">Author: Olivier Belanger (belangeo@gmail.com)</h5>

<HR>

<div>
<table align="center" width=50&#37;>
    <tr align="center">
        <td><a href="#documentation">Documentation</a></td>
        <td><a href="#download">Downloads</a></td>
        <td><a href="#install">Installation</a></td>
        <td><a href="#tutorials">Tutorials</a></td>
        <td><a href="#donation">Donation</a></td>
    </tr>
</table>
</div>

<HR>

<p align="center"><IMG SRC="CookDSP-Icon.png" ALT="" WIDTH=100 HEIGHT=100></p>

<br>
<div>The CookDSP library is a set of functions and objects to help 
the creation of plugins inside the Reaper software with the built-in 
JS language. JS is a scripting language which is compiled on the 
fly and allows you to modify and/or generate audio and MIDI processes, as well 
as draw custom vector based UI and analysis displays.</div>

<br>
<div>One must import the file <i>cookdsp.jsfx-inc</i> in the plugin
before using any of the functions documented here. Importing a file 
is very easy with the <b>import</b> keyword: </div>

<pre>
import cookdsp.jsfx-inc
</pre> 
<br>

<HR>

<h2 id="documentation">API documentation (version %s)</h2>

<div> Documentation of functions and objects of the library.
"""
index.write(index_head % VERSION)

page_template = """
<link rel="stylesheet" type="text/css" href="cookdsp.css">
<link href="prettify.css" type="text/css" rel="stylesheet" />
<script type="text/javascript" src="prettify.js"></script>
<body onload="prettyPrint()">

<div style="font-size: 9pt;">JSFX - CookDSP version %s documentation</div>
<HR>
<div>
<table class="navigate" width="100&#37;">
    <tr>
        <td class="prev"><a href="%s.html">%s</a></td>
        <td class="center"><a href="index.html">home</a></td>
        <td class="next"><a href="%s.html">%s</a></td>
    </tr>
</table>
</div>
<HR>

%s

<HR>
<div>Download example : <a href="cookdsp_examples/%s" download>%s</a></div>
<HR>
<div>See the source file : <a href="cookdsp/%s">%s</a></div>
<HR>
<div style="font-size: 9pt;">(c) Olivier Belanger, 2020</div>

"""
def export_example(name, text):
    lines = text.splitlines(True)
    text = "// JSFX-CookDSP - %s - manual example\n// (c) Olivier Belanger - 2020 - belangeo@gmail.com\n\n" % name
    skip = True
    for line in lines:
        if skip and line.strip() == "":
            continue
        skip = False
        if len(line) > 4:
            text = text + line[4:]
        else:
            text = text + line
    filename = "cookdsp_"+name
    with open(os.path.join(EXAMPLEFOLDER, filename), "w") as f:
        f.write(text)
    return filename

def export_tutorial(name, text):
    lines = text.splitlines(True)
    text = "// JSFX-CookDSP - %s - tutorial example\n// (c) Olivier Belanger - 2020 - belangeo@gmail.com\n\n" % name
    skip = True
    for line in lines:
        if skip and line.strip() == "":
            continue
        skip = False
        if len(line) > 4:
            text = text + line[4:]
        else:
            text = text + line
    filename = "cookdsp_tutorial_"+name
    with open(os.path.join(TUTORIALEXAMPLEFOLDER, filename), "w") as f:
        f.write(text)
    return filename

with open(r"%s" % os.path.join(LOCATION, MAINFILE), 'r') as f:
    lines = f.readlines()

# Add the pobjects file in the auto-generated documentation.
lines.append("/* Polyphonic objects (multi-channel expansion) */")
lines.append("import cookdsp/pobjects.jsfx-inc")

names = []
for line in lines:
    if line.startswith("import"):
        file = line.strip().replace("import ", "")
        sourcename = os.path.split(file)[1]
        file = os.path.join(LOCATION, file)
        with open(file, 'r') as f:
            text = f.read()
        pos2 = 0
        pos1 = text.find('/*', pos2)
        while (pos1 != -1):
            pos2 = text.find('*/', pos1)
            page = text[pos1:pos2]
            ret1 = page.find('\n')
            ret2 = page.find('\n', ret1+1)
            last = page.rfind('\n')
            name = page[ret1+1:ret2].strip().replace(' ', '_').lower()
            names.append(name)
            pos1 = text.find('/*', pos2)

for line in lines:
    if line.startswith("import"):
        file = line.strip().replace("import ", "")
        sourcename = os.path.split(file)[1]
        file = os.path.join(LOCATION, file)
        with open(file, 'r') as f:
            text = f.read()
        ### get function names for syntax coloring ###
        for line in text.splitlines():
            if line.startswith("function "):
                fn1 = len("function ")
                try:
                    fn2 = line.index("(")
                except:
                    continue
                fname = line[fn1:fn2]
                if fname not in functionnames and not fname.startswith("_"):
                    functionnames.append(fname)
        ##############################################
        pos2 = 0
        pos1 = text.find('/*', pos2)
        while (pos1 != -1):
            pos2 = text.find('*/', pos1)
            page = text[pos1:pos2]
            ret1 = page.find('\n')
            ret2 = page.find('\n', ret1+1)
            last = page.rfind('\n')
            name = page[ret1+1:ret2].strip().replace(' ', '_').lower()
            page = page[ret1+1:last]
            if "===" in page:
                examplefile = ""
                where = page.find("Example")
                if where != -1:
                    tmp = page.find('\n', where)
                    tmp = page.find('\n', tmp+1)
                    extext = page[tmp:]
                    examplefile = export_example(name, extext)
                current = names.index(name)
                if current == 0:
                    prev1, prev2 = "", ""
                else:
                    prev1, prev2 = names[current-1], "prev"
                if current == len(names)-1:
                    next1, next2 = "", ""
                else:
                    next1, next2 = names[current+1], "next"
                pagename = os.path.join(FOLDEROUT, "%s.html" % name)
                html = markdown.markdown(page)
                html = page_template % (VERSION, prev1, prev2, next1, next2, html, examplefile, examplefile, sourcename, sourcename)
                html = html.replace('<code>', '<code class="prettyprint">')
                with open(pagename, 'w') as f:
                    f.write(html)
                desc = page.splitlines()[3]
                index.write('- <a href="%s.html"><b>%s</b></a>: %s<br>\n' % (name, name, desc))
            else:
                index.write('</div>\n\n<div><br><b>%s</b><br>\n' % page)
            pos1 = text.find('/*', pos2)
    elif line.startswith("/*"):
        index.write('</div>\n<h3>%s</h3>\n\n<div>' % line.replace("/","").replace("*","").strip())

index.write("""
<HR>
<h2 id="download">Downloads</h2>

- Download the library: <a href="%s" download>%s</a>
<br><br>
- Download all CookDSP examples as a zip archive: <a href="%s" download>%s</a>
<br><br>
- Download all CookDSP tutorial examples as a zip archive: <a href="%s" download>cookdsp_tutorials.zip</a>
<br><br>
- Download the mono FFT plugin template: <a href="cookdsp/fft-mono-template" download>fft-mono-template</a>
<br><br>
- Download the stereo FFT plugin template: <a href="cookdsp/fft-stereo-template" download>fft-stereo-template</a>
<br><br>
- Download the mono Phase Vocoder plugin template: <a href="cookdsp/pv-mono-template" download>pv-mono-template</a>
<br><br>
- Download the stereo Phase Vocoder plugin template: <a href="cookdsp/pv-stereo-template" download>pv-stereo-template</a>

<HR>

""" % (RELEASE+".zip", RELEASE+".zip", EXAMPLES+".zip", EXAMPLES+".zip", TUTORIALSPATH+".zip"))

index.write(r"""
<h2 id="install">Installation</h2>

<div>To install the CookDSP library, unzip the content of the download in the Reaper's Effects directory.

The location of this directory is (where &lt;username&gt; should be replaced by the name of the user's home
folder) :</div>

<br>
<b>Windows XP</b> : 

<pre>
C:\Documents and Settings\&lt;username&gt;\Application Data\REAPER\Effects
</pre>


<b>Windows Vista/7/8</b> : 

<pre>
C:\Users\&lt;username&gt;\AppData\Roaming\REAPER\Effects
</pre>

<b>OSX</b> : 

<pre>
/Users/&lt;username&gt;/Library/Application Support/REAPER/Effects 
</pre>

<b>linux (native Reaper) </b> : 

<pre>
~/.config/REAPER/Effects 
</pre>

<b>linux (Reaper with Wine) </b> : 

<pre>
~/.wine/drive_c/users/&lt;username&gt;/Application Data/REAPER/Effects 
</pre>
<br>
<HR>
""")

tuthead = """
<link rel="stylesheet" type="text/css" href="../cookdsp.css">
<link href="../prettify.css" type="text/css" rel="stylesheet" />
<script type="text/javascript" src="../prettify.js"></script>
<body onload="prettyPrint()">

<div style="font-size: 9pt;">JSFX - CookDSP tutorials</div>
<HR>
<div>
<table class="navigate" width="100&#37;">
    <tr>
        <td class="prev"><a href="%s.html">%s</a></td>
        <td class="center"><a href="../index.html">home</a></td>
        <td class="next"><a href="%s.html">%s</a></td>
    </tr>
</table>
</div>
<HR>
"""

tuttail = """
<HR>
<div>Download full code : <a href="%s" download>%s</a></div>
<HR>
<div style="font-size: 9pt;">(c) Olivier Belanger, 2020</div>
"""
index.write('<h2 id="tutorials">Tutorials (Under development...)</h2>')

tutorials = sorted([f for f in os.listdir(TUTORIALS) if f.endswith(".md")])
tutorialsNoExt = [os.path.splitext(tut)[0] for tut in tutorials]
tutorialsHtmlNames = ["%s.html" % tut for tut in tutorialsNoExt]
for tut in tutorials:
    current = tutorials.index(tut)
    name = tutorialsNoExt[current]
    with open(os.path.join(TUTORIALS, tut), "r") as f:
        text = f.read()
        pos = text.find("Complete plugin")
        pos = text.find("\n", pos) + 1
        export_tutorial(name, text[pos:])
        desc = text.splitlines(False)[0]
        html = markdown.markdown(text)
    htmlname = tutorialsHtmlNames[current]
    if current == 0:
        prev1, prev2 = "", ""
    else:
        prev1, prev2 = tutorialsNoExt[current-1], "prev"
    if current == len(tutorials)-1:
        next1, next2 = "", ""
    else:
        next1, next2 = tutorialsNoExt[current+1], "next"

    with open(os.path.join(TUTORIALSFOLDER, htmlname), "w") as f:
        html = html.replace('<code>', '<code class="prettyprint">')
        f.write(tuthead % (prev1, prev2, next1, next2))
        f.write(html)
        f.write(tuttail % (os.path.join(TUTORIALEXAMPLE, "cookdsp_tutorial_%s" % name), name))
    index.write('<a href="%s">%s</a> : %s<br>' % (os.path.join(TUTORIALS, htmlname), name, desc))


index.write("""
<HR>
<h2 id="donation">Donation</h2>

<div>This project is developed by Olivier Belanger on his free time to provide a 
complete dsp library to ease the plugin creation within Reaper. If you feel this 
project is useful to you and want to support it and it's future development, please 
consider donating money.</div>

<p align="center"><a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=9CA99DH6ES3HA" rel="nofollow"><img src="https://www.paypal.com/en_US/i/btn/btn_donateCC_LG.gif" /></a> </p>

<HR>
<div style="font-size: 9pt;">(c) Olivier Belanger - 2020 - belangeo@gmail.com</div>
""")
index.close()

with open(PRETTYTEMPLATE, "r") as f:
    tmptext = f.readlines()

with open(PRETTIFY, "w") as f:
    for i in range(95):
        f.write(tmptext[i])
    f.write('  var COOKDSP_KEYWORDS = ["')
    for i, fname in enumerate(functionnames):
        f.write("%s," % fname)
        if i % 8 == 0:
            f.write('" +\n      "')
    f.write('"];\n')
    for i in range(95, len(tmptext)):
        f.write(tmptext[i])

os.system("cp resources/*.css %s" % FOLDEROUT)
os.system("cp %s %s" % (PRETTIFY, FOLDEROUT))
os.system("cp %s %s" % (COOKDSP_ICON, FOLDEROUT))

os.system('cp -r "%s" %s' % (EXAMPLEFOLDER, LOCATION))

rootdir = os.getcwd()
os.chdir(FOLDEROUT)
zipdir(EXAMPLES, EXAMPLES+".zip")
zipdir(RELEASE, RELEASE+".zip")
zipdir(TUTORIALSPATH, TUTORIALSPATH+".zip")

os.chdir(rootdir)
rep = input("Do you want to upload to ajax server (y/n) ? ")
if rep == "y":
    os.system("scp -r cookdspdoc jeadum1@ajaxsoundstudio.com:/home/jeadum1/ajaxsoundstudio.com")
