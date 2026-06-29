class Solution:
    def recursiveStairs(self, n: int, datBank: List[int]):
        if n <= 1:
            return 1
        
        if datBank[n] != -1: return datBank[n]

        datBank[n] = self.recursiveStairs(n-1, datBank) + self.recursiveStairs(n-2, datBank)

        return datBank[n]
    def climbStairs(self, n: int) -> int:
        datBank = [-1] * (n+1)
        return self.recursiveStairs(n, datBank)