import heapq

A = []

N = int(input())
A = list(map(int, input().split()))[:N]

heapq.heapify(A)
print(A)
