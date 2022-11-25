list = [-99, 100, -88, 70, 180, -40]

def sort_list (list):
    sorted= True

    while (sorted):
        sorted= False 
        for g in range (len(list)):
           for j in range (len(list) -1):
            if list [j] > list[j+1]:
                list [j], list [j+1] = list [j+1], list [j] 
                sorted = True
sort_list(list)
print(list)
