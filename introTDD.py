import unittest, math

def reverseList(list):
    for i in range (0, int(len(list)/2)):
        # print('before for', list)
        list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
        # print('after for', list)
    return list

def isPalindrome(str):
    newstr = ""
    for i in range(len(str)-1, -1, -1):
        newstr += str[i]
        # print('newstr', str[i])
    if str == newstr:
        valid = True
        return valid
    else:
        return False
    return newstr

def amountGiven(money):
    moneyList = []
    quarters = math.floor(money/25)
    change = money - quarters*25
    dimes = math.floor(change/10)
    morechange = change - dimes*10
    fives = math.floor(morechange/5)
    somechange = morechange - fives*5
    pennies = math.floor(somechange / 1)
    moneyList.append(quarters)
    moneyList.append(dimes)
    moneyList.append(fives)
    moneyList.append(pennies)
    print('money: ', moneyList)
    return moneyList

def factorial(num):
    factorialIs = 1
    if num == 0:
        return 1
    else: 
        for i in range (num, 0, -1):
            factorialIs *= i
        return factorialIs

def fibonacci(integer):
    fibList = [0,1]
    if integer < 3:
        return fibList[integer-1]
    else:
        for i in range(3,integer+1):
            newIndex = fibList[i-2] + fibList[i-3]
            fibList.append(newIndex)
        return fibList[integer-1]

class fibonacciTestCases(unittest.TestCase):
    def testUno(self):
        self.assertEqual(fibonacci(3), 1)
    def testTwo(self):
        self.assertTrue(fibonacci(4)==2)
    def testThree(self):
        self.assertFalse(fibonacci(7)==7)
    def testFour(self):
        self.assertEqual(fibonacci(2),1)
# class factorialProduct(unittest.TestCase):
#     def testOne(self):
#         self.assertEqual(factorial(5), 120)
#     def testTwo(self):
#         self.assertFalse(factorial(0) == 0)
#     def testthree(self):
#         self.assertTrue(factorial(5)% 5 == 0)

# class coinsGivenTestCases(unittest.TestCase):
#     def testUno(self):
#         self.assertEqual(amountGiven(92), [3,1,1,2])
#     def testDos(self):
#         self.assertFalse(len(amountGiven(92))==5)
#     def testTres(self):
#         self.assertIn(3,amountGiven(75))
#     def testQuatro(self):
#         self.assertEqual(amountGiven(87), [3,1,0,2])
#     def testCinco(self):
#         self.assertNotIn(0, amountGiven(93))

# class reverseListTestCases(unittest.TestCase):
#     def testOne(self):
#         self.assertEqual(reverseList([3,5,6,7,9]), [9,7,6,5,3])
#     def testTwo(self):
#         self.assertTrue(len([0,2,3,4])==len(reverseList([0,2,3,4])))
#     def testThree(self):
#         self.assertFalse(len(reverseList([9,6,5,3]))==3) 
#     def testFour(self):
#         self.assertIn(5, [3,4,5,6,9])
#     def setUp(self):
#         print("running setup")
#     def tearDown(self):
#         print("tearing down")

# class isPalindromeTestCases(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(isPalindrome("racecar"), True)
#     def test2(self):
#         self.assertFalse(isPalindrome("racebr"))
#     def test3(self):
#         self.assertTrue(isPalindrome("trapapart"))
#     def test4(self):
#         self.assertEqual(isPalindrome("trapapart"), True)
#     def test5(self):
#         self.assertFalse(isPalindrome("orange"))
#     def setUp(self):
#         print("running setup")
#     def tearDown(self):
#         print("tearing down")

if __name__ == "__main__":
    unittest.main()