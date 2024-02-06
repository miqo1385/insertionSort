import time
import random

arrx1 = [1, 2, 3, 4, 5, 6, 7, 9, 8]
arrx2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
arrx3 = [0, -1, 3, 4, 5, 11, 766, 12]
arrx4 = [random.randint(1, 1000) for _ in range(1000)]
arrx5 = [random.randint(1, 1000) for _ in range(1000)]
arrx6 = [(3, 'apple'), (2, 'banana'), (5, 'orange'), (2, 'grape'), (3, 'pineapple')]


def insertion_sort(arr):
    unsorted = arr
    start_time = time.time()  # Here we are using the time library. we will use this variable to start the time that
    # will measure
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position

    end_time = time.time()  # this variable will take the end time of the sorting

    time_insertion = end_time - start_time  # this will subtract the end time with the start time and will give
    # time it take the array to run

    return f'\tArray sorted using insertion: {arr}\n \tRunning time : {time_insertion}'


if __name__ == "__main__":
    print()
    print(f'\tBest-Case scenario: {arrx1}')
    print(insertion_sort(arrx1))
    print()
    print(f'\tWorse-Case scenario: {arrx2}')
    print(insertion_sort(arrx2))
    print()
    print(f'\tAverage-Case scenario: {arrx3}')
    print(insertion_sort(arrx3))
    print()
    print(f'\tFirst Large Data: {arrx4}')
    print(insertion_sort(arrx4))
    print()
    print(f'\tSecond Large Data: {arrx5}')
    print(insertion_sort(arrx5))
    print()
    print(f'\tSorting with Objects/Tuples: {arrx6}')
    print(insertion_sort(arrx6))
