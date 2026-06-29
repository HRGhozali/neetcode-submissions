# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        bot = 1
        top = n
        result = guess(bot + (top - bot)//2)
        while (result != 0):
            if result > 0: bot = (bot + (top - bot)//2) + 1
            elif result < 0: top = (bot + (top - bot)//2) - 1
            result = guess(bot + (top - bot)//2)
        return bot + (top - bot)//2