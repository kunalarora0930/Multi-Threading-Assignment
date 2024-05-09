# Multithreading Matrix Multiplication in Python

## Introduction

This Python project explores the concept of multithreading in Python by applying it to matrix multiplication. Matrix multiplication is a computationally intensive task, especially when dealing with large matrices. By utilizing multithreading, we aim to parallelize the matrix multiplication process, thereby potentially reducing the overall execution time.

## Requirements
1. Python 3.x
2. NumPy
3. Matplotlib (for visualization)

## Project Structure
`Multi_threading.py` : Contains the main script to execute the multithreaded matrix multiplication and analyze the performance.

`matrices.py`: Module to generate random matrices for multiplication.

`README.md`: Documentation providing an overview of the project, instructions, and analysis.

## Aproach
`Matrix Generation`: The matrix_matrices module generates a list of random matrices of shape (1000, 1000) using NumPy's randint() function. These matrices serve as input for the matrix multiplication task.

`Matrix Multiplication Function`: The matrix_multiplication() function performs matrix multiplication using NumPy's dot() function.

`Multithreading`: The multiplication_task() function represents the task of matrix multiplication for a subset of matrices. We divide the total number of matrices into chunks and assign each chunk to a separate thread for parallel execution.

`Thread Management`: The run_threads() function initializes and starts multiple threads, each responsible for a chunk of matrix multiplication tasks. Once all threads have completed their tasks, the function calculates and returns the total execution time.

`Analysis`: We analyze the performance of multithreading by varying the number of threads from 1 to 15. For each configuration, we measure the execution time and plot a graph depicting the relationship between the number of threads and the time taken.

## Results
The execution time decreases as the number of threads increases, up to a certain point. Beyond that point, adding more threads may not lead to further improvements and could even degrade performance due to overhead. The optimal number of threads depends on various factors such as the number of available CPU cores and the nature of the computation.

![](https://github.com/maheshmani13/MultiThreading-Analysis/blob/main/time.png)

![](https://github.com/maheshmani13/MultiThreading-Analysis/blob/main/Time%20Vs%20Threads.png)


## Conclusion
Multithreading can significantly improve the performance of computationally intensive tasks like matrix multiplication by utilizing the available computational resources more efficiently. However, it requires careful consideration of factors such as load balancing, overhead, and synchronization to achieve optimal results.
