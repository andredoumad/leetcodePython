# Andre Doumad
# 200823
'''
This problem was asked by Amazon.

In order to improve customer experience, Amazon has developed a system to provide recommendations to the customers regarding the items they can purchase. Based on a historical customer purchase information, an item association can be defined as - if an item A is ordered by a customer, then item B is also likely to be ordered by the same customer. (e.g. Book1 is frequently ordered with Book2.). All items that are linked together by an item association can be considered to be in the same group. An item without any association to any other item can be considered to be its own item association with a group size of 1. 

given a list of item association relationships (i.e., group of items likely to be ordered together), write an algorithm that outputs the largest item association group. If the two groups have the same number of items then select the group which contains the item that appears first in lexicographic order.

Input:
The input to to the function/method consists of an argument- 
itemAssociation, a list containing pairs of strings representing the items that are ordered together.

Output:
Return a list of strings representing the largest item association group, sorted lexicographically.

EXAMPLE:
Input:
itemAssociation:
[[Item1, Item2],
 [Item3, Item4],
 [Item4, Item5]]

Output:
[Item3, Item4, Item5]

Explanation:
There are two item association groups:
group1: [Item1, Item2]
group2: [Item3, Item4, Item5]
In the available item associations, group2 has the largest association.
So, the output is [Item3, Item4, Item5].

Helper Description:
The following class is used to represent a pair of strings and is already implemented in the default code( no need to write this definition again in your code.)

class PairString():
    def __init__(self, first, second):
        self.first = first
        self.second = second

'''


class PairString():
    def __init__(self, first, second):
        self.first = first
        self.second = second

class Solution():
    def largestItemAssociation(self, itemAssociation):
        # programming-funzone.
        pass


s = Solution()
print(s.largestItemAssociation([['Item1', 'Item2'], ['Item3', 'Item4'], ['Item4', 'Item5']])) # should print [Item3, Item4, Item5]