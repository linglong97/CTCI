def isUnique(s):
	return len(set(s)) == len(s)

from collections import defaultdict
import math
def isPermutation(s1,s2):
	dict1 = defaultdict(int)
	dict2 = defaultdict(int)
	for s in s1:
		dict1[s] += 1
	for s in s2:
		dict2[s] += 1
	for key in dict1:
		if key not in dict2 or dict1[key] != dict2[key]:
			return False
	for key in dict2:
		if key not in dict1:
			return False
	return True

def palindromePermutation(s1):
	dict = defaultdict(int)
	oddcounter = 0
	for s in s1:
		dict[s] += 1

	for key in dict:
		if dict[key] != " ":
			if dict[key] % 2 == 1:
				oddcounter += 1
	return oddcounter > 1

# skipped urlify because that's code monkey stuff

def oneAway(s1,s2):
	m = len(s1)
	n = len(s2)
	if abs(m-n) > 1:
		return False
	different = False
	i, j = 0,0
	if m == n:
		while i< m and j <n:
			if s1[i] != s2[j]:
				if different == True:
					return False
				else:
					different = True
			i += 1
			j += 1
	if m > n:
		while i< m and j < n:
			if s1[i] != s2[j]:
				if different == True:
					return False
				else:
					different = True
					i += 1
			i += 1
			j += 1
	#TODO: implement n < m, same logic
	return True

def stringCompression(s):
	if not s:
		return
	currlen = 1
	currchar = s[0]
	ans = ""
	for i in range(1,len(s)):
		if i == len(s)-1:
			if s[i] == currchar:
				currlen += 1
				ans += currchar+str(currlen)
			else:
				ans += currchar+str(currlen)
		elif s[i] == currchar:
			currlen += 1
		else:
			ans += currchar+str(currlen)
			currlen = 1
			currchar = s[i]
	
	if len(ans) > len(s):
		return s
	else:
		return ans

def rotate_matrix(matrix):
	matrix = list(reversed(matrix))

	for i in range(len(matrix)):
		for j in range(i, len(matrix)):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	return matrix

print rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])

def zero_matrix(matrix):
	rowzero = False
	colzero = False
	for el in matrix[0]:
		if el == 0:
			rowzero = True
			break
	for row in matrix:
		if row[0] == 0:
			colzero = True
			break
	for i in range(1, len(matrix)):
		for j in range(1, len(matrix[0])):
			if matrix[i][j] == 0:
				matrix[0][j] = 0
				matrix[i][0] = 0
	for i in range(len(matrix[0])):
		if matrix[0][i] == 0:
			for k in range(1, len(matrix)):
				matrix[k][i] = 0
	for i in range(len(matrix)):
		if matrix[i][0] == 0:
			for k in range(1, len(matrix)):
				matrix[i][k] == 0
	if rowzero:
		for i in range(len(matrix[0])):
			matrix[0][i] = 0
	if colzero:
		for i in range(len(matrix)):
			matrix[i][0] = 0
	return matrix

def string_rotation(s1, s2):
	return s2 in (s1+s1)

print string_rotation('waterbottle', 'erbottlewats')









