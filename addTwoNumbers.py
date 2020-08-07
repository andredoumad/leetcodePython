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
# import typing
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=''
        b=''
        searching = True
        while searching:
            a+=str(l1.val)
            if l1.next == None:
                searching = False
            l1 = l1.next

        searching = True
        while searching:
            b+=str(l2.val)
            if l2.next == None:
                searching = False
            l2 = l2.next
        # print(a)
        # print(b)
        c = str(int(a) + int(b))
        
        l3 = None
        for i in reversed(range(0, len(c))):
            newNode = ListNode(val=int(c[i]), next=l3)
            l3 = newNode
        
        searching = True
        a = l3
        while searching:
            print(a.val)
            if a.next == None:
                searching = False
            a = a.next

        # print('result:')
        # print(l3.val)
        # print(l3.next.val)
        # print(l3.next.next.val)
        return l3



l1_c = ListNode(2, None)
l1_b = ListNode(4, l1_c)
l1_a = ListNode(3, l1_b)

l2_c = ListNode(5, None)
l2_b = ListNode(6, l2_c)
l2_a = ListNode(4, l2_b)

solution = Solution()
print(solution.addTwoNumbers(l1=l1_a, l2=l2_a))