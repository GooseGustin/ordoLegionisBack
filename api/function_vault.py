
def removeDuplicates(arr): 
    arr_copy = arr.copy()
    for i in arr_copy: 
        if arr_copy.count(i) > 1:
            arr_copy.remove(i)
    return arr_copy