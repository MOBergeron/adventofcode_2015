import md5

ms = "bgvyzdsv"

fz = False
sz = False

i = 1
while True:
	th = "{}{}".format(ms,i)
	h = md5.new(th).hexdigest()

	if(not fz and h.startswith('00000')):
		fz = True
		print("With 5 zeroes : {}".format(i))
		print("With 5 zeroes : {}".format(h))

	if(not sz and h.startswith('000000')):
		sz = True
		print("With 6 zeroes : {}".format(i))
		print("With 6 zeroes : {}".format(h))

	if(fz and sz):
		break

	i += 1