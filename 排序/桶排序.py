

def radix_sort(li):
    max_num = max(li)
    it = 0
    while 10**it <= max_num:
        buckets = [[] for _ in range(10)]
        
        for var in li :
            
            digit = (var // 10**it)%10
            buckets[digit].append(var)
        li.clear()
        
        for buc in buckets:
            li.extend(buc)
            
        it += 1
        #循环重新建立桶

li = [53, 3, 24, 12]
radix_sort(li)

        
            
        