#!/usr/bin/env python
import os
import json

f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
content = json.loads(f.read())
f.close()

def f(n, j, r=0):
    if(isinstance(j,list)):
        for v in j:
            if(isinstance(v,int)):
                n += int(v)
            if(isinstance(v,list)):
                n = f(n,v,r)
            if(isinstance(v,dict)):
                n = f(n,v,r)
    if(isinstance(j,dict)):
        if(r==0 or not "red" in j.values()):
            for k,v in j.items():
                if(isinstance(v,int)):
                    n += int(v)
                if(isinstance(v,list)):
                    n = f(n,v,r)
                if(isinstance(v,dict)):
                    n = f(n,v,r)

    return n

print("Part 1 : {}".format(f(0, content)))
print("Part 2 : {}".format(f(0, content, 1)))
