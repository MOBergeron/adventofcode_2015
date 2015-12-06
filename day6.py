import os
import re

f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
content = f.read()
f.close()

PATTERN = "^(?P<a>(turn (on|off))|toggle) (?P<c1>\d{1,3},\d{1,3}) through (?P<c2>\d{1,3},\d{1,3})$"

r = re.compile(PATTERN)

m = [[False for x in range(1000)] for x in range(1000)]

for c in content.split('\n'):
	mh = r.match(c)
	c1 = [int(i) for i in mh.group('c1').split(',')]
	c2 = [int(i)+1 for i in mh.group('c2').split(',')]
	if(mh.group('a') == 'turn on'):
		for x in xrange(c1[0],c2[0]):
			for y in xrange(c1[1],c2[1]):
				m[x][y] = True
	elif(mh.group('a') == 'turn off'):
		for x in xrange(c1[0],c2[0]):
			for y in xrange(c1[1],c2[1]):
				m[x][y] = False
	elif(mh.group('a') == 'toggle'):
		for x in xrange(c1[0],c2[0]):
			for y in xrange(c1[1],c2[1]):
				m[x][y] = not m[x][y]

l = 0
for x in xrange(1000):
	for y in xrange(1000):
		if(m[x][y]):
			l+=1

print("{} lit lights".format(l))

m = [[0 for x in range(1000)] for x in range(1000)]

for c in content.split('\n'):
	mh = r.match(c)
	c1 = [int(i) for i in mh.group('c1').split(',')]
	c2 = [int(i)+1 for i in mh.group('c2').split(',')]
	if(mh.group('a') == 'turn on'):
		for x in xrange(c1[0],c2[0]):
			for y in xrange(c1[1],c2[1]):
				m[x][y] += 1
	elif(mh.group('a') == 'turn off'):
		for x in xrange(c1[0],c2[0]):
			for y in xrange(c1[1],c2[1]):
				m[x][y] -= 1 if not m[x][y] == 0 else 0
	elif(mh.group('a') == 'toggle'):
		for x in xrange(c1[0],c2[0]):
			for y in xrange(c1[1],c2[1]):
				m[x][y] += 2

l = 0
for x in xrange(1000):
	for y in xrange(1000):
		l+=m[x][y]

print("{} brightness".format(l))