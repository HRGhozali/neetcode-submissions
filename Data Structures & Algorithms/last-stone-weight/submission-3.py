import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        i = 0
        while len(stones) > 1:
            stoneChoice = heapq.nlargest(2, stones)
            heapq.heappop_max(stones)
            heapq.heappop_max(stones)
            if stoneChoice[0] != stoneChoice[1]: 
                heapq.heappush_max(stones, abs(stoneChoice[0] - stoneChoice[1]))
                i += 1
        if len(stones) == 0: return 0
        else: return stones[0]