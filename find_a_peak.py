def my_max(col):
    x = 0
    m = col[0]
    for n in range(1,len(col)):
        if col[n] > m:
            x = n
            m = col[x]
    return x

def two_d_peak(a: list[list[int]]):
    if len(a) <= 1:
        if len(a) == 0:
            return "baka... "
        else:
            new = my_max(a[0])
            return new, a[0][new]

    m = len(a[0])

    if m <= 3:
        if m == 3:
            j = 1
        elif m == 2:
            column_one = [row[0] for row in a]
            column_two = [row[1] for row in a]
            one = my_max(column_one)
            two = my_max(column_two)
            print(one, two)
            print(a)
            if a[one][0] > a[two][1]:
                return a[one][0]
            else:
                return a[two][1]
        elif m == 1:
            new = [row[0] for row in a]
            one = my_max(new)
            return a[one]
        else:
            return "Baka!... you uh.. it cant be an empty list baka, but its not like a care or anything..."

    else: j = m//2 #a middle column
    print(a)
    i = [row[j] for row in a]
    i = my_max(i) #global max on row

    if a[i][j-1] > a[i][j]:
        new = [row[:j] for row in a]
        return two_d_peak(new)
    if a[i][j+1] > a[i][j]:
        new = [row[j:] for row in a]
        return two_d_peak(new)
    else:
        return a[i][j]

if __name__ == "__main__":
    a = [
    [0,1,2,3,4,5,6,7,8],
    [17,16,15,14,13,12,11,10,9],
    [18,19,20,21,22,23,24,25,26],
    [35,34,33,32,31,30,29,28,27],
    [36,37,38,39,40,41,42,43,44],
    [42,999,49,48,47,46,45,44],
    ]
    b = [
    [1],
    [2],
    [3],
    [4],
    ]
    print(two_d_peak(b))
