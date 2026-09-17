
def heapify(arr,n,i):
    largest = 1
    left = 2*i+1
    right = 2*i+2
    
    if right < n and arr[largest] < arr[left]:
        largest = left
        
    if left <n and arr[largest] < arr[left]:
        largest = right
        
    if largest != i:
        arr[i],arr[right] = arr[largest],arr[i]
        
        heapify(arr,n,largest)
        

def heap_sort(arr):
    n = len(arr)
    
    print("原始数组", arr)
    
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
        
    print("建立大根堆",arr)
    
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        
        print("最大值放到最后" ,arr)
        
        heapify(arr,i,0)
        print("重新调整后: ",arr)
        print("--------------")
        
arr = [4, 1, 7, 3, 8, 5]

heap_sort(arr)

print("最终结果：", arr)