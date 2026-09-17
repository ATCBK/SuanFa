
def partition(li,right,left):
    tmp = li[left]
    while left <right:
        while left < right and li[right]>=tmp:#确保中间有数，开始查找右边比temp小的数字
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    
