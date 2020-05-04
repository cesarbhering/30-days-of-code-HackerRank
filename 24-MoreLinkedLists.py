#OUTRA SOLUÇÃO QUE TIVE QUE CONSULTAR, APESAR DE ENTENDER O CONCEITO.
def removeDuplicates(self, head):
    h = head
    while head.next != None:
        if head.next.data != head.data:
            head = head.next
        else:
            head.next = head.next.next
    return h
