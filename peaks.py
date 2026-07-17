a = [
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8],
]


def twoD_peak(a):
    height, width = len(a)-1, len(a[0])
    print(width)
    mid_h, mid_w = height//2, width//2
    print(mid_w)
    true_mid = a[mid_h][mid_w]
    print(true_mid)

    if true_mid < a[mid_h][mid_w - 1]:
        a = [a[:mid_w+1] for _ in a]
        return twoD_peak(a)
    elif true_mid < a[mid_h][mid_w + 1]:
        a = [a[:mid_w+1] for _ in a]
        return twoD_peak(a)

    
    return

twoD_peak(a)

def recur_array(a):
    print(a)
    if len(a) == 0:
        return "empty list"
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return max(a[0], a[1])
    
    mid = len(a)//2
    #if the # on the left of mid is larger than the mid, than only work with left side.
    if a[mid] < a[mid-1]:
        return recur_array(a[:mid-1])
    elif a[mid] < a[mid+1]:
        return recur_array(a[mid+1:])
    else:
        return mid
