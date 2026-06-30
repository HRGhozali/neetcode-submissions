class Solution:
    def mergeSort(self, arr, l, r):
        if (l < r):
            mid = l + (r - l) // 2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid+1, r)
            self.merge(arr, l, mid, r)

    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        arr1 = [0] * n1
        arr2 = [0] * n2

        for i in range(n1):
            arr1[i] = arr[l+i]
        for i in range(n2):
            arr2[i] = arr[m+i+1]
        
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                arr[k] = arr1[i]
                k += 1
                i += 1
            else:
                arr[k] = arr2[j]
                k += 1
                j += 1
        while i < n1:
            arr[k] = arr1[i]
            k += 1
            i += 1
        while j < n2:
            arr[k] = arr2[j]
            j += 1
            k += 1
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums)-1)
        return nums
        