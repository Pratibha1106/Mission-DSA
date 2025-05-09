# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        newList = ListNode()
        temporary_list = newList

        def getSmallestValue():
            min_value = float('inf')  
            min_index = -1 
            for i in range(len(lists)):
                if lists[i] is not None and lists[i].val < min_value:
                    min_value = lists[i].val
                    min_index = i
            if min_index != -1:
                lists[min_index] = lists[min_index].next
            return min_value
        
        while True:
            x = getSmallestValue() 
            if x == float('inf'):
                break
            c = ListNode(val=x)
            temporary_list.next = c
            temporary_list = temporary_list.next 
        
        return newList.next