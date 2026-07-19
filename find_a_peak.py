array1 = [0,1,2,3,4,12,6,7,8]

def straightforward_method(a) -> int | None:
    n=0
    for _ in range(len(array1)-1):
        #if possition n is >= possition n+1 than return n
        if a[n] >= a[n+1]:
            return n
        else:
            n += 1
    return -1

def divide_method(a) -> int:
    #base case
    print(a)
    if len(a) <= 2:
        if len(a) == 0:
            return None
        if len(a) == 1:
            return a[0]
        if a[0] > a[1]:
            return a[0]
        else:
            return a[1]
    #recursion
    mid = len(a)//2
    if a[mid] < a[mid - 1]:
        return divide_method(a[:mid])
    elif a[mid] < a[mid + 1]:
        return divide_method(a[mid + 1:])
    else: 
        return a[mid]



if __name__ == "__main__":
    #print(f"the first peak is numbner {array1[straightforward_method(array1)]} in possition {straightforward_method(array1)}")
    print(f"a peak in array1 holds the value", divide_method(array1))