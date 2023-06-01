def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    left_day, right_day = 0, 1
    best_profit = 0

    while right_day < len(prices):
        if prices[left_day] < prices[right_day]:
            profit = prices[right_day] - prices[left_day]
            best_profit = max(best_profit, profit)
        else:
            left_day = right_day
        # 這裡原先要left_day += 1 但為了要保持最佳價格所以left > right的時候不動
        right_day += 1
    
    return best_profit
            


prices = [7,1,5,3,6,4]
print(maxProfit(prices))