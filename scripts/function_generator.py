# multiple function generator

if 1: # buffer_init
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


=== Output log of process "function_generator.py", launched: "07 Jan 2015 15:28:51" ===
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25)
(
    __amps__ = memalloc(25);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; 
    _buffer_gen10(this.buf, this.size, __amps__, 25);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26)
(
    __amps__ = memalloc(26);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; 
    _buffer_gen10(this.buf, this.size, __amps__, 26);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27)
(
    __amps__ = memalloc(27);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; 
    _buffer_gen10(this.buf, this.size, __amps__, 27);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28)
(
    __amps__ = memalloc(28);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    _buffer_gen10(this.buf, this.size, __amps__, 28);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29)
(
    __amps__ = memalloc(29);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    __amps__[28] = h29; 
    _buffer_gen10(this.buf, this.size, __amps__, 29);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30)
(
    __amps__ = memalloc(30);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    __amps__[28] = h29; __amps__[29] = h30; 
    _buffer_gen10(this.buf, this.size, __amps__, 30);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31)
(
    __amps__ = memalloc(31);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    __amps__[28] = h29; __amps__[29] = h30; __amps__[30] = h31; 
    _buffer_gen10(this.buf, this.size, __amps__, 31);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32)
(
    __amps__ = memalloc(32);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    __amps__[28] = h29; __amps__[29] = h30; __amps__[30] = h31; __amps__[31] = h32; 
    _buffer_gen10(this.buf, this.size, __amps__, 32);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33)
(
    __amps__ = memalloc(33);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    __amps__[28] = h29; __amps__[29] = h30; __amps__[30] = h31; __amps__[31] = h32; 
    __amps__[32] = h33; 
    _buffer_gen10(this.buf, this.size, __amps__, 33);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34)
(
    __amps__ = memalloc(34);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    __amps__[28] = h29; __amps__[29] = h30; __amps__[30] = h31; __amps__[31] = h32; 
    __amps__[32] = h33; __amps__[33] = h34; 
    _buffer_gen10(this.buf, this.size, __amps__, 34);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35)
(
    __amps__ = memalloc(35);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    __amps__[28] = h29; __amps__[29] = h30; __amps__[30] = h31; __amps__[31] = h32; 
    __amps__[32] = h33; __amps__[33] = h34; __amps__[34] = h35; 
    _buffer_gen10(this.buf, this.size, __amps__, 35);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36)
(
    __amps__ = memalloc(36);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    __amps__[28] = h29; __amps__[29] = h30; __amps__[30] = h31; __amps__[31] = h32; 
    __amps__[32] = h33; __amps__[33] = h34; __amps__[34] = h35; __amps__[35] = h36; 
    _buffer_gen10(this.buf, this.size, __amps__, 36);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37)
(
    __amps__ = memalloc(37);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    __amps__[28] = h29; __amps__[29] = h30; __amps__[30] = h31; __amps__[31] = h32; 
    __amps__[32] = h33; __amps__[33] = h34; __amps__[34] = h35; __amps__[35] = h36; 
    __amps__[36] = h37; 
    _buffer_gen10(this.buf, this.size, __amps__, 37);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38)
(
    __amps__ = memalloc(38);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    __amps__[28] = h29; __amps__[29] = h30; __amps__[30] = h31; __amps__[31] = h32; 
    __amps__[32] = h33; __amps__[33] = h34; __amps__[34] = h35; __amps__[35] = h36; 
    __amps__[36] = h37; __amps__[37] = h38; 
    _buffer_gen10(this.buf, this.size, __amps__, 38);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39)
(
    __amps__ = memalloc(39);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    __amps__[28] = h29; __amps__[29] = h30; __amps__[30] = h31; __amps__[31] = h32; 
    __amps__[32] = h33; __amps__[33] = h34; __amps__[34] = h35; __amps__[35] = h36; 
    __amps__[36] = h37; __amps__[37] = h38; __amps__[38] = h39; 
    _buffer_gen10(this.buf, this.size, __amps__, 39);
);
function buffer_gen10(h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40)
(
    __amps__ = memalloc(40);
    __amps__[0] = h1; __amps__[1] = h2; __amps__[2] = h3; __amps__[3] = h4; 
    __amps__[4] = h5; __amps__[5] = h6; __amps__[6] = h7; __amps__[7] = h8; 
    __amps__[8] = h9; __amps__[9] = h10; __amps__[10] = h11; __amps__[11] = h12; 
    __amps__[12] = h13; __amps__[13] = h14; __amps__[14] = h15; __amps__[15] = h16; 
    __amps__[16] = h17; __amps__[17] = h18; __amps__[18] = h19; __amps__[19] = h20; 
    __amps__[20] = h21; __amps__[21] = h22; __amps__[22] = h23; __amps__[23] = h24; 
    __amps__[24] = h25; __amps__[25] = h26; __amps__[26] = h27; __amps__[27] = h28; 
    __amps__[28] = h29; __amps__[29] = h30; __amps__[30] = h31; __amps__[31] = h32; 
    __amps__[32] = h33; __amps__[33] = h34; __amps__[34] = h35; __amps__[35] = h36; 
    __amps__[36] = h37; __amps__[37] = h38; __amps__[38] = h39; __amps__[39] = h40; 
    _buffer_gen10(this.buf, this.size, __amps__, 40);
);
