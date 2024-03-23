def bubble(list):
    indexing_lenght = len(list)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0,indexing_lenght):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]


    return list

print(bubble([4,5,6,3,5,2,6,7,8,9]))