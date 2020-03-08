__author__ = 'vinodkumar545'

from IPython import embed

"""
Validate whether the arthemtic parathensis expression is valid or not

return True or False

"""

class Solution:

	def validateExpression(self, value):
		used_index, i = [], 0
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
					print("closed parathensis found first")
			
			# print(opened, closed)
			i += 1
		
		print(opened, closed)
		
		if match == (opened + closed) and opened == closed:
			print('True')
			return True
		
		else:
			print('False')
			return False

solution = Solution()

value = "(a + b) * (c + d)"
# value = "((a + b) * ab) + (a + b)"
# value = '3) + (5j'
# value = "(((a + b )"
# value = "((((()"
# value = "))(("
# value = "((a + b)"

solution.validateExpression(value)

