import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        kLargest = heapq.nlargest(k, freq.items(), key=lambda k: k[1])
        return [k[0] for k in kLargest]