__author__ = 'vinodkumar545'

from IPython import embed

"""
find the maximun stock profit from stock prices

profit = selling day - buying day

returns:
	profit
	buy day
	sell day
"""

class Solution:
	def maxProfit(self, nums):

		PROFIT, BUY_DAY, SELL_DAY, i = 0, 0, 0, 0

		if len(nums) <= 1:
			print('Not enough STOCK_PRICES')
			return PROFIT, BUY_DAY, SELL_DAY


		while(i < len(nums) - 1):
			
			for j in range(i + 1, len(nums)):

				# check the differenct between sellday and buy day
				if nums[j] > nums[i]:

					difference = nums[j] - nums[i]

					if difference > PROFIT:
						PROFIT = difference
						BUY_DAY = i
						SELL_DAY = j

			i += 1

		if PROFIT == 0:
			print("No profit available, wait for more days!!")
		else:
			print("Profit: %s%%\nBuy Day: %s\nBuy Value: %s\nSell Day: %s\nSell Value: %s"%(PROFIT, BUY_DAY + 1, nums[BUY_DAY], SELL_DAY + 1, nums[SELL_DAY]))
			return PROFIT, BUY_DAY, SELL_DAY

solution = Solution()

# STOCK_PRICES = [10, 30, 100, 60, 50, 80]
# STOCK_PRICES = []
# STOCK_PRICES = [10]
# STOCK_PRICES = [10, 100]
# STOCK_PRICES = [100, 10]
# STOCK_PRICES = [100, 90, 80, 70, 60]
STOCK_PRICES = [100, 60, 70, 80, 40, 30, 90]

solution.maxProfit(STOCK_PRICES)
