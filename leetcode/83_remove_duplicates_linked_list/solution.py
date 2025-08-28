class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head
        
        tail = head
        while tail.next:
            if tail.val == tail.next.val:
                tail.next = tail.next.next
            else:
                tail = tail.next

        return head
