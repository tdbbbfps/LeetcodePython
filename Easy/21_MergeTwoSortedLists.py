def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1 = list1 + list2
        list1.sort()
        return list1


print((mergeTwoLists([1,2,4], [1,3,4])))
print((mergeTwoLists([], [])))
print((mergeTwoLists([], [0])))