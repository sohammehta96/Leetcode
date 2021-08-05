"""
Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the maximum number of water bottles you can drink.

"""
def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    drink = numBottles
    empty = 0
    for i in range(10):
        numBottles, empty = (numBottles+empty)//numExchange, (numBottles+empty)%numExchange
        drink += numBottles        
    return drink