
ip = "1321131112"

for _ in xrange(50):
	t = ""
	x = [-1,1]
	for i in ip:
		i = int(i)

		if(x[0] == -1):
			x[0] = i
		else:
			if(x[0] == i):
				x[1] += 1
			else:
				t += "{}{}".format(x[1],x[0])
				x[0] = i
				x[1] = 1

	if(x[0] == -1):
		x[1] += 1
	else:
		t += "{}{}".format(x[1],x[0])
		x[0] = -1
		x[1] = 1
	
	ip = t
	if(_ == 39):
		print(len(t))

print(len(t))
