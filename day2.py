#!/usr/bin/env python
import os
import re

PATTERN = "(\d+)x(\d+)x(\d+)"
REGEX_COMPILED = re.compile(PATTERN)

f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
content = f.read()
f.close()

tWrp = 0
tRib = 0

for c in content.split('\n'):
	match = REGEX_COMPILED.match(c)
	if(match):
		l,w,h = (int(i) for i in match.groups())
		lw = l*w
		wh = w*h
		hl = h*l

		lowest = lw

		if(lowest > wh):
			lowest = wh
		if(lowest > hl):
			lowest = hl

		if(l <= w and w <= h):
			low1 = l
			low2 = w
		elif(l <= h and h <= w):
			low1 = l
			low2 = h
		elif(w <= h and h <= l):
			low1 = w
			low2 = h
		elif(w <= l and l <= h):
			low1 = w
			low2 = l
		elif(h <= w and w <= l):
			low1 = h
			low2 = w
		elif(h <= l and l <= w):
			low1 = h
			low2 = l

		tWrp += 2*lw + 2*wh + 2*hl + lowest
		tRib += low1+low1+low2+low2+l*w*h


print("{} feet of wrapping".format(tWrp))
print("{} feet of ribbon".format(tRib))
