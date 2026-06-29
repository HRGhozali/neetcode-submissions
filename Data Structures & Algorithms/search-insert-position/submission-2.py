class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        top = len(nums)-1
        bot = 0
        mid = -1
        while (bot <= top):
            mid = (top - bot) // 2 + bot
            if (nums[mid] == target): return mid
            elif nums[mid] > target: 
                top = mid - 1
            else: 
                bot = mid + 1
        return bot
        