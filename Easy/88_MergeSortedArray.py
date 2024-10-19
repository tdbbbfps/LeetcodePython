def merge(nums1: list[int], m: int, nums2: list[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Can you come up with an algorithm that runs in O(m + n) time?
        # No. I can only come up with O(len(nums1) + len(nums2))
        for i, val in enumerate(nums1):
                if (val == 0):
                        nums1.pop(i)
        for i, val in enumerate(nums2):
                if (val == 0):
                        nums2.pop(i)
        print(f'1:{nums1}, 2:{nums2}')
        nums1 = nums1[:m] + nums2[:n]
        nums1.sort()
        print(nums1)
merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3)
# merge([1,2,3,0,0,0], 3, [2,5,6], 3)
# merge([1], 1, [], 0)
# merge([0], 0, [1], 1)