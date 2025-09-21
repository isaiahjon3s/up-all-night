# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head to simplify the logic
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Process both lists while either has nodes or there's a carry
        while l1 or l2 or carry:
            # Get values from current nodes (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the actual head (skip dummy)
        return dummy_head.next

# Helper functions for testing
def create_linked_list(nums):
    """Create a linked list from a list of numbers"""
    if not nums:
        return None
    
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def print_linked_list(head):
    """Print linked list values"""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: 342 + 465 = 807 (represented as [2,4,3] + [5,6,4] = [7,0,8])
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test 1: {print_linked_list(result)}")  # Should output [7, 0, 8]
    
    # Test case 2: 0 + 0 = 0
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test 2: {print_linked_list(result)}")  # Should output [0]
    
    # Test case 3: 999 + 1 = 1000 (represented as [9,9,9] + [1] = [0,0,0,1])
    l1 = create_linked_list([9, 9, 9])
    l2 = create_linked_list([1])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test 3: {print_linked_list(result)}")  # Should output [0, 0, 0, 1]
        