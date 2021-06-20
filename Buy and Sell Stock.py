"""
The cost of stock on each day is given in an array A[] of size N. Find
all the days on which you buy and sell the stock so that in between
those days your profit is maximum.
Note: There may be multiple possible solutions. Return any one of
them. Any correct solution will result in a output of 1, whereas
wrong solutions will result in an output of 0.
"""
def buyandsell(prices):
    
    #deciding actions based on consecutive stock prices
    action = []
    
    #for each day of price
    for i in range(len(prices)):
        
        #for last day price
        if i == len(prices) - 1:
            
            #if last day price is greater than second last day price = sell
            if prices[i-1] < prices[i]:
                action.append("sell")
                
            #else buy, but buy is just a placeholder and will not be considered
            else:
                action.append("buy")
                
        #for all other days of prices
        else:
            
            #if price increases tomorrow, buy today
            if prices[i] < prices[i+1]:
                action.append("buy")

            #if price decreases tomorrow, sell today
            else:
                action.append("sell")
    
    #can't sell on first day before buying, neutralizing all initial sells
    for i in range(action.index("buy")):
        action[i] = ""
    
    #selecting the first occurences of "buy" or "sell" from repeated increase or decrease
    buy = []
    sell = []
    
    #if buy on first day
    if action[0] == "buy":
        buy.append(0)
    #checking for buy from 2nd day to last day, and choosing only 1st in a series
    for i in range(1,len(action)):
        if action[i] == "buy":
            if action[i-1] != "buy":
                buy.append(i)
    
    #checking for sell from 2nd day to last day, and choosing only 1st in a series
    for i in range(1,len(action)):
        if action[i] == "sell":
            if action[i-1] != "sell":
                sell.append(i)
    
    #calculating profit using buy-sell pairs
    profit = 0
    
    #profit on each trade is cash received - cash spent for each trade
    for i in range(len(sell)):
        profit = profit + (prices[sell[i]] - prices[buy[i]])
        
    #returning maximum profit
    return profit







#calling the function
import random

prices = []

for i in range(random.randint(10,20)):
    prices.append(random.randint(100,1000))
    
print(buyandsell(prices))