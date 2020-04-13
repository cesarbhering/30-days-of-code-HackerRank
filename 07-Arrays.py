arr = [1, 4, 3, 2]
arr = arr[::-1]
result = ""
for i in arr:
    result += str(i)+" "
print(result)

#Também daria, mas foi cola.
# print(' '.join(map(str,arr[::-1]))) 


