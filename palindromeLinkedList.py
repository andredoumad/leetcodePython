# Andre Doumad
# TODO: Could you do it in O(n) time and O(1) space?

'''
This question was asked by Amazon.

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        if head == None:
            return True
        l1 = []
        l2 = []
        t = head
        
        while True:
            l1.append(t.val)
            t = t.next
            if t == None:
                break

        prev = None
        curr = head
        nex = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nex
            if nex:
                nex = nex.next
        head = prev
        t = head
        while True:
            l2.append(t.val)
            t = t.next
            if t == None:
                break
        
        if l1 == l2:
            return True
        else:
            return False

solution = Solution()

l = ListNode(1,ListNode(2))
result = solution.isPalindrome(l)
print('result ', result)


l = ListNode(1,ListNode(2,ListNode(2,ListNode(1))))
result = solution.isPalindrome(l)
print('result ', result)

'''
output:
result  False
result  True
'''