

def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i-1
        while j>=0 and tmp < li[j]:#找插入的位置
            li[j+1] = li[j]
            j -= 1 #控制j的位置，依次减小排序
        li[j+1] = tmp