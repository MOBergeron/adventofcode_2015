#!/usr/bin/env python
import os
import re
import itertools

P = "^Sue (?P<n>\d+): (?P<o1>[a-z]+): (?P<n1>\d+), (?P<o2>[a-z]+): (?P<n2>\d+), (?P<o3>[a-z]+): (?P<n3>\d+)$"
ASO = {"children": 3,
	"cats": 7,
	"samoyeds": 2,
	"pomeranians": 3,
	"akitas": 0,
	"vizslas": 0,
	"goldfish": 5,
	"trees": 3,
	"cars": 2,
	"perfumes": 1}


def parseInput(inp):
	r = re.compile(P)

	a = {}
	for c in content.split('\n'):
		m = r.match(c)
		if(m):
			a[int(m.group('n'))] = {}
			a[int(m.group('n'))][m.group('o1')] = int(m.group('n1'))
			a[int(m.group('n'))][m.group('o2')] = int(m.group('n2'))
			a[int(m.group('n'))][m.group('o3')] = int(m.group('n3'))

	return a

def day16(pi,p=1):
	nr = []
	for i in range(1, len(pi.keys())+1):
		for k,v in ASO.items():
			if(k in pi[i].keys()):
				if(p==2 and k in ("cats","trees") and pi[i][k] <= ASO[k]):
					if(pi[i][k] <= ASO[k]):
						if(i not in nr ): nr.append(i)
				elif(p==2 and k in ("pomeranians","goldfish")):
					if(pi[i][k] >= ASO[k]):
						if(i not in nr ): nr.append(i)
				elif(not pi[i][k] == ASO[k]):
					if(i not in nr ): nr.append(i)


	for i in pi.keys():
		if(i not in nr):
			print(i)

if __name__ == '__main__':
	f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
	content = f.read()
	f.close()
	day16(parseInput(content))
	day16(parseInput(content),2)