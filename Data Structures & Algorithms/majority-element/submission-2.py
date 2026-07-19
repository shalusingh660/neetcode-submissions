class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for val in nums:
            if val in count:
                count[val]+=1
            else:
                count[val] = 1
        for val in count:
            if count[val] > len(nums)//2:
                return val


        