import time, tracemalloc, random

def counting_sort(array):
    size = len(array)
    output = [0] * size

    count = [0] * (max(array) + 1)

    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, (max(array) + 1)):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

print("Counting sort\n")

lista = [4, 2, 2, 8, 3, 3, 1]
print("Lista não ordenada:", lista)

tracemalloc.start()
t_inicio = time.time()
counting_sort(lista)
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
lista_ordenada = counting_sort(lista)
t_fim = time.time()
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

# print("Lista ordenada:", lista_ordenada)
print(f"tempo de execução: {t_fim-t_inicio:.6f} segundos")
print(f"memória usada: {memoria_pico/1024:.3f} KB")
