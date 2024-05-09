# Generating 1000 random matrices of 1000 size
# performing generation too using multi-threading

# importing libraries
import random as r
import threading


matrix_matrices = [[] for i in range(1000)]


def generation_task(startIndex, endIndex):
    for i in range(startIndex, endIndex + 1):
        matrix = [[r.randint(0, 1000) for j in range(1000)] for k in range(1000)]
        matrix_matrices[i] = matrix
        print("running")


activeThreads = threading.active_count()

t1 = threading.Thread(target=generation_task, args=(0, 249))
t2 = threading.Thread(target=generation_task, args=(250, 499))
t3 = threading.Thread(target=generation_task, args=(500, 749))
t4 = threading.Thread(target=generation_task, args=(750, 999))

t1.start()
t2.start()
t3.start()
t4.start()

while threading.active_count() != activeThreads:
    pass
