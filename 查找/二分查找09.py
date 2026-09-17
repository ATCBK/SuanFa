def binary_search(li,val):
    left = 0
    right = len(li)-1
    
    while left <= right:
        mid = (left + right)//2
        
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            left = mid +1
        else:
            right = mid -1
        return None
print(binary_search([1,2,3,4,5],3))