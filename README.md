# Big O Algorithms Analysis in Python

This repository contains implementations of various algorithms along with their Big O analysis. Each algorithm is provided with a brief explanation and a code sample.

## 1. Constant Time (O(1))

### Explanation:

Constant time complexity implies that the runtime of an algorithm remains constant regardless of the size of the input data.

### Example:

```python
def constant_time_algo(arr):
    return arr[0]

# Example usage:
result = constant_time_algo([1, 2, 3, 4, 5])
print(result)  # Output: 1

```

## 2. Linear Time (O(n))

### Explanation:

Linear time complexity means that the runtime of an algorithm grows linearly with the size of the input data.

### Example:

```python
def linear_time_algo(arr):
    for num in arr:
        print(num)

# Example usage:
linear_time_algo([1, 2, 3, 4, 5])
# Output:
# 1
# 2
# 3
# 4
# 5

```

## 3. Quadratic Time (O(n^2))

### Explanation:

Quadratic time complexity indicates that the runtime of an algorithm grows quadratically with the size of the input data.

### Example:

```python
def quadratic_time_algo(arr):
    for i in arr:
        for j in arr:
            print(i, j)

# Example usage:
quadratic_time_algo([1, 2, 3])
# Output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3


```

## 4. Logarithmic Time (O(log n))

### Explanation:

Logarithmic time complexity means that the runtime of an algorithm grows logarithmically with the size of the input data.

### Example:

```python
import math

def logarithmic_time_algo(n):
    return math.log(n, 2)

# Example usage:
result = logarithmic_time_algo(16)
print(result)  # Output: 4.0


```

## Array Operations in Python

Arrays are fundamental data structures in Python that store collections of items, usually of the same data type. Python provides extensive support for array manipulation through built-in functions and libraries. This section outlines common array operations in Python.

## 1. Creating Arrays

# 1.1. Using Lists

```python
Copy code
my_array = [1, 2, 3, 4, 5]
```

# 1.2. Using the array Module

```python
Copy code
import array
my_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates integer type
```

# 1.3. Using NumPy

```python
Copy code
import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
```

## 2. Accessing Elements

# 2.1. Accessing by Index

```python
Copy code
print(my_array[0])  # Output: 1
```

# 2.2. Slicing

python
Copy code
print(my_array[1:4]) # Output: [2, 3, 4]

## 3. Modifying Arrays

# 3.1. Changing Element Value

```python
Copy code
my_array[0] = 10
```

# 3.2. Appending Elements

python
Copy code
my_array.append(6)

# 3.3. Removing Elements

```python
Copy code
my_array.remove(3)  # Removes the first occurrence of 3
```

## 4. Array Operations

# 4.1. Sorting

```python
Copy code
sorted_array = sorted(my_array)
```

# 4.2. Reversing

```python
Copy code
reversed_array = my_array[::-1]
```

# 4.3. Finding Maximum and Minimum

```python
Copy code
max_value = max(my_array)
min_value = min(my_array)
```

## 5. Combining Arrays

# 5.1. Concatenating Arrays

```python
Copy code
combined_array = my_array1 + my_array2
```

# 5.2. Extending Arrays

```python
Copy code
my_array1.extend(my_array2)
```

## 6. Searching

# 6.1. Linear Search

```python
Copy code
index = my_array.index(4)
```

# 6.2. Binary Search (for Sorted Arrays)

```python
Copy code
import bisect
index = bisect.bisect_left(sorted_array, 4)
```

## 7. Iterating Over Arrays

# 7.1. Using a Loop

```python
Copy code
for item in my_array:
    print(item)
```

# 7.2. Using List Comprehension

```python
Copy code
squared_array = [x**2 for x in my_array]
```

# Sorting Algorithms

## Bubble Sort

```cpp
#include <bits/stdc++.h>
using namespace std;

void bubbleSort(int arr[], int n)
{
    int i, j;
    bool swapped;
    for (i = 0; i < n - 1; i++)
    {
        swapped = false;
        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (swapped == false)
            break;
    }
}
void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        cout << " " << arr[i];
}
int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int N = sizeof(arr) / sizeof(arr[0]);
    bubbleSort(arr, N);
    cout << "Sorted array: \n";
    printArray(arr, N);
    return 0;
}
```

```python
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
```

## Selection Sort

