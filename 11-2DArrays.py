resultado = []
for x in range(0, 4):
    for y in range(0, 4):
        resultado.append(sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3]))

print(max(resultado))
