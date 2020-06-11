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
