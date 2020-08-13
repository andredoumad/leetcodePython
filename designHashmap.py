# Andre Doumad
'''
This problem was asked by Amazon.

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
'''
class hashEntry(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

'''
Runtime: 456 ms, faster than 25.90% of Python3 online submissions for Design HashMap.
Memory Usage: 17.6 MB, less than 29.24% of Python3 online submissions for Design HashMap.
'''
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 32
        self.data = [-1]*self.size

    def doubleSize(self):
        print('doubleSize')
        temp = self.data
        self.size *= 2
        while len(self.data)<self.size+16:
            self.data.append(-1)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        while key >= len(self.data):
            self.doubleSize()
        print('self.data ', self.data)
        self.data[key] = hashEntry(key, value)


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        while key >= len(self.data):
            self.doubleSize()
        if self.data[key] == -1:
            return -1
        else:
            return self.data[key].value


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        while key >= len(self.data):
            self.doubleSize()
        self.data[key] = -1


import unittest

class UnitTest(unittest.TestCase):
    def test_a(self):
        hashMap = MyHashMap()
        hashMap.put(1, 1)
        hashMap.put(2, 2)
        result = hashMap.get(1)
        self.assertEqual(result, 1)
        result = hashMap.get(3)
        self.assertEqual(result,-1)
        hashMap.put(2, 1);
        result = hashMap.get(2) 
        self.assertEqual(result,1)
        hashMap.remove(2)
        result = hashMap.get(2) 
        self.assertEqual(result,-1)

if __name__=='__main__':
    unittest.main()

'''
output:
doubleSize
self.data  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
self.data  [-1, <__main__.hashEntry object at 0x7fa7330f9580>, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
self.data  [-1, <__main__.hashEntry object at 0x7fa7330f9580>, <__main__.hashEntry object at 0x7fa7330f9b80>, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''