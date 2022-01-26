# https://www.geeksforgeeks.org/linked-list-vs-array/
# https://zippy-lan-200.notion.site/Intro-to-Linked-Lists-2ea969ab51874fb688d15973ffa12a61

# Linked Lists
from email import header


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

new_node = Node(5)

# print(new_node)
# print(new_node.value)
# print(new_node.next)
class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def pushOn(self, new_value):
        new_node = Node(new_value, self.head)
        self.head = new_node

    def append(self, new_value):
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
        
        last = self.head

        while last.next:
            print("+++++++++++++")
            print(f'Current Node: {last}')
            print(f'Current Value: {last.value}')
            print(f'Current next: {last.next}')
            last = last.next
            print('+++++++++++++')
            print(f'New node is at:{last}')
        last.next = new_node

    def removeDups(self):
        if self.head is None:
            return self.head
        values = set()
        values.add(self.head.value)

        temp = self.head
        while temp and temp.next:
            if temp.next.value in values:
                temp.next = temp.next.next
            else:
                values.add(temp.next.value)
                temp = temp.next
        return self.head

    def reverseIt(self,head):
        if head is None:
            return None
        if head.next is None:
            return head
        
        new_head = self.reverseIt(head.next)
        head.next.next = head
        head.next = None
        return new_head

    


        
        

my_list = LinkedList()

my_list.pushOn('Nate')
my_list.pushOn("Billy")
my_list.append('Coding Temple')
new_list = my_list.reverseIt(my_list.head)
print(new_list.next.next)




    


# linked_list = LinkedList()


