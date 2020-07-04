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
