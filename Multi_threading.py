import time
import threading

import matplotlib.pyplot as plt
import numpy as np

# importing random generate matrices from out matrices file
from matrices import matrix_matrices


def matrix_multiplication(X, Y):
    # Perform matrix multiplication of matrices X and Y.
    result = np.dot(X, Y)
    return result


def multiplication_task(start_index, end_index, matrix):
    # Perform matrix multiplication for a subset of matrices in matrix_list.
    for i in range(start_index, end_index + 1):
        matrix_multiplication(matrix_matrices[i], matrix)


def run_threads(num_threads):
    """
    Run matrix multiplication tasks using multiple threads.
    """
    threads = []
    matrix = np.random.randint(0, 1000, size=(1000, 1000))
    start_time = time.time()
    chunk_size = len(matrix_matrices) // num_threads
    active_threads = threading.active_count()
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size - 1 if i < num_threads - 1 else len(matrix_matrices) - 1
        t = threading.Thread(target=multiplication_task, args=(start, end, np.copy(matrix)))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return time.time() - start_time


if __name__ == "__main__":
    threads_count_array = list(range(1, 16))
    run_times = []

    for thread_count in threads_count_array:
        time_taken = run_threads(thread_count)
        run_times.append(time_taken)
        print(f"Number of threads: {thread_count}, Time Taken: {time_taken} seconds")

    i = 1
    print("threads time")
    for time in run_times:
        print(str(i) + "       " + str(time) + "s")
        i = i+1
    plt.plot(threads_count_array, run_times)
    plt.xlabel('Number of Threads')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Number of Threads vs Execution Time')
    plt.show()
