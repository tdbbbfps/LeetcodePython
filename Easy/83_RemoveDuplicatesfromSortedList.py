# LinkedList contain two things: data and its next node
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    duplicates = []
    for i in head:
        if (not i in duplicates):
            duplicates += i
    return head


deleteDuplicates([1,1,2])