def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid_index = int(len(nums) / 2)

        if (target <= nums[mid_index]):
                for i, val in enumerate(nums[0:mid_index]):
                        if (target >= val):
                                return i 
        ##FIXME fix these codes
        elif (target > nums[mid_index]):
                for i, val in enumerate(nums[mid_index::]):
                        if (target >= val):
                                return i + mid_index

        return
print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3,5,6],7))