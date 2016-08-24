# -*- coding:utf-8 -*-
'''
给定不同面值的若干种硬币以及一个总金额 amount.写一个函数来计算为了凑够这个总金额，最少你需要几枚硬币. 如果无解，则返回 -1.

例子 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

例子 2:
coins = [2], amount = 3
return -1.

注意:
你可以假设每种硬币你有无限多个。
'''


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 如果amout大于最大数的整数倍，那次数就越少
        count = 0
        if not coins or amount == 0:
            return -1
        while amount:
            max_value = max(coins)
            if max(coins) <= amount:
                count += amount // max(coins)
                amount = amount % max(coins)
                print count, amount
                coins.remove(max(coins))
                if not coins and amount != 0:
                    return -1
                if coins:
                    if amount < min(coins):
                        amount += max_value
                        count -= 1
            else:
                coins.remove(max(coins))
                if not coins and amount != 0:
                    return -1
        return count


nums = [1, 2, 5]
s = Solution()
print s.coinChange(nums, 11)
