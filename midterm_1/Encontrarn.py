from stackp import Stack
import time

def encontrar_n_para_5_segundos():
    n = 5000000  
    while True:
        start_time = time.time()
        
        stack = Stack(n)  
        for _ in range(n):
            stack.push("x")  
        
        elapsed_time = time.time() - start_time  
        
        if elapsed_time >= 1:
            return n, elapsed_time  
        
        n += 5000  


n_encontrado, tiempo_tomado = encontrar_n_para_5_segundos()
print(f"Se encontró n = {n_encontrado}, con un tiempo de {tiempo_tomado:.2f} segundos.")