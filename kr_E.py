N = int(input())
A = list(map(int, input().split(maxsplit=N)))
k = 0

for i in range(N):
    if 2*i+1 < len(A) and 2*i+2 < len(A) and (A[i] < A[2*i+1] or A[i] < A[2*i+2]):
        k += 1

if k > 0:
    print("NO")
else:
    print("YES")
