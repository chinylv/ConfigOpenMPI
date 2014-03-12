#!/usr/bin/python
#coding=utf-8

import os

#cmd = 'python ckMPIconf.py'
#loop_cmd = 'for i in `seq -w 1 332` ; do printf "node$i\t";rsh node$i $1 ; sleep 0.3 ; done'
py_cmd = 'python /home/charles/reconfmpi/ckMPIconf.py --path=/etc/modprobe.d/'

def main():
    global py_cmd
    out = os.system(py_cmd)
    out = out >> 8
    if out == 0:
        print 'Already modified'
    elif out == 1:
        print 'To be modified'
    elif out == 2:
        print 'Multiple lines found'
    else:
        print 'Usage error. Please double check!'
    #print out

if __name__ == '__main__':
    main()
