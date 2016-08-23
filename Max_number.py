# -*- coding:utf-8 -*-
'''
给定两个列表，列表长度分别为 m 和 n， 列表中元素都是 0-9 的数字，两个列表代表两个整数.　从这两个列表中取数字，来构建一个长度为 k 且数值最大的数字. 来自同一个列表的数字之间的相对顺序需要保持不变.返回一个包含k个数字的列表. 你应该尽量去优化你的时间和空间复杂度.

例子 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

例子 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

例子 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
'''


# class Solution(object):
#     def maxNumber(self, nums1, nums2, k):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#
#         def generate_combinations(nums1, nums2, k):
#             if k == 1:
#                 if nums1 or nums2:
#                     for item in nums1 + nums2:
#                         yield [item]
#             else:
#                 for i, num in enumerate(nums1):
#                     for item in generate_combinations(nums1[i + 1:], nums2, k - 1):
#                         yield [num] + item
#                 for i, num in enumerate(nums2):
#                     for item in generate_combinations(nums1, nums2[i + 1:], k - 1):
#                         yield [num] + item
#
#         _split_list = generate_combinations(nums1, nums2, k)
#         return max(_split_list)
#
#
# s = Solution()
# print(s.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 3))
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []

        if len(nums1 + nums2) <= k:
            print nums1 > nums2
            return nums1 + nums2 if nums1 > nums2 else nums2 + nums1

        tmp_max = max(nums1 + nums2)
        res.append(tmp_max)
        if k == 1:
            return res

        if tmp_max in nums1:
            res.extend(self.maxNumber(nums1[nums1.index(tmp_max) + 1:], nums2, k - 1))
        else:
            res.extend(self.maxNumber(nums1, nums2[nums2.index(tmp_max) + 1:], k - 1))

        return res


s = Solution()
print s.maxNumber([6, 7], [6, 0, 4], 5)
