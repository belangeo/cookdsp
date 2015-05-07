import markdown, os, codecs

MDFILE = "cookdsp_workshop.md"
OUTFOLDER = "cookdsp_workshop_html"

if not os.path.isdir(OUTFOLDER):
    os.mkdir(OUTFOLDER)

with codecs.open(MDFILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

encoding =  """<head><meta charset="UTF-8"></head>
<link rel="stylesheet" type="text/css" href="cookdsp.css">
<link href="prettify.css" type="text/css" rel="stylesheet" />
<script type="text/javascript" src="prettify.js"></script>
<body onload="prettyPrint()">
"""

navigate = """
<HR>
<div>
<table class="navigate" width="100&#37;">
    <tr>
        <td class="prev"><a href="%s">%s</a></td>
        <td class="next"><a href="%s">%s</a></td>
    </tr>
</table>
</div>
<HR>
"""

header = []
filelist = [[]]
file = 0
for line in lines: 
    if line.startswith("%"):
        header.append(line)
        continue
    if line.startswith("^"):
        continue
    if "-----" in line:
        filelist.append([])
        file += 1
    elif "http" in line:
        line = line.replace("->", "").replace("<-", "").replace("`", "")
        line = "[%s](%s)\n" % (line.strip(), line.strip())
        filelist[file].append(line)
    else:
        line = line.replace("->", "").replace("<-", "")
        if line.strip() == "//" : line = "\n"
        filelist[file].append(line)

count = 0
for lst in filelist:
    str = ""
    with codecs.open(os.path.join(OUTFOLDER, "node%02d.html" % count), "w", encoding="utf-8") as f:
        for line in lst:
            str = str + line
        html = encoding
        if count == 0:
            prev1, prev2 = "", ""
        else:
            prev1, prev2 = "node%02d.html" % (count - 1), "prev"
        if count == len(filelist)-1:
            next1, next2 = "", ""
        else:
            next1, next2 = "node%02d.html" % (count + 1), "next"
        html = html + navigate % (prev1, prev2, next1, next2)
        html = html + markdown.markdown(str)
        html = html.replace('<code>', '<code class="prettyprint">')
        f.write(html)
    count += 1

    
