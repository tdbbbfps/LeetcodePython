# receive a list of numbers and I have to figure out which two numbers can be the sum of target
# O(n^2)
def twoSum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j] == target):
                # return indexs
                return [i,j]
    return []

# if num list has 5 elements then the loop will at most go through 5 times
# O(n)
def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Store nums' index in this dict.
    num_to_index = {}
    # iterate the nums list (i as index, num as value) (I think this is better than using range(nums) when you need index and elements at the same time.)
    
    for i, num1 in enumerate(nums):
        # target = num1 + num2, target - num1 then the rest will be num2
        num2 = target - num1
        # check if there's any same value(key) in the dict, if do then return num1 and num2
        if (num2 in num_to_index):
            print(num_to_index)
            return [i, num_to_index[num2]]
        # Store into dict number(key): index(value)
        num_to_index[num1] = i

    return []

numlist = [2,7,11,15]
target = 17
# print(twoSum1(numlist, target))
print(twoSum2(numlist, target))