'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
class Node():
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self._remove(self.hash[key])
        n = Node(key, value)
        self._add(n)
        self.hash[key] = n
        if len(self.hash) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.hash[n.key]

    def printLRU(self):
        print('-------')
        print('hash')
        for k,v in self.hash.items():
            print('k ', k, ' v ', v.val)
        print('linkedlist')
        temp = self.head
        while temp != None:
            print('value: ', temp.val)
            temp = temp.next

solution = LRUCache(2)
solution.put(1,1)
solution.put(2,2)
solution.put(3,3)
solution.printLRU()
solution.get(2)
solution.printLRU()

'''
output:
-------
hash
k  2  v  2
k  3  v  3
linkedlist
value:  0
value:  2
value:  3
value:  0
-------
hash
k  2  v  2
k  3  v  3
linkedlist
value:  0
value:  3
value:  2
value:  0
'''
