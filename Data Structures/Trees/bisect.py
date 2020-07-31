Problem: https://www.hackerrank.com/challenges/median/problem

import math
import bisect


def print_median(f):
    mid = math.floor(len(f) / 2)
    if len(f) % 2 == 0:
        val=sum(f[mid-1:mid+1]) / 2
        print("{:.0f}".format(val) if val.is_integer() else val)
    else:
        print(f[mid])

def median(op, x):
    if op == "a":
        bisect.insort(f,x)
        print_median(f)
    else:
        position = bisect.bisect_left(f, x)
        if (position >= len(f) or f[position] != x):
            print("Wrong!")
        else:
            del f[position]
            print("Wrong!") if len(f) == 0 else print_median(f)


N = int(input())
f = []
for i in range(0, N):
    a,num = input().strip().split(' ')
    median(a, int(num))
