import os

f = open('input/{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]),'r')
content = f.read()
f.close()

t = 1
vh = [(0,0)]

sx = 0
sy = 0

rx = 0
ry = 0

st = True

for c in content:
	if(c == 'v'): #move south
		if(st):
			sy += 1
		else:
			ry += 1
	elif(c == '^'): #move north
		if(st):
			sy -= 1
		else:
			ry -= 1
	elif(c == '<'): #move west
		if(st):
			sx -= 1
		else:
			rx -= 1
	elif(c == '>'): #move east
		if(st):
			sx += 1
		else:
			rx += 1

	x,y = (sx,sy)
	if(not st):
		x,y = (rx,ry)
		
	if((x,y) not in vh):
		vh.append((x,y))
		t += 1

	st = not st

print("{} houses".format(t))
