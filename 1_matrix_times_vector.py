# Matrix times Vector

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	# 1.
	if len(a[0]) != len(b):
		return -1
	# 2.
	else:
		result = []
		# 2a.
		for row in a:
			hold = 0
			# 2b.
			for i in range(len(row)):
				hold += row[i]*b[i]
			# 2c.
			result.append(hold)
	#2d.
	return result

# Sample use case
print(matrix_dot_vector([[1,2,3],[2,4,5],[6,8,9]],[1,2,3]))