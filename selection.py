def selection(l):
	# return list
	r = []
	# while l isn't empty
	while l:
		# find minimum value in the list
		m = l[0]
		for f in range(len(l)):
			if l[f] < m:
				m = l[f]
		# pop that value onto return list
		r.append(l.pop(l.index(m)))
	# return value
	return(r)
