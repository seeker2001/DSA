"""
Leetcode : 876
Problem Statement: Given the head of a singly linked list, return the middle node of the linked list. If 
there are two middle nodes, return the second middle node.

Solution 1:
1. Count the number of nodes in the list and find the index of middle node
2. Now by doing traversal again return the middle node.

Time Complexity -> O(N) Space Complexity -> O(1)

Optimal Solution:
1. Use hare and tortoise approach (i.e. slow and fast pointers) to find the middle node.

Time Complexity -> O(N) Space Complexity -> O(1)

"""
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1->2->3->4->5->6  fast.next -> None, fast -> None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
