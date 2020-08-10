# Andre Doumad
'''
Say you have an array for which the ith element is 
the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), design an 
algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0

Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
import unittest, time, heapq

class Solution:
    def maxProfit(self, prices):
        # heapq solution - O(n) time - 
        # heap[0] will be the lowest price
        priceHeap=[]
        maxprofit=0
        for price in prices:
            if not priceHeap:
                heapq.heappush(priceHeap,price)
            elif price-priceHeap[0]>maxprofit:
                maxprofit= price-priceHeap[0]
            heapq.heappush(priceHeap,price)
        return maxprofit

        #Runtime: 52 ms, faster than 99.45% of Python3 online submissions for Best Time to Buy and Sell Stock.
        #Memory Usage: 15.1 MB, less than 56.32% of Python3 online submissions for Best Time to Buy and Sell Stock.

class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        result = solution.maxProfit([7,1,5,3,6,4])
        print('result ', result)
        self.assertEqual(result, 5, '')

        result = solution.maxProfit([7,6,4,3,1])
        print('result ', result)
        self.assertEqual(result, 0, '')

        result = solution.maxProfit([2,4,1])
        print('result ', result)
        self.assertEqual(result, 2, '')

if __name__ == '__main__':
    unittest.main()