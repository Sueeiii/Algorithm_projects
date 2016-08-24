# -*-coding:utf-8-*-
'''
给你一个整数列表 nums ，你需要返回一个新的列表 counts . 列表 counts 有这样的特性， counts[i] 是nums[i]右侧小于它的数字的个数.

例子:

给定 nums = [5, 2, 6, 1]

 5 的右面有 2 个更小的数字 (2 和 1).
 2 的右面有 1 个更小的数字 (1).
 6 的右面有 1 个更小的数字 (1).
１的右面有 0 个更小的数字。
那么需要返回数组 [2, 1, 1, 0].
'''


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = []
        for index, value in enumerate(nums):
            # 用来计数有多少个数字比本身小的数
            # print index, '->', value
            # if index == len(nums) - 1:
            #     counts.append(0)
            count = 0
            i = index
            # print i
            while i < len(nums):
                # 判断是否比后面的数字大，大加一，小不算
                if value > nums[i]:
                    count = count + 1
                    # print count
                i = i + 1
                print i
            counts.append(count)
        return counts


S = Solution()
print S.countSmaller([4, 5, 3, 2, 7])
