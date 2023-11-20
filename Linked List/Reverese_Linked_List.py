"""
Leetcode : 206
Problem Statement: Given the head of a singly linked list, write a program to reverse the linked list, and 
return the head pointer to the reversed list.

Iterative Approach:
1. Use two pointers cur and prev to traverse the linked list and do following ops in each iteration :
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
until cur becomes None

Time Complexity -> O(N) Space Complexity -> O(1)

"""
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
