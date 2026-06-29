class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDict = {}
        for index, num in enumerate(nums):
            comp = target - num
            if comp in seenDict: return [seenDict[comp], index]
            seenDict[num] = index
        return []