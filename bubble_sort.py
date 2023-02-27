def bubbleSort(array):
    swapped = False
    for i in range(len(array)-1):
        print(i)
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
        if swapped == False:
            break

arr = [2,3,9,1,34,-1,-18,-2,-15,0]
bubbleSort(arr)
print(arr)