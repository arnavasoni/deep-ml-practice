# Transpose Matrix
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	'''
	Example:
	2 rows, 3 columns;
	convert to 3 rows, 2 columns.
	
	'''
	
	'''
	For the return statement:
     *a is used to access all of the elements from a data structure,
	for a function to apply to them
	or each of them being used as arbitrary 
	number of parameters
     '''
	return [list(col) for col in zip(*a)]

# Sample use case
a = [[1,2,3],[4,5,6]]
print(transpose_matrix(a))