"""
Two pointer approach
Time = O(n)
Space = O(1)
"""


def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    ref_ptr = main_ptr = head
    count = 0
    
    for _ in range(n):
        ref_ptr = ref_ptr.next
    
    if not ref_ptr:
        return head.next
    
    while ref_ptr.next:
        ref_ptr = ref_ptr.next
        main_ptr = main_ptr.next
    
    print("Node no. % d from last is % d " %(n, main_ptr.data)) 
    
    main_ptr.next = main_ptr.next.next
    return head