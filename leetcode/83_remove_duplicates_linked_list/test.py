import unittest
from solution import Solution

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def list_to_linked(arr):
    head = ListNode()
    tail = head
    for val in arr:
        tail.next = ListNode(val)
        tail = tail.next
    return head.next

class TestSolution(unittest.TestCase):
    def test(self):
        sol = Solution()
        tests = [
            ([1,1,2], [1,2]),
            ([1,1,2,2], [1,2]),
            ([1,1,2,3,3], [1,2,3]),
            ([], [])
        ]
        for data, expected in tests:
            with self.subTest(data=data):
                head = list_to_linked(data)
                result = sol.deleteDuplicates(head)
                self.assertEqual(linked_to_list(result), expected)

if __name__ == "__main__":
    unittest.main()
