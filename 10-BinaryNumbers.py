n = 5
numeroBinario = []
restante = 0

#Cria lista com o número binário
while n >= 1:
    restante =  n % 2
    n = n/2
    numeroBinario.insert(0,int(restante))

print(*numeroBinario, sep='')

#Verifica o máximo de repetições consecutivas do nº 1.
Count = 0
MaxCount = 0
for i in numeroBinario:
    if i is 1:
        Count += 1
        if Count >= MaxCount:
            MaxCount = Count
    else:
            Count = 0

print(MaxCount)