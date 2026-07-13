class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        found =False
        for num in nums:
            if num in seen:
                found = True
                break
            else:
                seen.add(num)
                found = False
        return found  
        