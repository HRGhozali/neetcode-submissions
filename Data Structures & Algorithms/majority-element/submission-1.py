class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqHash = {}
        maxFreq = -1
        maxVal = -10000000000
        for i in nums:
            freqHash[i] = freqHash.get(i, 0) + 1
            if freqHash[i] > maxFreq:
                maxFreq = freqHash[i]
                maxVal = i
        return maxVal