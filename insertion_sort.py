n = int(input('Enter the size of the array : '))
arr = []

print('Enter the n elements : ')

for i in range(0,n):
    num = int(input())
    arr.append(num)

print(arr)
    
for i in range(1,n):
    num1 = arr[i]
    j = i - 1
    
    while(j>=0 and num1<arr[j]):
        arr[j+1] = arr[j]
        j = j-1
    
    arr[j+1] = num1

print('Sorted array : ',arr)