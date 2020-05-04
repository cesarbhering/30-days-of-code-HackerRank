# MAIS UMA SOLUÇÃO QUE TIVE QUE CONSULTAR O FORUM, PORÉM DEVO TER MAIS ATENÇÃO AOS EXERCÍCIOS.
def levelOrder(self, root):
    fila = []
    no = root
    while no != None:
        print(no.data, end=' ')
        if no.left != None:
            fila.append(no.left)
        if no.right != None:
            fila.append(no.right)
        if len(fila) != 0:
            no = fila.pop(0)
        else:
            break
