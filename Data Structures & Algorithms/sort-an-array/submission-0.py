class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        size = 1

        while size < n:
            left = 0

            while left < n:
                mid = min(left + size - 1, n - 1)
                right = min(left + 2 * size - 1, n - 1)

                temp = []
                i = left
                j = mid + 1

                while i <= mid and j <= right:
                    if nums[i] <= nums[j]:
                        temp.append(nums[i])
                        i += 1
                    else:
                        temp.append(nums[j])
                        j += 1

                while i <= mid:
                    temp.append(nums[i])
                    i += 1

                while j <= right:
                    temp.append(nums[j])
                    j += 1

                for k in range(len(temp)):
                    nums[left + k] = temp[k]

                left += 2 * size

            size *= 2

        return nums

            
