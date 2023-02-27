def selectionSort(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i+1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex] , array[i]


arr = [2,3,9,1,34,-1,-18,-2,-15,0]
selectionSort(arr)
print(arr)
