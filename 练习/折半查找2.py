
def zheban_chazhao(li,aim):
    left = 0
    right = len(li)-1
    while left < right:
        mid = (left+right)//2
        if li[mid] == aim:
            return mid
        elif li[mid] < aim:
            left += 1
        else:
            right -=1
        return -1

li = [1,2,3,4,5,6]
print(li[zheban_chazhao(li,3)])