class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        result = 0

        for num in nums:
            if num-1 not in numSet:
                current_num = num
                current_count = 1

                while current_num+1 in numSet:
                    current_num += 1
                    current_count +=1
                

                result = max(current_count, result)

        return result
