# Insert Sort Algorithm

def insertionSort2(n, arr):
    print("Input -->",arr)
    for i in range(1,n):
        toinsert = arr[i]
        for j in reversed(range(i)):
            if arr[j] > toinsert:
                arr[j+1] = arr[j]
                arr[j] = toinsert
    print("Sorted -->",arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

# Quick Sort Algorithm

-- Simple
def quicksort(arr):
    left,equal,right=[],[],[]
    key=arr[0]
    for i in range(len(arr)):
        if arr[i] < key:
            left.append(arr[i])
        elif arr[i] == key:
            equal.append(arr[i])
        else:
            right.append(arr[i])

    if len(left) > 1: quicksort(left)
    if len(right) > 1: quicksort(right)

    for i in range(len(left+equal+right)):
        arr[i] = (left+equal+right)[i]
    #print(*arr)

if __name__ == '__main__':
    n=input()
    arr=list(map(int,input().split()))
    print("Given:" , arr)
    quicksort(arr)
    print("Sorted:" , arr)
    
-- Advanced (Lomuto partition scheme)

def swap(arr,index1,index2):
    arr[index1],arr[index2]=arr[index2],arr[index1]

def quicksort_inplace(start,end):
    global arr
    if start < end:
        key,i=arr[end],start
        for j in range(start,end):
            if arr[j] < key:
                swap(arr,i,j)
                i += 1
        swap(arr,i,end)

        print(*arr)
        quicksort_inplace(start,i-1)
        quicksort_inplace(i+1,end)

n=int(input())
arr=list(map(int,input().split()))
quicksort_inplace(0,n-1)

# Merge Sort Algorithm

def mergesort(arr):
    if len(arr) > 1:
        mid=len(arr)//2

        L=arr[:mid]
        R=arr[mid:]
        mergesort(L)
        mergesort(R)

        i = j = k =0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1

        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1

n=7
a="38 27 43 3 9 82 10"
arr=list(map(int,a.split()))
print("Given:", arr)
mergesort(arr)
print("Sorted:", arr)
