podpiski = set()
subs = set()

N = int(input())
for i in range(N):
    podpiski.add(str(input()))

M = int(input())
for i in range(M):
    subs.add(str(input()))
    
friend = podpiski.intersection(subs)
poklon = subs - friend
kumir = podpiski - friend

print(len(friend), len(poklon), len(kumir))
