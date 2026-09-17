

def find_max(li,index):
    if index == 0:
        return li[0]
    else:
        max_val = find_max(li,index-1)
        if li[index] > max_val:
            max_val = li[index]
            
        return max_val
        

li = [3, 7, 2, 9, 5, 1]

print(find_max(li, len(li)-1))