
from queue import priorityQueue
import random

fila=[]
prioridade = 0

for ordem_chegada in range(0, 10):
    prioridade = random.randint(1,11)
    fila.append((prioridade, ordem_chegada))

heapq.heapify(fila)
print(fila)

while not fila.empty():
    next_item = fila.get()
    print(next_item)

