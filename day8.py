import os

f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
content = f.read()
f.close()

tc = 0
ts = 0
tn = 0

for c in content.split('\n'):
	tc += len(c)
	ts += len(eval(c))
	c = c.replace('\\','\\\\')
	c = c.replace('"','\\"')
	c = '"' + c + '"'
	tn += len(c)

print("First part {}".format(tc - ts))
print("Second part {}".format(tn - tc))