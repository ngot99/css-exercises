from linkedlist import Node
from linkedlist import LinkedList
# 2.1 remove dupe from an unsorted linked list
# Given an unsorted linked list, identify any duplicates and remove the node
# While node != end, traverse through
# If value is in list, make curr node skip to next. 
# If value is not dup, just continue traversing.
def remove_dupe(ll):
    set1 = set()
    curr_node = ll.head
    set1.add(curr_node.data)

    while curr_node.next:
        print("test")
        if curr_node.next.data in set1:
            print("dupe value", curr_node.next.data)
            curr_node.next = curr_node.next.next

        else:
            set1.add(curr_node.data)
            curr_node = curr_node.next

def remove_dupe2(ll):
    prev_node = ll.head
    #if there is more than 1 node. 
    if prev_node.next:
        curr_node = prev_node.next
        # nested loop, compare each node to every othere node and remove dups along the way
        while prev_node.next:
            while curr_node.next:
                if prev_node.data == curr_node.data:
                    curr_node.next = curr_node.next.next
                else:
                    curr_node = curr_node.next
            prev_node = prev_node.next
            print(prev_node.data)
            curr_node = prev_node.next
    else:
        return
    
# Helper function that creates a linked list.
def create_ll(ll,values):
    #ll.appendToTail(1)
    for i in range(len(values)):
        ll.appendToTail(values[i])

if __name__ == "__main__":
    ll = LinkedList()
    values = [0,1,0]
    create_ll(ll,values)
    #ll.printList()
    #remove_dupe(ll)
    remove_dupe2(ll)
    ll.printList()
