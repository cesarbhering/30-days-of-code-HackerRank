#CONSULTEI ESTA SOLUÇÃO NO FORUM, PRECISO ESTUDAR MAIS RECURSIVIDADE.
def getHeight(self, root):
    if root == None or (root.left == 0 and root.right == 0):
        return -1
    else:
        AltEsquerda = self.getHeight(root.left)+1
        AltDireita = self.getHeight(root.right)+1
        return max(AltDireita, AltEsquerda)
