import time, tracemalloc, random

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista)//2]
        menores = [x for x in lista if x < pivot]
        iguais = [x for x in lista if x == pivot]
        maiores = [x for x in lista if x > pivot]
        return quick_sort(menores) + iguais + quick_sort(maiores)

print("Quick sort\n")

lista = [5, 3, 8, 4, 2, 7]
print("Lista não ordenada: ", lista)

tracemalloc.start()
t_inicio = time.time()
lista_ordenada = quick_sort(lista)
t_fim = time.time()
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Lista ordenada: ", lista_ordenada)
print(f"tempo de execução: {t_fim-t_inicio:.6f} segundos")
print(f"memória usada: {memoria_pico/1024:.3f} KB")

print("\n\n=== Lista grande com 10000 elementos ===")
lista = [random.randint(0, 10000) for i in range(10000)]

tracemalloc.start()
t_inicio = time.time()
lista_ordenada = quick_sort(lista)
t_fim = time.time()
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

# print("Lista ordenada:", lista_ordenada)
print(f"tempo de execução: {t_fim-t_inicio:.6f} segundos")
print(f"memória usada: {memoria_pico/1024:.3f} KB")
