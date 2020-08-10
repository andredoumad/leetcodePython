# Andre Doumad
'''
This Problem was asked by Amazon.

Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def printList(self, node):
        n = node
        while n:
            print(n.val)
            if n.next != None:
                n = n.next
            else:
                break

    def add(self, val):
        if self.head == None:
            self.head = ListNode(val, None)
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = ListNode(val, None)

    def mergeTwoLists(self, l1, l2):
        if l1 == None and l2 == None:
            return self.head

        # # print list
        # print('--------------')
        # if self.head != None:
        #     print('=== head ===')
        #     self.printList(self.head)
        #     print('=== l1 ===')
        #     self.printList(l1)
        #     print('=== l2 ===')
        #     self.printList(l2)
        # else:
        #     print('=== l1 ===')
        #     self.printList(l1)
        #     print('=== l2 ===')
        #     self.printList(l2)

        if l1 != None and l2 != None:
            if l1.val <= l2.val:
                # print('adding l1.val')
                self.add(l1.val)
                return self.mergeTwoLists(l1.next,l2)
            else:
                # print('adding l2.val')
                self.add(l2.val)
                return self.mergeTwoLists(l1,l2.next)
        elif l1 == None and l2 != None:
            self.add(l2.val)
            return self.mergeTwoLists(l1,l2.next)
        elif l2 == None and l1 != None:
            self.add(l1.val)
            return self.mergeTwoLists(l1.next,l2)

class UnitTest(unittest.TestCase):

    def test_a(self):
        solution = Solution()
        l1 = ListNode(1, None)
        l1.next = ListNode(2, None)
        l1.next.next = ListNode(4, None)

        l2 = ListNode(1, None)
        l2.next = ListNode(3, None)
        l2.next.next = ListNode(4, None)

        result = solution.mergeTwoLists(l1, l2)
        print('result: ', result)

if __name__=='__main__':
    unittest.main()

'''
OUTPUT:
--------------
=== l1 ===
1
2
4
=== l2 ===
1
3
4
adding l1.val
--------------
=== head ===
1
=== l1 ===
2
4
=== l2 ===
1
3
4
adding l2.val
--------------
=== head ===
1
1
=== l1 ===
2
4
=== l2 ===
3
4
adding l1.val
--------------
=== head ===
1
1
2
=== l1 ===
4
=== l2 ===
3
4
adding l2.val
--------------
=== head ===
1
1
2
3
=== l1 ===
4
=== l2 ===
4
adding l1.val
--------------
=== head ===
1
1
2
3
4
=== l1 ===
=== l2 ===
4
spliced result is: 
1
1
2
3
4
4
result:  <__main__.ListNode object at 0x7f08660bbc40>
'''