class Solution:
    def convToArr(self, string: str):
        arr = [0] * 26
        for i in string:
            arr[ord(i)-97] += 1
        return tuple(arr)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}
        for i in strs:
            iArr = self.convToArr(i)
            if iArr in anaDict: anaDict[iArr].append(i)
            else: anaDict[iArr] = [i]
        final = []
        for i in anaDict.values():
            final.append(i)
        return final