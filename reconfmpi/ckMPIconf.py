#!/usr/bin/python
#coding=utf-8

import os, sys, re, shutil

filename    = 'mlx4_en.conf'
fullname    = ''
rep_str     = 'options mlx4_core pfctx=0 pfcrx=0 log_num_mtt=20 log_mtts_per_seg=4'

def prop_error():
    print 'Usage: python ckMPIconf.py [--path=/path/to/the/folder/]'

def expand_home(tpath):
    if tpath.startswith('~'): tpath = os.path.expanduser('~') + tpath[1:]
    if not tpath.endswith('/'): tpath = tpath + '/'
    return tpath

def make_path():
    global filename
    global fullname

    if len(sys.argv) == 1:
        fullname = os.path.abspath('.') + '/' + filename
    elif len(sys.argv) == 2 and sys.argv[1].startswith('--path='):
        fullname = expand_home(sys.argv[1][7:]) + filename
    else:
        prop_error()
        sys.exit(-1)

    #print fullname
    if not os.path.exists(fullname):
        print 'File path %s not found.' % (fullname)
        sys.exit(-1)

def match_regex():
    global fullname

    infile = open(fullname)
    p = re.compile(r'^ *options mlx4_core pfctx=0 pfcrx=0 *$', re.DOTALL)

    ncount = 0
    for s in infile:
        m = p.search(s)
        if m: ncount += 1

    infile.close()

    if ncount > 2: ncount = 2

    #if ncount == 0:
    #    print 'No line matched, so that this file is okay.'
    #elif ncount == 1:
    #    print 'Exactly one line matched. This file needs to be modified.'
    #else:
    #    print 'Multiple lines matched. There must be something wrong!'

    return ncount

def write_file():
    global filename
    global fullname
    global rep_str

    # make a copy first
    if not os.path.exists('/tmp/'+filename+'.bak'):
        shutil.copyfile(fullname, '/tmp/'+filename+'.bak')
    shutil.copyfile(fullname, fullname+'.bak')

    p = re.compile(r'^ *options mlx4_core pfctx=0 pfcrx=0 *$', re.DOTALL)
    infile = open(fullname+'.bak')
    outfile = open(fullname, 'w')

    for s in infile:
        m = p.search(s)
        if not m:
            outfile.write(s)
        else:
            outfile.write(rep_str)

    infile.close()
    outfile.close()

    print 'Rewrite finished.'

if __name__ == '__main__':
    make_path()
    out = match_regex()
    #if out == 1:
    #    write_file()
    sys.exit(out)
