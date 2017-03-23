from math import ceil

def arraysort(a):
    len = a.__len__()
    if len < 2:
        return a
    if len == 2:
        if a[0] < a[1]:
            return a
        else:
            temp = a[0]
            a[0] = a[1]
            a[1] = temp
            return a
    else:
        mid = ceil(len/2)
        left = arraysort(a[0:mid])
        right = arraysort(a[mid:len])
        return(mergesorted(left, right))

def mergesorted(left, right):
    left_len = left.__len__()
    right_len = right.__len__()
    merged = [0] * (left_len + right_len)
    i=0; j=0; k=0
    while i<(left_len+right_len):
        if j >= left_len:
            merged[i:] = right[k:]
            break
        elif k >= right_len:
            merged[i:] = left[j:]
            break
        elif left[j] < right[k]:
            merged[i] = left[j]
            j = j+1
        else:
            merged[i] = right[k]
            k = k+1
        i = i+1
    return merged

test_array = [3,0,24,-9,1,35,-8,-7,1,0,45,2]
print("unsorted test array: ", test_array)
print("->sorted test array: ", arraysort(test_array))