```cpp
#include <bits/stdc++.h>
using namespace std;

void selectionSort(int arr[], int n)
{
    int i, j, min_idx;

    for (i = 0; i < n - 1; i++)
    {
        min_idx = i;
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        if (min_idx != i)
            swap(arr[min_idx], arr[i]);
    }
}
void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
        cout << endl;
    }
}
int main()
{
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);

    selectionSort(arr, n);
    cout << "Sorted array: \n";
    printArray(arr, n);
    return 0;
}
```

```python
def selectionSort(array):
    n = len(array)

    for i in range(n):
        min = i
        for j in range(i+1, n):
            if array[min] > array[j]:
                min = j

        array[i], array[min] = array[min], array[i]

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    selectionSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
```

## Merge Sort

```cpp
#include <bits/stdc++.h>
using namespace std;
void merge(int array[], int const left, int const mid,
           int const right)
{
    int const subArrayOne = mid - left + 1;
    int const subArrayTwo = right - mid;

    auto *leftArray = new int[subArrayOne],
         *rightArray = new int[subArrayTwo];
]
    for (auto i = 0; i < subArrayOne; i++)
        leftArray[i] = array[left + i];
    for (auto j = 0; j < subArrayTwo; j++)
        rightArray[j] = array[mid + 1 + j];

    auto indexOfSubArrayOne = 0, indexOfSubArrayTwo = 0;
    int indexOfMergedArray = left;

    while (indexOfSubArrayOne < subArrayOne && indexOfSubArrayTwo < subArrayTwo)
    {
        if (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo])
        {
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
            indexOfSubArrayOne++;
        }
        else
        {
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
            indexOfSubArrayTwo++;
        }
        indexOfMergedArray++;
    }

    while (indexOfSubArrayOne < subArrayOne)
    {
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
        indexOfSubArrayOne++;
        indexOfMergedArray++;
    }

    while (indexOfSubArrayTwo < subArrayTwo)
    {
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
        indexOfSubArrayTwo++;
        indexOfMergedArray++;
    }
    delete[] leftArray;
    delete[] rightArray;
}

void mergeSort(int array[], int const begin, int const end)
{
    if (begin >= end)
        return;

    int mid = begin + (end - begin) / 2;
    mergeSort(array, begin, mid);
    mergeSort(array, mid + 1, end);
    merge(array, begin, mid, end);
}

void printArray(int A[], int size)
{
    for (int i = 0; i < size; i++)
        cout << A[i] << " ";
    cout << endl;
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr) / sizeof(arr[0]);

    cout << "Given array is \n";
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    cout << "\nSorted array is \n";
    printArray(arr, arr_size);
    return 0;
}
```

```python
def mergeSort(arr): 
    if len(arr) > 1:
        mid = len(arr)//2
 
        L = arr[:mid]
 
        R = arr[mid:]

        mergeSort(L)

        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
 
    mergeSort(arr)
 
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
```

# Quick Sort
```cpp
#include <bits/stdc++.h>
using namespace std;

int partition(int arr[],int low,int high)
{
//choose the pivot

int pivot=arr[high];
//Index of smaller element and Indicate
//the right position of pivot found so far
int i=(low-1);

for(int j=low;j<=high;j++)
{
	//If current element is smaller than the pivot
	if(arr[j]<pivot)
	{
	//Increment index of smaller element
	i++;
	swap(arr[i],arr[j]);
	}
}
swap(arr[i+1],arr[high]);
return (i+1);
}

// The Quicksort function Implement
			
void quickSort(int arr[],int low,int high)
{
// when low is less than high
	if(low<high)
	{	
		int pi=partition(arr,low,high);
		
		quickSort(arr,low,pi-1);
		quickSort(arr,pi+1,high);
	}
}
			

int main() {
int arr[]={10,7,8,9,1,5};
int n=sizeof(arr)/sizeof(arr[0]);
// Function call
quickSort(arr,0,n-1);
//Print the sorted array
cout<<"Sorted Array\n";
for(int i=0;i<n;i++)
{
	cout<<arr[i]<<" ";
}
return 0;
}
```

```python
def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low,high):
        if array[j] <= pivot:
            i += 1
            (array[i] , array[j]) =  (array[j] , array[i])

    (array[i + 1] , array[high]) = (array[high] , array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
 
    quickSort(arr , 0, len(arr) - 1)
 
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
```

```cpp

```

```python

```

```cpp

```

```python

```

```cpp

```

```python

```
