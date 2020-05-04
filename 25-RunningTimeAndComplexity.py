#CONSEGUI FAZER O EXECÍCIO APÓS LER A DICA ABAIXO, POIS ESTAVA EXCEDENDO O LIMITE DE TEMPO PARA OS CÁLCULOS.
#For those interested: If a number is divisable by another number less or equal to the square root of the first number... it is NOT prime. 

for i in range(int(input())):
    num = int(input())
    quadrado = int(num ** 0.5)
    teste = 0
    if num == 1:
        print("Not prime")
        teste = 1
    elif num == 2:
        print("Prime")
        teste = 1
    else:
        for n in range(2,quadrado+1):
            if num % n == 0:
                print("Not prime")
                teste = 1
                break
    if teste == 0:
        print("Prime")


