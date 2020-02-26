#Rotate List by K places
#Input: 1->2->3->4->5->NULL, k = 12, Output: 4->5->1->2->3->NULL

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def rotateKplace(self, head, n):
    """
    input: ListNode head, int n
    return: ListNode
    """
    # write your solution here
    if head is None:
      return head
    
    l1 = 1
    p1 = head
    while p1.next:
      l1 += 1
      p1 = p1.next
    
    n = n % l1

    if n == 0:
      return head
    
    l2 = 1
    p2 = head
    while l2 < l1 - n:
      p2 = p2.next
      l2 += 1
    
    p1.next = head
    head = p2.next
    p2.next = None

    return head

