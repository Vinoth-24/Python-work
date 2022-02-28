N = 15
count = 0
for i in range(N):
    print(" " * (N - count) +"*" * (2*count + 1))
    count += 1
count = count -1
for i in range (N):
    print(" " * (N-count) + "*" * (2*count + 1))
    count -= 1

