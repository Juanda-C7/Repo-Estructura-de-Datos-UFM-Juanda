class Stack:
    def __init__(self, size: int):
        self.max = size
        self.elements = [None] * size
        self.top = -1

    def __repr__(self):
        return f'Current stack: {self.elements} | Top: {self.top}'
    
    def push(self, val: str) -> None:
        if self.top == self.max - 1:
            print('Stack overflow')
            return None
        
        self.top += 1
        self.elements[self.top] = val
    
    def pop(self) -> any:
        if self.top == -1:
            print('Stack underflow')
            return None

        val = self.elements[self.top]
        self.elements[self.top] = None 
        self.top -= 1
        return val
    
    def peek(self) -> any:
        if self.top == -1:
            print('Stack underflow')
            return None

        return self.elements[self.top]

    def search(self, key: str) -> int:
        """Busca un elemento en el stack y devuelve su índice desde la cima.
        Retorna -1 si no se encuentra."""
        for i in range(self.top, -1, -1):  # Buscar desde el top hacia abajo
            if self.elements[i] == key:
                return self.top - i  # Posición relativa desde la cima
        return -1  # No encontrado
