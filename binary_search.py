def binary_search(arr, first, last, target):
    middle = (first + last)//2
    
    if(first == last and target != arr[middle]):
        print('Entered element is not present')
    elif(target == arr[middle]):
        print('Entered element found!!')
    elif(target < arr[middle]):
        binary_search(arr, first, middle-1, target)
    else:
        binary_search(arr, middle+1, last, target)

n = int(input('Enter the number of elements : '))
print('Enter n elements : ')

arr=[]

for i in range(0,n):
    num = int(input())
    arr.append(num)
    
for i in range(1,n):
    num1 = arr[i]
    j = i - 1
    
    while(j>=0 and num1<arr[j]):
        arr[j+1] = arr[j]
        j = j-1
    
    arr[j+1] = num1

tgt = int(input('Enter the element to be found : '))

binary_search(arr, 0, n-1, tgt)