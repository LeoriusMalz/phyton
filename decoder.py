with open("input.txt", "r") as inf:
    s = list(inf.readline() + ".")

i, k = 0, 0
while s[i] != '.':
    if not('a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z'):
        k += 1
        if ('a' <= s[i+1] <= 'z' or 'A' <= s[i+1] <= 'Z' or s[i+1] == '.'):
            if k > 1:
                s[i] = int(''.join(s[i-k+1:i+1]))
                del s[i-k+1:i]
                i = i - k + 1
            else:
                s[i] = int(s[i])
    else:
        k = 0
    i += 1

for i in range(0,len(s)-2,2):
    print(s[i] * s[i+1], end='')
