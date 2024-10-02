def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
                if (nums[i] == val):
                        nums.pop(i)
                        continue
                else:
                        i += 1
        return len(nums), nums



print(removeElement([3,2,2,3],3))
print(removeElement([0,1,2,2,3,0,4,2],2))