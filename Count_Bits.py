'''
给定一个非负整数num. 对于每一个在范围0 ≤ i ≤ num的数字 i ，计算其二进制表达式中１的个数，并作为一个数组返回。

例子: 假设 num = 5 你应该返回 [0,1,1,2,1,2]（分别是０\１＼２＼３＼４＼５二进制表达式中１的个数）.

进阶:

很容易就能想出一个复杂度在O(n*sizeof(integer))的算法. 但是你能做出一个复杂度接近于线性 O(n) 的算法么？
空间复杂度应该是 O(n).
您能在不使用内置函数的情况下完成本题么？
你应该利用已经计算出来的结果.
在范围 [2-3], [4-7], [8-15] 里做除法等等. 并且用旧的结果生成新的结果。
在计算二进制表达式里有多少个１时，该数字的奇偶状态是否会有些帮助？
'''


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # l = list([0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2])
        # if num <= 10:
        #     return l[:num + 1]
        # else:
        #     for i in range(11, num + 1):
        #         if i % 2 == 0:
        #             l.append(l[i // 2])
        #         else:
        #             l.append(l[i // 2] + 1)
        #             print(i // 2)
        #     return l
        count = [1 for _ in range(num + 1)]
        count[0] = 0
        cur = 2
        cur2 = 2
        while cur <= num:
            if cur == cur2:
                cur2 = cur2 << 1
            else:
                count[cur] = count[cur2 >> 1] + count[cur - (cur2 >> 1)]
            cur = cur + 1
        return count


solution = Solution()
print(solution.countBits(16))
