#@title Ma'lumotlar tuzilmasi va algoritmlar

#linked lists

from linked_list_funcs import Node, LinkedList
#bo`sh list yaratamiz
llist = LinkedList()
#tugun yaratamiz
llist.head=Node("soat 6:30 da uyg'onaman")
seven = Node("soat yettida uy ishlarini qilaman")
eight = Node("soat 8:00 da universitetga yo`l olaman")

#tugunlarni bog`laymiz`

llist.head.next = seven
seven.next  = eight
#endi konsolga chiqaramiz
#llist.printList()

#yangi tugun boshiga qo'shish

llist.push("soat 6:00 da tush ko`rayotgan bo`laman")
#llist.printList()