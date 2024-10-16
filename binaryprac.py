def binary_search(arr,item):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        guess=arr[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None

print(binary_search([1,2,3,4,5,6,9],9))#returns the index position of the second arguement
