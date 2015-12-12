#!/usr/bin/env python
import os
import re
import itertools

f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
content = f.read()
f.close()

P = "^(?P<f>[a-zA-Z]+) to (?P<t>[a-zA-Z]+) = (?P<d>\d+)$"
r = re.compile(P)

cy = []
dy = []
t = []

for c in content.split('\n'):
    m = r.match(c)
    if(m):
        if(not m.group('f') in cy):
            cy.append(m.group('f'))
        if(not m.group('t') in cy):
            cy.append(m.group('t'))

        dy.append(m.groups())

x = 0
for ip in itertools.permutations(cy, len(cy)):
    t.append(0)
    for i in range(len(ip)):
        if(not i == 0):
            for d in dy:
                if((d[0] == ip[i-1] and d[1] == ip[i]) or (d[1] == ip[i-1] and d[0] == ip[i])):
                    t[x] += int(d[2])
                    break
    x+=1
l = 1000000
h = 0
for i in t:
    if(l > i):
        l = i
    if(h < i):
        h = i

print("Shortest : {}".format(l))
print("Longest : {}".format(h))
