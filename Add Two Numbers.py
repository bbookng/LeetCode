# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def make_number(self, li: Optional[ListNode]) -> int:
        number = 0
        std = 1
        while li:
            number += li.val * std
            li = li.next
            std *= 10
        return number

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1, number2 = self.make_number(l1), self.make_number(l2)
        result = number1 + number2

        answer = ListNode()
        answer.val = str(result)[-1]
        current = answer

        for number in str(result)[::-1][1:]:
            current.next = ListNode(int(number))
            current = current.next

        return answer

