class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num]+= 1
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])

        for key , value in seen.items():
            bucket[value].append(key)
        top_k = []
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k
            

            
        
        