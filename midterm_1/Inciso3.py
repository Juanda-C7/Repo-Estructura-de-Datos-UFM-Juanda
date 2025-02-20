from stackp import Stack
import time


n = 5090000  # Valor de n encontrado previamente

# Crear 5 stacks con tamaños n, 2n, 3n, 4n, 5n
stacks = [Stack(i * n) for i in range(1, 6)]

# Poblar cada stack completamente con "X"
for stack in stacks:
    for _ in range(stack.max):  # Llenar hasta el tamaño máximo
        stack.push("X")

print("Todos los stacks han sido poblados completamente.")

#inciso 5


def operations():
    for stack in stacks:
        stack.search("Y")  
        stack.pop()  

operations()