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
