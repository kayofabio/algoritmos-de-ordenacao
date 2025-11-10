import time, tracemalloc, random

def counting_sort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

def radix_sort(array):
    max_element = max(array)

    place = 1
    while max_element // place > 0:
        counting_sort(array, place)
        place *= 10

print("Radix sort")

lista = [121, 432, 564, 23, 1, 45, 788]
print("Lista não ordenada: " ,lista)

tracemalloc.start()
t_inicio = time.time()
radix_sort(lista)
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
lista_ordenada = radix_sort(lista)
t_fim = time.time()
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

# print("Lista ordenada:", lista_ordenada)
print(f"tempo de execução: {t_fim-t_inicio:.6f} segundos")
print(f"memória usada: {memoria_pico/1024:.3f} KB")
