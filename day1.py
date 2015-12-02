import os

f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
content = f.read()
f.close()

tf = 0
tb = None

i = 1
for c in content:
	if(c == '('):
		tf += 1
	if(c == ')'):
		tf -= 1

	if(tf == -1 and not tb):
		tb = i

	i += 1


print("Floor {}".format(tf))
print("First basement visit {}".format(tb))
