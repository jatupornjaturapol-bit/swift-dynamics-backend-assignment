"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return 'number can not less than 0'

        if number == 0:
            return 'ศูนย์'

        numbers = [
            'ศูนย์',
            'หนึ่ง',
            'สอง',
            'สาม',
            'สี่',
            'ห้า',
            'หก',
            'เจ็ด',
            'แปด',
            'เก้า'
        ]

        units = [
            '',
            'สิบ',
            'ร้อย',
            'พัน',
            'หมื่น',
            'แสน'
        ]

        text_result = ''
        number_str = str(number)
        length = len(number_str)

        for index, char in enumerate(number_str):
            digit = int(char)
            position = length - index - 1

            if digit == 0:
                continue

            if position == 1:
                if digit == 1:
                    text_result += 'สิบ'
                elif digit == 2:
                    text_result += 'ยี่สิบ'
                else:
                    text_result += numbers[digit] + 'สิบ'
            elif position == 0:
                if digit == 1 and length > 1:
                    text_result += 'เอ็ด'
                else:
                    text_result += numbers[digit]
            else:
                text_result += numbers[digit] + units[position]
        return text_result

solution = Solution()

print(solution.number_to_thai(101))
print(solution.number_to_thai(21))
print(solution.number_to_thai(3456))
print(solution.number_to_thai(0))
print(solution.number_to_thai(-1))



        
