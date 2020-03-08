__author__ = 'vinodkumar545'

from random import randint

class Solution:
	def getColumnName(self, num):

		div, rem = divmod(num, 26)
		# print(div, rem)

		string = ''

		if rem == 0:
			string = 'Z'

			while(div > 25):
				d, r = divmod(div, 26)
				if r == 0:
					string = "Z" + string
				else:
					string = chr(96 + r).upper() + string
				div = d
		else:
			string = chr(96 + rem).upper()

			while(div > 0):
				d, r = divmod(div, 26)
				string = chr(96 + r).upper() + string

				div = d

		print("Number: %s"%(num))
		print("Column: %s"%(string))

solution = Solution()
num = randint(1, 10000)

solution.getColumnName(num)

