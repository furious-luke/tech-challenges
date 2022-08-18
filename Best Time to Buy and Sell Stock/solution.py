from functools import reduce
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return reduce(max_profit_reducer, reversed(prices), (0, 0))[0]


def max_profit_reducer(maxes, cur_price):
    max_profit, max_price = maxes
    return (
        max(max_profit, max_price - cur_price),
        max(max_price, cur_price),
    )


if __name__ == '__main__':
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ]
    for prices, result in test_cases:
        assert Solution().maxProfit(prices) == result
