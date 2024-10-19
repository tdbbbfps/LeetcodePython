def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    nums1 = nums1 + nums2
    nums1.sort()
    mid = int(len(nums1) / 2)
    print(f'{nums1}`s mid: idx:{mid}={nums1[mid]}')
    # Odd
    if (len(nums1) % 2 != 0 or len(nums1) == 1):
        return nums1[mid]
    # Even
    else:
        return (nums1[mid-1] + nums1[mid]) / 2


print(findMedianSortedArrays([2,2,4,4], [2,2,2,4,4]))
print(findMedianSortedArrays([2,2,4,4,4], [2,2,2,4,4]))
# print(findMedianSortedArrays([1,3], [2,4]))