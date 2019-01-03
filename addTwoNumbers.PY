class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        root = head = ListNode(0)
        while l1 or l2 or carry:
            l1, val1 = [l1.next, l1.val] if l1 else [0, 0]
            l2, val2 = [l2.next, l2.val] if l2 else [0, 0]
            carry,curr = divmod(val1+val2+carry, 10) #Update carry=sum/10carry = sum / 10carry=sum/10 and create a new node with the digit value of (sum mod 10)
            head.next = ListNode(curr) #set it to current node's next
            head = head.next #advance current node to next
        return root.next

        
