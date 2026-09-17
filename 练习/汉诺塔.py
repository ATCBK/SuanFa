

def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,b,c)
        print("移动%d到%d",a,c)
        hanoi(n-1,b,a,c)

hanoi(3,"A","B","c")
        
    