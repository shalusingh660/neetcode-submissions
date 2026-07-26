class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums)-1
        def merge_sort(nums,start,end):
            if start<end:
                mid = (start + end)//2
                merge_sort(nums,start,mid)
                merge_sort(nums,mid+1,end)
                merge(nums,start,mid,end)
        def merge(nums,start,mid,end):
            i = start
            j = mid+1
            temp = []
            while(i<=mid and j<=end):
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            while(i<=mid):
                temp.append(nums[i])   
                i+=1
            while(j<=end):
                temp.append(nums[j])
                j+=1
            k=start
            for num in temp:
                nums[k]=num
                k+=1
        merge_sort(nums,0,len(nums)-1)
        return nums