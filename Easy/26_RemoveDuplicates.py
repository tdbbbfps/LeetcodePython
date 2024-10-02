def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        # Set dont allow duplicate elements, so transform to set will automatically kill duplications
        nums[:] = sorted(set(nums))
        return len(nums)
        # iterate through the array
        # i = 0
        # while i < len(nums):
        #         if (i + 1 < len(nums) and nums[i] == nums[i+1]):
        #                 nums.pop(i+1)
        #         else:
        #                 i += 1
        # return len(nums)

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))