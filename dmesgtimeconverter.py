#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import datetime


'''
dmsg content:
[3247380.221604] sdfpro[37237]: segfault at 7f17870580bf ip 00007f17870580bf sp 00007f177e8bb150 error 14

uptime content:
  8:59am  up 438 天  6:23,  1 个用户，平均负载：36.60, 56.57, 74.35
'''

def getboottime():
    '''
    return bootime datetime
    '''
    import subprocess
    import re
    output = subprocess.Popen(["uptime"], stdout=subprocess.PIPE).communicate()[0]
    m = re.match(r'''.+up (\d+)\D+(\d+):(\d+).+''', output)
    duration = datetime.timedelta(days=int(m.group(1)), hours=int(m.group(2)), minutes=int(m.group(3)))
    return datetime.datetime.today() - duration

def main():
    boottime = getboottime()
    
    for aline in sys.stdin:
        if (len(aline.strip()) !=0):
            arrayline = aline.split()
            if len(arrayline)>1 and arrayline[0][0] == '[' and arrayline[0][-1] == ']':                
                arraytime = arrayline[0][1:-1].split(".")
                elapsedsecond = long(arraytime[0])
                elapsedmicro = long(arraytime[1])                
                sys.stdout.write(aline.replace(arrayline[0][1:-1], str(boottime + datetime.timedelta(seconds=elapsedsecond, microseconds=elapsedmicro))))               
    

if __name__ == "__main__":
    main()