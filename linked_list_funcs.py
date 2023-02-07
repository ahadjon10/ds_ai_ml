#@title Ma'lumotlar tuzilmasi va algoritmlar

#linked lists

class Node:

    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def push(self, new_data):
        #yangi tugun yarat
        new_node = Node(new_data)
        #bosh tugunni bitta keyinga sur
        new_node.next = self.head
        #yangi tugunni listni boshiga olib o`t
        self.head = new_node


    