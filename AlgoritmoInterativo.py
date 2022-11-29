tam = int(input("Digite o tamanho do vetor: "))

lista = [int(input("Digite um valor: ")) for x in range(tam)]

def somaValores(valores):
    soma = 0

    for x, y in enumerate(valores):
        if x != len(valores):
            soma += y
    
    return soma

result = somaValores(lista)

print(result)