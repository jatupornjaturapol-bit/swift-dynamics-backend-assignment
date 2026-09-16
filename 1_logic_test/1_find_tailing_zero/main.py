"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative

Ex
7! = 504 0 == 1
\(n! = n \times (n - 1) \times (n - 2) \times \dots \times 1\)สำหรับค่าของ 0! ถูกกำหนดให้เท่ากับ 1 เสมอ [1]
-10! = 10! * -1
"""



class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        value = number 
        if(value < 0):
            value = value * -1

        result = 1
        for i in range(1, value + 1):
            result *= i

        count = 0

        print('factorial',result)

        while result % 10 == 0:
            count += 1
            result //= 10

        return count

solution = Solution()

print(solution.find_tailing_zeroes(0))
print(solution.find_tailing_zeroes(7))
print(solution.find_tailing_zeroes(-10))
