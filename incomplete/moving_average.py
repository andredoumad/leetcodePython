# Andre Doumad
# 200908
'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''

'''
Solution: 
Use a list to store the numbers used to calculate sum, and two variables to record the sum and times the next() method gets called. Every time when next() method gets called, append the value to the list and add it to sum. If length of the list is less than given size, return sum / n (n is the times next() method gets called). If times the next() method gets called have been over the given size, then minus first value in the list from sum and remove it from the list, and return sum / size.
'''
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        :type size: int
        """
        self._size = size
        self._array = []
        self._sum = 0

    def next(self, val: int) -> float:
        """
        :type val: int
        :rtype: float
        """
        self._sum += val
        self._array.append(val)
        if len(self._array) > self._size:
            self._sum -= self._array.pop(0)
        return self._sum / len(self._array)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)