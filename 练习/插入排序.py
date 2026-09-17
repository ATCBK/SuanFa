


def charu_paixu(li):
    for i in range(len(li)):
        temp = li[i]  #存放当前的值
        j = i - 1 #为该值前面的值放置下标
        while j >= 0 and li[j]>temp: #开始循环从后一位和当前指向开始比较
            li[j+1] = li[j] #当前位置和前面的一致，进行替换，temp存了当前最小的值，当while条件不满足时插入
            j -= 1 #开始继续向后排序
            
        li[j+1] = temp#当上述条件不满足时将temp插入空出来的位置
    
            
        