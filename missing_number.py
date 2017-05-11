def find_missing(a,b):
	a = set(a)
	b = set(b)

	if a == b:
		return 0
	elif (a is None) or (b is None):
		return 0
	else:
		if len(a) > len(b):
			missing = a.difference(b)
		else:
			missing = b.difference(a)

	missing = list(missing)
	missing = "".join(map(str,missing))
	return int(missing)

