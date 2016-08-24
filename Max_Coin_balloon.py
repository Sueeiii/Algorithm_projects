# -*- coding:utf-8 -*-
'''
给定 n 个气球, 序号是0 到 n-1. 每一个气球上面会被涂上一个数字，这些数字放在列表 nums里. 你被要求戳破气球. 如果你戳破气球 i 你将得到nums[左边] * nums[i] * nums[右边] 个金币. 其中左边 和 右边 是挨着 i的两个气球. 戳破之后, 左边 和 右边就相邻了。

找到你能通过这个游戏获取到的最大金币数。

注意:
(1)你可以认为 nums[-1] = nums[n] = 1. 它们并不真实存在，所以你无法戳破它们.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

例子:

给定 [3, 1, 5, 8]

返回 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_value = 0
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return nums[0] * nums[1] + max(nums)
        while len(nums) > 2:
            # 取中间的最小值来计算金币
            min_value = min(nums[1:len(nums) - 1])
            min_index = nums.index(min_value)
            left = nums[min_index - 1] if min_index > 0 else 1
            right = nums[min_index + 1] if min_index < len(nums) - 1 else 1
            sum_value = sum_value + left * nums.pop(min_index) * right
        return sum_value + nums[0] * nums[1] + max(nums)


l = [4, 5, 3, 2, 7]
s = Solution()
print s.maxCoins(l)
# [3, 8, 11, 5, 4]有问题
