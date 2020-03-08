from IPython import embed
# value = "(a + b) * (c + d)"
# value = "((a + b) * ab) + (a + b)"
# value = '3) + (5j'
# value = "(((a + b )"
# value = "((((()"
# value = "))(("
value = "((a + b)"
i = 0
used_index = []
opened, closed, match = 0, 0, 0
while(i < len(value)):
	if value[i] == ")":
		closed += 1
	if value[i] == '(':
		opened += 1
		increament = 0
		for j in range(i + 1, len(value)):
			if value[j] == '(':
				increament += 1
			if value[j] == ')' and increament != 0:
				increament -= 1
			if value[j] == ')' and increament == 0 and j not in used_index:
				match += 2
				used_index.append(j)
				print("one closed expression found")
				break
	if value[i] == ")" and i not in used_index:
		if opened == 0:
			closed += 1
			print("False")
	# print(opened, closed)
	i += 1
print(opened, closed)
if match == (opened + closed) and opened == closed:
	print('True')
else:
	print('False')
