#!/usr/bin/env python
import os
import re
import itertools

f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
content = f.read()
f.close()

P = "^(?P<f>[A-Z]).+(?P<a>gain|lose) (?P<n>\d+).+(?P<t>[A-Z]).+\.$"
r = re.compile(P)

def f(p=[]):
	u = True if p else False
	d = {}

	for c in content.split('\n'):
		m = r.match(c)
		if(m):
			if(m.group('f') not in p):
				p.append(m.group('f'))
				if(u):
					d[(m.group('f'),'O')] = 0
					d[('O',m.group('f'))] = 0
			n = int(m.group('n')) * (-1 if m.group('a') == "lose" else 1)
			d[(m.group('f'),m.group('t'))] = n

	t = []
	x = 0
	hv = 0

	ips = list(itertools.permutations(p,len(p)))
	for ip in ips:
		t.append(0)
		for i in range(len(ip)):
			t[x] += d[(ip[i],ip[i-1])] + d[(ip[i],ip[i+(-len(ip)+1 if i == len(ip)-1 else 1)])]
		hv = t[x] if(hv < t[x]) else hv
		x+=1

	return hv

print(f())
print(f(['O']))
