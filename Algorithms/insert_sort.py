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
