class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    class Solution:
        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            head = None
            temp = None
            carry = 0

            while l1 is not None or l2 is not None:
                sum = carry
                if l1 is not None:
                    sum += l1.val
                    l1 = l1.next
                if l2 is not None:
                    sum += l2.val
                    l2 = l2.next
                new_node = ListNode(sum % 10 + carry)
                carry = sum // 10
                if temp is None:
                    temp = head = new_node
                else:
                    temp.next = new_node
                    temp = temp.next

            if carry > 0:
                temp.next = ListNode(carry)
            return head

