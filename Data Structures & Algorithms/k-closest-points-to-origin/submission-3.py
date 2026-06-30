import numpy as np
import heapq
class Solution:
    def distance(self, point: List[int]) -> int:
        return np.sqrt((point[0] - 0)**2+(point[1] - 0)**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = -self.distance(point)
            heapq.heappush(heap, [dist, point])
            if len(heap) > k: 
                heapq.heappop(heap)
        return [point[1] for point in heap]