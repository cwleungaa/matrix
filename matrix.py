def input_matrix():
	i = int(input('請輸入矩陣的列數: '))
	j = int(input('請輸入矩陣的行數: '))

	real_matrix = []

	for m in range(i):
		sub_matrix = []
		for n in range(j):
			a = input('請輸入矩陣的元素(由上往下輸入): ')
			sub_matrix.append(a)	
		real_matrix.append(sub_matrix)
	print(real_matrix)	

	return real_matrix


def print_matrix(A):
	for i in A:
		for j in i:
			print(j,end = '\t')
		print('\n')

def vaild_matrix(A,B):              #check rowA=rowB ,colA=colB
	if len(A) != len(B):
		print('兩個MATRIX不可以相加!!!!!')
		quit()
	elif len(A[0]) != len(B[0]):
		print('兩個MATRIX不可以相加!!!!!')
		quit()		
	else:
		print('兩個MATRIX可以相加')

def add_matrix(A,B):
	result_matrix = []

	for i in range(len(A)):
		sub_matrix2 = []
		for j in range(len(A[0])):
			a = int(A[i][j])+int(B[i][j])
			sub_matrix2.append(a)
		
		result_matrix.append(sub_matrix2)

	print(result_matrix)		

	return result_matrix


def main():
	A = input_matrix()
	B = input_matrix()
	print_matrix(A)
	print('----------------')
	print_matrix(B)
	vaild_matrix(A,B)
	C = add_matrix(A,B)
	print_matrix(C)


main()
