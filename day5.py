#!/usr/bin/env python
import os
import re

f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
content = f.read()
f.close()

PATTERN1 = ".*([aeiou].*){3}.*"
PATTERN2 = ".*(?P<l>[a-z])(?P=l).*"
PATTERN3 = ".*(ab).*"
PATTERN4 = ".*(cd).*"
PATTERN5 = ".*(pq).*"
PATTERN6 = ".*(xy).*"

PATTERN7 = ".*(?P<w>[a-z]{2}).*(?P=w).*"
PATTERN8 = ".*(?P<l>[a-z]).(?P=l).*"

rp1 = re.compile(PATTERN1)
rp2 = re.compile(PATTERN2)
rp3 = re.compile(PATTERN3)
rp4 = re.compile(PATTERN4)
rp5 = re.compile(PATTERN5)
rp6 = re.compile(PATTERN6)

rp7 = re.compile(PATTERN7)
rp8 = re.compile(PATTERN8)

t1 = 0
t2 = 0

for c in content.split('\n'):
	if(rp1.match(c) and rp2.match(c) and not rp3.match(c) and not rp4.match(c) and not rp5.match(c) and not rp6.match(c)):
		t1 += 1

	if(rp8.match(c) and rp7.match(c)):
		t2 += 1

print("{} nice strings #1".format(t1))
print("{} nice strings #2".format(t2))
