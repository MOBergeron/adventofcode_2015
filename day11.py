import re
from string import ascii_lowercase

h = [x for x in ascii_lowercase]
d = {}
b = {}
for i in xrange(1, len(h)+1):
	d[i] = h[i-1]
	b[h[i-1]] = i

PATTERN = "^.*(?P<q>[a-z])(?P=q).*(?P<p>[a-z])(?P=p).*$"

r = re.compile(PATTERN)

ip = "hxbxwxba"

def f(ip):
	if(b[ip[-1:]] == len(d)):
		ip = f(ip[:-1]) + d[1]
	else:
		ip = ip[:-1] + d[b[ip[-1:]]+1]
	return ip

g = 0
while(True):
	q = -1
	p = 0
	w = False
	if(r.match(ip) and not "i" in ip and not "o" in ip and not "l" in ip):
		for i in ip:
			if(q == -1):
				q = b[i]
			elif(q+1 == b[i]):
				q = b[i]
				p+=1
			else:
				q = b[i]
				p = 0

			if(p == 2):
				w = True
				break

	if(w):
		g += 1
		print(ip)
		if(g == 2):
			break
	
	ip = f(ip)

