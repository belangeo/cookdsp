# multiple function generator

X = 2
if X == 0: # buffer_init
    head = "function buffer_gen10(%s)\n(\n"

    head2 = "    __amps__ = memalloc(%d);"
    
    body = "__amps__[%d] = h%d; "

    close = "\n    _buffer_gen10(this.buf, this.size, __amps__, %d);\n);"

    for i in range(25, 41):
        t = ""
        args = ""
        for j in range(i):
            args = args + "h%d" % (j+1)
            if j != (i-1):
                args = args + " "
        t = head % args
        t2 = head2 % i
        buf = ""
        for j in range(i):
            if (j%4) == 0:
                buf = buf + "\n    "
            buf = buf + body % (j, (j+1))
        t = t + t2 + buf + close % i
        print t

elif X == 1: # list functions generator
    head = "function list(%s)\n(\n"
    alloc = "    this.buf = memalloc(%d);\n    this.buf[%d] = %d;"
    body = "this.buf[%d] = h%d; "
    close = "\n    this.buf;\n);"
    for i in range(1, 41):
        args = ""
        for j in range(i):
            args = args + "h%d" % (j+1)
            if j != (i-1):
                args = args + " "
        buf = ""
        for j in range(i):
            if (j%4) == 0:
                buf = buf + "\n    "
            buf = buf + body % ((j+1), (j+1))

        t = head % args
        t2 = alloc % ((i+1), 0, i)
        t = t + t2 + buf + close
        print t
        
elif X == 2: # tmplist generator
    head = "function tmplist(%s)\n(\n"
    alloc = "    this.buf = _TMPLISTFIRSTPOS_;\n    this.buf[%d] = %d;"
    body = "this.buf[%d] = h%d; "
    close = "\n    this.buf;\n);"
    for i in range(1, 41):
        args = ""
        for j in range(i):
            args = args + "h%d" % (j+1)
            if j != (i-1):
                args = args + " "
        buf = ""
        for j in range(i):
            if (j%4) == 0:
                buf = buf + "\n    "
            buf = buf + body % ((j+1), (j+1))

        t = head % args
        t2 = alloc % (0, i)
        t = t + t2 + buf + close
        print t
