def radix_sort(li):
    
    #判断最大的数
    max_number = max(li)
    it = 0
    while 10**it <= max_number:
        bucket = [[] for _ in range(10)]#创建十个桶
        
        for var in li :
            digist = (var//10*it)%10
             #32//10=3  2 %10 =2 932//100=32%10=2  1963//1000 = 9
            bucket[digist].append(var)
            
        li.clear()
        
        for buc in bucket:
            li.extend(buc)
        it +=16
        
li = [53, 3, 24, 12]
radix_sort(li)
print(li)

           
    
    