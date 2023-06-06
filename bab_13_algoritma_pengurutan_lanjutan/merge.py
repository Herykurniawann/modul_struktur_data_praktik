def merge(list1,list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    while i < len(list1):
        combined.append(list1[i])
        i += 1
        
    while j < len(list2):
        combined.append(list2[j])
        j += 1
        
    return combined

print(merge([1,2,7,8],[3,4,5,6]))