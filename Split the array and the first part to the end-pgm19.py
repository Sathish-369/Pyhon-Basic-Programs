

def splitArry(arr, n ,k):
    for i in range(0, k):
        x= arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j+1]

        arr[n-1]= x

arr = [13, 24, 5, 67, 88, 99]
n =len(arr)
position = 2

splitArry(arr, n, position)

for i in range(0, n):
    print(arr[i], end = '')

