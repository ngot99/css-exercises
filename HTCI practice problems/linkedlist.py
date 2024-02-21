# linkedlist.py
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def appendToTail(self, d):
        end = Node(d)
        if self.head is None:
            self.head = end
            return
        
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        
        curr_node.next = end

    def printList(self):
        curr_node = self.head
        if self.head is None:
            print("list is emptty")
            return
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
def remove_dupe2(ll):
    prev_node = ll.head
    #if there is more than 1 node. 
    if prev_node.next:
        curr_node = ll.head.next
        # nested loop, compare each node to every othere node and remove dups along the way
        while prev_node.next:
            while curr_node.next:
                if prev_node.data == curr_node.data:
                    curr_node.next = curr_node.next.next
                else:
                    curr_node = curr_node.next
            prev_node = prev_node.next
            curr_node = prev_node.next
    else:
        return