#!/usr/bin/env python
import os
import math
from copy import deepcopy

f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
content = f.read()
f.close()

row = int(math.sqrt(len(content.replace('\n',''))))
col = row
m = [[] for _ in range(row)]

def lightOn(m, x, y):
	lo = 0
	if(x-1 >= 0):
		if(m[x-1][y]): lo += 1
	if(y-1 >= 0):
		if(m[x][y-1]): lo += 1
	if(x+1 < row):
		if(m[x+1][y]): lo += 1
	if(y+1 < col):
		if(m[x][y+1]): lo += 1
	if(x-1 >= 0 and y-1 >= 0):
		if(m[x-1][y-1]): lo += 1
	if(x-1 >= 0 and y+1 < col):
		if(m[x-1][y+1]): lo += 1
	if(x+1 < row and y-1 >= 0):
		if(m[x+1][y-1]): lo += 1
	if(x+1 < row and y+1 < col):
		if(m[x+1][y+1]): lo += 1
	return lo

def day18(m, p=1):
	mt = [[False for _ in range(col)] for _ in range(row)]
	for _ in range(100):
		for x in range(row):
			for y in range(col):
				lo = lightOn(m, x, y)
				if(m[x][y] and not lo in (2,3)):
					mt[x][y] = True
				elif(not m[x][y] and lo == 3):
					mt[x][y] = True
		if(p==2):
			mt[0][0] = False
			mt[row-1][0] = False
			mt[0][col-1] = False
			mt[row-1][col-1] = False

		for x in range(row):
			for y in range(col):
				m[x][y] = not m[x][y] if mt[x][y] else m[x][y]
				mt[x][y] = False
	return len([x for n in m for x in n if x])

y = 0
for c in content:
	if(c == '\n'):
		y+=1
	else:
		if(c == "#"):
			m[y].append(True)
		else:
			m[y].append(False)

print("Part 1 : {}".format(day18(deepcopy(m))))
m[0][0] = True
m[row-1][0] = True
m[0][col-1] = True
m[row-1][col-1] = True
print("Part 2 : {}".format(day18(m, 2)))
