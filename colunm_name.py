__author__ = 'vinodkumar545'

from random import randint

"""
Identify the Excel Colunm name from the integer number

return Colunm name

"""

class Solution:
	def getColumnName(self, num):

		string = ''

		if num == 0:
			return string

		else:
			n = num
			while(n > 0):
				div, rem = divmod(n, 26)
				print(n, div, rem)
				
				if rem == 0:
					string = "Z" + string

					if div <= 26: div = div - 1

				else:
					string = chr(96 + rem).upper() + string
					
				n = div

		print("Number: %s"%(num))
		print("Column: %s"%(string))

solution = Solution()
num = randint(1, 9999999)

solution.getColumnName(num)

