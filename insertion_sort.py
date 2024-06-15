n = int(input())
arr = list(map(int, input().split()))
length = len(arr)
for i in range(length):
    j = i
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -=1
print(arr)
