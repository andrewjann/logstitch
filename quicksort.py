def quicksort(arr,low,high):
    if (low < high):
        pIndex = partition(arr,low,high)
        quicksort(arr,low,pIndex-1)
        quicksort(arr,pIndex+1,high)

def partition(arr,low,high):
    pVal = arr[low]
    pInd = low
    for i in range(low+1,high+1):
        if arr[i] > pVal:
            pInd += 1
            arr[i], arr[pInd] = arr[pInd], arr[i]
    arr[low], arr[pInd] = arr[pInd], arr[low]
    return pInd
