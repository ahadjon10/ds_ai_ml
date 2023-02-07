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

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("tugun mavjud emas")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last=self.head
        while last.next:
            last = last.next
        last.next = new_node
    def deleteNode(self, key):
        #listni boshini top
        temp = self.head
        #birinchi node(tugunni) tekshiramiz
        if (temp and temp.data==key):
            self.head = temp.next
            temp = None
            return
            #bo'lmasa keyingi tugunlarni ko'rib chiqamiz
        while temp:
            if temp.data ==key:
                break
            prev=temp
            temp=temp.next
        #agar qiymat topilmasa
        if temp==None:
            return
        #tugunni listdab o'chiramiz
        prev.next = temp.next
        temp=None    
        

    