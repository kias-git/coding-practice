'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        last_sequence = "1"
        for sequence_number in range(1, n):
            next_sequence = ""
            current_char = None
            current_char_count = 0
            for char in last_sequence:
                if current_char == char:
                    current_char_count += 1
                    continue
                if current_char and current_char != char:
                    next_sequence += str(current_char_count) + current_char
                current_char = char
                current_char_count = 1
            last_sequence = next_sequence + str(current_char_count) + current_char
        return last_sequence
