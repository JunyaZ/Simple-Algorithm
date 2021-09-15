

A=[1,2,3,3,4,0,4,4,0,0,0,4,4,5]
# 1. remove the duplication from a sorted array, duplicates only appear twice
def dedup(arr):
    i=0
    while (i<len(arr)-1):
        if arr[i]!=arr[i+1]:
            i+=1
        else:
           arr.remove(arr[i])
           i+=1
    return len(arr)
# 2. remove duplication from a sorted array, duplicates appear more than twice.
def dedup2(arr):
    pointer=0
    for i in range(len(arr)):
        if arr[pointer]!=arr[i]:
            pointer+=1
            arr[pointer]=arr[i]
    return pointer+1
# 3. Move Zeros
def moveZeros(arr):
    for i in arr:
        if i==0:
            arr.remove(i)
            arr.append(i)
    return arr

def moveZeroes2(nums):
    left=0
    right=0
    while right<len(nums):
        if nums[right]==0:
            right+=1
        else:
            nums[left],nums[right]=nums[right],nums[left] #swap the numbers
            left+=1
            right+=1
# 3. reverse words in string
s='i want to go home'
def reverse(arr):
    arr=arr.split(' ')
    left=0
    right=len(arr)-1
    while (left<right):
        arr[left],arr[right]=arr[right],arr[left]
        print(arr)
        left+=1
        right-=1
# 3.reverse the arrary
def reversearr(arr):
    left=0
    right=len(arr)-1
    while (left<right):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
B=[3,4,5,6,7,8,8,9,0]
reversearr(B)
print(B)

# 4. reverse a interger
C=2345
def reverseInt(INT):
    rev=0
    p=INT
    while(p!=0):
        mod=p % 10
        p=p//10
        rev=rev*10+mod
    return rev

print(reverseInt(C))

# 5. Rotate a array of elements to the right by k steps
examples=[1,4,5,4,3,26,7]
# n=7,k=3
# rotate to [5,6,7,1,2,3,4]
# 4321 765 --> 5671234

def rotatearr1(arr,k):
    p1=arr[:-k]
    p2=arr[-k:]
    return p2+p1



def reversearrCut(arr,left,right):
    while (left<right):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

def rotatearr2(arr,k):
    end_indx=len(arr)-1
    if k >len(arr):
        return arr
    else:
        reversearrCut(arr,0,end_indx-k)
        reversearrCut(arr,end_indx-k+1,end_indx)
        reversearrCut(arr,0,end_indx)


rotatearr2(examples,20)
print(examples)          
# 4.bubble sort
def bubblesort(arr):
    end_indx=len(arr)-1
    for i in range(end_indx):
        for j in range(end_indx-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

# 4. mergesort
print("Before",examples)
bubblesort(examples)
print("after",examples)