"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return 'number can not less than 0'

        if number == 0:
            return 'roman number cannot be 0'

        roman_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        result = []
        num = number

        for value, symbol in roman_map:
            count, num = divmod(num, value)

            result.append(symbol * count)

            if num == 0:
                break

        return ''.join(result)

solution = Solution()

print(solution.number_to_roman(101))
print(solution.number_to_roman(21))
print(solution.number_to_roman(3456))
print(solution.number_to_roman(0))
print(solution.number_to_roman(-1))