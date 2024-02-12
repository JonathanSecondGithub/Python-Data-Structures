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
