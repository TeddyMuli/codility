#!/usr/bin/python3
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        tail = head
        carry = 0

        while l1 or l2 or carry != 0:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            sum = digit1 + digit2 + carry
            num = sum % 10
            carry = sum // 10
            tail.next = ListNode(num)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
