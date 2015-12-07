import os
import re

f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
content = f.read()
f.close()

PATTERN = "^(((?P<fa>([a-z]{1,2})|\d) (?P<a>AND) (?P<ga>[a-z]{1,2}))|((?P<fo>[a-z]{1,2}) (?P<o>OR) (?P<go>[a-z]{1,2}))|((?P<fl>[a-z]{1,2}) (?P<l>LSHIFT) (?P<gl>\d+))|((?P<fr>[a-z]{1,2}) (?P<r>RSHIFT) (?P<gr>\d+))|(?P<c>(\d+)|([a-z]+))|((?P<n>NOT) (?P<fn>[a-z]{1,2}))) -> (?P<t>[a-z]+)$"

r = re.compile(PATTERN)

def f1(kv={}):
	ld = []

	while True:
		nd = False
		rs = False
		for c in content.split('\n'):
			m = r.match(c)
			if(m and not c in ld):
				if(m.group('c')):
					if(m.group('c').isdigit() or m.group('c') in kv.keys()):
						if(m.group('c').isdigit()):
							v = int(m.group('c'))
						else:
							v = kv[m.group('c')]

						kv[m.group('t')] = v
						ld.append(c)
						rs = True
				elif(m.group('a')):
					if((m.group('fa') == "1" or m.group('fa') in kv.keys()) and m.group('ga') in kv.keys()):
						if(m.group('fa') == "1"):
							v = 1
						else:
							v = kv[m.group('fa')]

						kv[m.group('t')] = v & kv[m.group('ga')]
						ld.append(c)
						rs = True
				elif(m.group('o')):
					if(m.group('fo') in kv.keys() and m.group('go') in kv.keys()):
						kv[m.group('t')] = kv[m.group('fo')] | kv[m.group('go')]
						ld.append(c)
						rs = True
				elif(m.group('l')):
					if(m.group('fl') in kv.keys()):
						kv[m.group('t')] = kv[m.group('fl')] << int(m.group('gl'))
						ld.append(c)
						rs = True
				elif(m.group('r')):
					if(m.group('fr') in kv.keys()):
						kv[m.group('t')] = kv[m.group('fr')] >> int(m.group('gr'))
						ld.append(c)
						rs = True
				elif(m.group('n')):
					if(m.group('fn') in kv.keys()):
						kv[m.group('t')] = ~kv[m.group('fn')] + 2**16
						ld.append(c)
						rs = True
			if(rs):
				nd = True
				break
		if(not nd):
			break

	return kv['a']

a = f1()
print(a)
print(f1({'b':a}))
