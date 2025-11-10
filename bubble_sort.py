import time, tracemalloc, random

def bubble_sort(elemento):
    n = len(elemento)
    for i in range(n):
        for j in range(0, n-i-1):
            if elemento[j] > elemento[j+1]:
                elemento[j], elemento[j+1] = elemento[j+1], elemento[j]
    return elemento

print("Bubble sort\n")

lista = [5, 3, 8, 4, 2, 7]
print("Lista não ordenada: ", lista)

tracemalloc.start()
t_inicio = time.time()
lista_ordenada = bubble_sort(lista)
t_fim = time.time()
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Lista ordenada:", lista_ordenada)
print(f"tempo de execução: {t_fim-t_inicio:.6f} segundos")
print(f"memória usada: {memoria_pico/1024:.3f} KB")

print("\n\n=== Lista grande com 10000 elementos (números inteiros) ===")
lista = [random.randint(0, 10000) for i in range(10000)]

tracemalloc.start()
t_inicio = time.time()
lista_ordenada = bubble_sort(lista)
t_fim = time.time()
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

# print("Lista ordenada:", lista_ordenada)
print(f"tempo de execução: {t_fim-t_inicio:.6f} segundos")
print(f"memória usada: {memoria_pico/1024:.3f} KB")