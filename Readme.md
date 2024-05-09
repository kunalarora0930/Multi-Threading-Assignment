# Concurrent Matrix Multiplication in Python

## Introduction

This Python project delves into multithreading in Python, specifically focusing on its application to matrix multiplication. Matrix multiplication is computationally demanding, particularly with large matrices. By employing multithreading, the aim is to parallelize the matrix multiplication process, potentially reducing overall execution time.

## Requirements
1. Python 3.x
2. NumPy
3. Matplotlib (for visualization)

## Project Structure
- `Multi_threading.py`: Main script executing the multithreaded matrix multiplication and performance analysis.
- `matrices.py`: Module generating random matrices for multiplication.
- `README.md`: Documentation offering project overview, instructions, and analysis.

## Approach
- **Matrix Generation**: The `matrices` module generates a list of random matrices of shape (1000, 1000) using NumPy's `randint()` function.
- **Matrix Multiplication Function**: The `matrix_multiplication()` function conducts matrix multiplication via NumPy's `dot()` function.
- **Multithreading**: The `multiplication_task()` function represents matrix multiplication task for a subset of matrices. The total matrices are divided into chunks, and each chunk is assigned to a separate thread for parallel execution.
- **Thread Management**: The `run_threads()` function initializes and starts multiple threads, each responsible for a chunk of matrix multiplication tasks. Upon completion of all threads' tasks, the function calculates and returns the total execution time.
- **Analysis**: Performance of multithreading is analyzed by varying the number of threads from 1 to 15. For each configuration, execution time is measured, and a graph is plotted illustrating the relationship between thread count and time taken.

## Results
Execution time decreases as the number of threads increases, up to a certain threshold. Beyond that point, adding more threads may not yield further improvements and could potentially degrade performance due to overhead. The optimal number of threads depends on factors like CPU core count and computation nature.

![Time Plot](https://github.com/kunalarora0930/Multi-Threading-Assignment/blob/main/time.png)

![Time vs. Threads Plot](https://github.com/kunalarora0930/Multi-Threading-Assignment/blob/main/Time%20Vs%20Threads.png)

## Conclusion
Multithreading can notably enhance the performance of computationally intensive tasks like matrix multiplication by efficiently utilizing available computational resources. However, achieving optimal results requires careful consideration of factors such as load balancing, overhead, and synchronization.
