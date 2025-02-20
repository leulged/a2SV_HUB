class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        pos = 0

        while curr and index > pos:
            curr = curr.next
            pos += 1

        if curr:
            return curr.val
            
        return -1

    def addAtHead(self, val: int) -> None:

        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:

        new_node = ListNode(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        pos = 0
        prev = None

        while temp and pos < index:
            prev = temp
            temp = temp.next
            pos += 1

        if pos != index:
            return

        prev.next = new_node
        new_node.next = temp

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        pos = 0
        prev = None

        while temp and pos < index:
            prev = temp
            temp = temp.next
            pos += 1

        if pos != index or temp is None:
            return
        print(temp.val)
        prev.next = temp.next
