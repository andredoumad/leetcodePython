# Andre Doumad
'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. 
Could you implement both?
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
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
        return head

solution = Solution()

l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,)))))

result = solution.reverseList(l1)
print('result = ', result)

while result != None:
    print('result val: ', result.val)
    result = result.next

'''
output:
result =  <__main__.ListNode object at 0x7f1fb39b8e50>
result val:  5
result val:  4
result val:  3
result val:  2
result val:  1
'''