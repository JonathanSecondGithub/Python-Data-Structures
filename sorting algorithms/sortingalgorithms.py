#Bubble Sort
def mergeSort(array): 
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


 