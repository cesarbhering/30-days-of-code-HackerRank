# Enter your code here. Read input from STDIN. Print output to STDOUT
NumPhones = int(input())
PhoneDict = {}
#Cria o Dicinário
for n in range(NumPhones):
    PhoneList = list(map(str,input().split()))
    PhoneDict.update({PhoneList[0]: PhoneList[1]})

#Printa nome=numero, caso esteja no dict, se nao printa not found.
while True:
    try:
        Nome = str(input())
        if Nome in PhoneDict:
            print(Nome + "=" + PhoneDict[Nome])
        else:
            print("Not found")
    except: break