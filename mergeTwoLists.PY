class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        s = t = ListNode(0)
        while not (l1 is None or l2 is None):
            if l1.val < l2.val:
                c = l1
                l1 = l1.next
            else:
                c = l2
                l2 = l2.next
            t.next = c
            t = t.next
        t.next = l1 or l2
        return s.next
                
