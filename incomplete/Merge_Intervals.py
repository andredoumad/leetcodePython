# Andre Doumad
# 200820
'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
import unittest

class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x: x[0])
        merged = []
        for a in intervals:
            if not merged or merged[-1][-1] < a[0]:

                merged.append(a)
                print('merged[-1][-1] ', merged[-1][-1])
            else:
                merged[-1][-1] = max(merged[-1][-1], a[-1])

            print('a[-1]', a[-1])
        return merged



class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
        print(solution.merge([[1,4],[4,5]]))

if __name__ == '__main__':
    unittest.main()