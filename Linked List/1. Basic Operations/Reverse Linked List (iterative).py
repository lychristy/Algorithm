#Reverse Linked List (iterative)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def reverse(self, head):
    """
    input: ListNode head
    return: ListNode
    """
    # write your solution here

    if head is None or head.next is None:
      return head

    prev = None
    while head:
      next = head.next
      head.next = prev
      prev = head
      head = next
    
    return prev