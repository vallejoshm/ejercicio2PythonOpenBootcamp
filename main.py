numero_inicial = 0
numero_final = 10
impares = []
for num in range (numero_inicial,numero_final+1):
    if num % 2 != 0 :
        impares.append(num)

print(impares)