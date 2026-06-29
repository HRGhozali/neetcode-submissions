class Solution:
    def search(self, nums: List[int], target: int) -> int:
        top = len(nums) - 1
        bot = 0
        while (bot <= top):
            mid = (top - bot) // 2 + bot
            if nums[mid] == target: return mid
            elif nums[mid] < target: bot = mid + 1
            else: top = mid - 1
        return -1