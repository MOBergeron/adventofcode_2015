#!/usr/bin/env python
import os
import itertools

EGGNOG = 150

def day17(inp):
	a = []
	z = []
	for i in range(1,len(inp)+1):
		b = list(itertools.combinations(inp,i))
		for c in b:
			if(sum(c) == EGGNOG):
				a.append(c)
				z.append(len(c))

	print("Part 1 : {}".format(len(a)))
	x = 0
	for i in range(len(a)):
		if(len(a[i]) == min(z)):
			x+=1
	print("Part 2 : {}".format(x))


if __name__ == '__main__':
	f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
	content = f.read()
	f.close()
	c = [int(x) for x in content.split('\n')]
	day17(c)