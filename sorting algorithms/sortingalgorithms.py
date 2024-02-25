# Bubble Sort
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


 