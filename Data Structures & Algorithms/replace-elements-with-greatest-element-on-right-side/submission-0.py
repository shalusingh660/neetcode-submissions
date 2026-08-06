class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        for i in range(len(arr)):
            right_max=-1
            for j in range(i+1,len(arr)):
                if arr[j] > right_max:
                    right_max = arr[j]
            ans[i] = right_max
        return ans