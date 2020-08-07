'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.solveIt(l1, l2, 0)
        
    def solveIt(self, l1, l2, c):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.solveIt(l1.next,l2.next,c)
        return ret


class unitTest(unittest.TestCase):
    def test_a(self):
        l1_c = ListNode(2, None)
        l1_b = ListNode(4, l1_c)
        l1_a = ListNode(3, l1_b)

        l2_c = ListNode(5, None)
        l2_b = ListNode(6, l2_c)
        l2_a = ListNode(4, l2_b)

        solution = Solution()
        result = solution.addTwoNumbers(l1=l1_a, l2=l2_a)
        print(result)



        l1_b = ListNode(8, None)
        l1_a = ListNode(1, l1_b)

        l2_a = ListNode(0, None)
        

        solution = Solution()
        result = solution.addTwoNumbers(l1=l1_a, l2=l2_a)
        print(result)
    

if __name__=='__main__':
    unittest.main()