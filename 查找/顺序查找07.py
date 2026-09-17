def linear_search(data_set,value):
    for i in range(len(data_set)):
        if data_set[i] ==value:
            return i 
    return 
print(linear_search([1,2,3,4,5],3))