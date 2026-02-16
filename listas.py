def double(arr):
    lista = []
    for x in arr:
        lista.append(x * 2)
    return lista

def maximum(arr):
    return max(arr)

def average(arr):
    return sum(arr) / len(arr)

def main():
    lista = [3, 8, 3, 4, 6]
    
    print("Lista original:", lista)
    print("Doble:", double(lista))
    print("Máximo:", maximum(lista))
    print("Promedio:", average(lista))

main()
