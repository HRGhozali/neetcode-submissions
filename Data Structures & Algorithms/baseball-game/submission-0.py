class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for ops in operations:
            match ops:
                case '+':
                    past = stack[-1] + stack[-2]
                    stack.append(past)
                    sum += past
                case 'D':
                    double = stack[-1] * 2
                    stack.append(double)
                    sum += double
                case 'C':
                    sum -= stack[-1]
                    stack.pop()
                case _:
                    sum += int(ops)
                    stack.append(int(ops))
        return sum