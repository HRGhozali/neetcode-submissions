class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        retArr = [0] * (2 * length)
        for i in range(len(nums)):
            retArr[i] = nums[i]
            retArr[i+len(nums)]=nums[i]
        return retArr