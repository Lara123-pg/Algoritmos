tam = int(input("Digite o tamanho do vetor: "))

lista = [int(input("Digite um valor: ")) for x in range(tam)]

tam -= 1

def somaValores(valores, size):
    if size < 0:
        return 0
    
    else:
        return valores[size] + somaValores(valores, size - 1)

result = somaValores(lista, tam)

print(result)