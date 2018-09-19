stock_prices_list = [10, 7, 5, 8, 11, 9]

# Finding the max difference in a list
def stock_prices(stock_prices_list):
    # Initializing variables
    buy_price = 0
    sell_price = 0
    temp_low_price = stock_prices_list[0]
    temp_high_price = stock_prices_list[0]
    time_index = 0
    max_profit = 0

    # Iterate over the range 0 to length of stock_prices_list to find max_profit
    for time_index in range(len(stock_prices_list)):
        if stock_prices_list[time_index] < temp_low_price:
            temp_low_price = stock_prices_list[time_index]
        else:
            sell_price = stock_prices_list[time_index]

        print("Current BUY: {} SELL: {}".format(buy_price, sell_price))
        max_profit = buy_price - sell_price

    return max_profit



results = stock_prices(stock_prices_list)
print(results)
