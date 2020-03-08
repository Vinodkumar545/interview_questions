# from IPython import embed

## stock prices for the company

# STOCK_PRICES = [10, 30, 100, 60, 50, 80]
# STOCK_PRICES = []
# STOCK_PRICES = [10]
# STOCK_PRICES = [100, 90, 80, 70, 60]
STOCK_PRICES = [100, 60, 70, 80, 40, 30, 90]


PROFIT, BUY_DAY, SELL_DAY, i = 0, 0, 0, 0

while(i < len(STOCK_PRICES) - 1):
	
	for j in range(i + 1, len(STOCK_PRICES)):

		# check the differenct between sellday and buy day
		if STOCK_PRICES[j] > STOCK_PRICES[i]:

			difference = STOCK_PRICES[j] - STOCK_PRICES[i]

			if difference > PROFIT:
				PROFIT = difference
				BUY_DAY = i
				SELL_DAY = j

	
	i += 1

print(PROFIT, BUY_DAY, SELL_DAY)
# return PROFIT, BUY_DAY, SELL_DAY
