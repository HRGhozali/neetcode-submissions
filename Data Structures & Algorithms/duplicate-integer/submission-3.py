class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenDict = {}
        for i in nums:
            if i in seenDict: return True
            seenDict[i] = True
        return False