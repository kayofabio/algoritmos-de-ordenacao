import time, tracemalloc, random

def heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

print("Heap sort\n")

lista = [12, 11, 13, 5, 6, 7]
print("Lista não ordenada: ", lista)

tracemalloc.start()
t_inicio = time.time()
heap_sort(lista)
t_fim = time.time()
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Lista ordenada: ", lista)
print(f"tempo de execução: {t_fim-t_inicio:.6f} segundos")
print(f"memória usada: {memoria_pico/1024:.3f} KB")

print("\n\n=== Lista grande com 10000 elementos ===")
lista = [random.randint(0, 10000) for i in range(10000)]

tracemalloc.start()
t_inicio = time.time()
lista_ordenada = heap_sort(lista)
t_fim = time.time()
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

# print("Lista ordenada:", lista_ordenada)
print(f"tempo de execução: {t_fim-t_inicio:.6f} segundos")
print(f"memória usada: {memoria_pico/1024:.3f} KB")
