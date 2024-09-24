def secuencia(n):
    if n < 2:
        return n
    else:
        return secuencia (n-1) + secuencia(n-2)

for i in range (10):
    print(secuencia(i))
