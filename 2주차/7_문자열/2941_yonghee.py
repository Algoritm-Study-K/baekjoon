alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str = input()
for c in alphabets:
	str = str.replace(c, ' ')
print(len(str))