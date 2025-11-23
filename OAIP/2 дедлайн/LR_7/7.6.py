def find_common_elements(list1: list, list2: list):
    set1 = set(list1)
    set2 = set(list2)
    common_set = set1 & set2  
    
    return list(common_set)

list1 = [1, 2, 3, 4, 5, 5]
list2 = [4, 5, 6, 7, 8, 5]
common = find_common_elements(list1, list2)
print(common)