DataDevolucao = list(map(int, input().split(" ")))
DataPrevista = list(map(int, input().split(" ")))

if DataDevolucao[2] == DataPrevista[2] and DataDevolucao[1] == DataPrevista[1]:
    if DataDevolucao[0] <= DataPrevista[0]:
        print("0")
    elif DataDevolucao[0] > DataPrevista[0]:
        print((int(DataDevolucao[0])-int(DataPrevista[0]))*15)

if DataDevolucao[2] == DataPrevista[2] and DataDevolucao[1] != DataPrevista[1]:
    if DataDevolucao[1] <= DataPrevista[1]:
        print("0")
    elif DataDevolucao[1] > DataPrevista[1]:
        print((int(DataDevolucao[1])-int(DataPrevista[1]))*500)

if DataDevolucao[2] != DataPrevista[2]:
    if DataDevolucao[2] <= DataPrevista[2]:
        print("0")
    else:
        print("10000")
