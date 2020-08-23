# Andre Doumad
# 200821
'''
Amazon Fresh is running a promotion in which customers receive prizes for purchasing a secret combination of fruits. The combination will change each day, and the team running the promotion wants to use a code list to make it easy to change the combination. The code list contains groups of fruits. Both the order of the groups within the code list and the order of the fruits within the groups matter. However, between the groups of fruits, any number, and type of fruit is allowable. The term "anything" is used to allow for any type of fruit to appear in that location within the group.
Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
Based on the above secret code list, a customer who made either of the following purchases would win the prize:
orange, apple, apple, banana, orange, banana
apple, apple, orange, orange, banana, apple, banana, banana
Write an algorithm to output 1 if the customer is a winner else output 0.

Input
The input to the function/method consists of two arguments:
codeList, a list of lists of strings representing the order and grouping of specific fruits that must be purchased in order to win the prize for the day.
shoppingCart, a list of strings representing the order in which a customer purchases fruit.
Output
Return an integer 1 if the customer is a winner else return 0.
Note
'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group. 'anything' has to be something, it cannot be "nothing."
'anything' must represent one and only one fruit.
If secret code list is empty then it is assumed that the customer is a winner.

Example 1:

Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [orange, apple, apple, banana, orange, banana]
Output: 1
Explanation:
codeList contains two groups - [apple, apple] and [banana, anything, banana].
The second group contains 'anything' so any fruit can be ordered in place of 'anything' in the shoppingCart. The customer is a winner as the customer has added fruits in the order of fruits in the groups and the order of groups in the codeList is also maintained in the shoppingCart.

Example 2:

Input: codeList = [[apple, apple], [banana, anything, banana]]
shoppingCart = [banana, orange, banana, apple, apple]
Output: 0
Explanation:
The customer is not a winner as the customer has added the fruits in order of groups but group [banana, orange, banana] is not following the group [apple, apple] in the codeList.

Example 3:

Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [apple, banana, apple, banana, orange, banana]
Output: 0
Explanation:
The customer is not a winner as the customer has added the fruits in an order which is not following the order of fruit names in the first group.

Example 4:

Input: codeList = [[apple, apple], [apple, apple, banana]] shoppingCart = [apple, apple, apple, banana]
Output: 0
Explanation:
The customer is not a winner as the first 2 fruits form group 1, all three fruits would form group 2, but can't because it would contain all fruits of group 1.

'''



class Solution():
    def solve(self, codeList, shoppingCart):
        codeDic, cartDic = {}, {}

        for i in range(0, len(codeList)):
            codeDic[i] = codeList[i]

        for i in range(0, len(shoppingCart)):
            cartDic[i] = shoppingCart[i]

        for k,v in codeDic.items():
            print('code k ', k, ' v ', v)

        for k,v in cartDic.items():
            print('cart k ', k, ' v ', v)

        hits = 0
        for k,v in codeDic.items():
            print('checking for code k ', k, ' v ', v)
            i = 0
            match = []
            for item in shoppingCart:
                print('item ', item)
                if i < len(v) and str(item) == str(v[i]) or i < len(v) and  str(v[i]) == 'anything':
                    print('v[i] ', v[i])
                    match.append(True)
                    i += 1

            print('match ', match)
            if len(match) == len(v):
                hits += 1

        print('hits = ', hits)
        if hits == len(codeList):
            return 1
        else:
            return 0

s = Solution()
print(s.solve([['apple', 'apple'], ['banana', 'anything', 'banana']], ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']))