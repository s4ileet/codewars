# There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_unique(arr):
    n = 0
    z = []
    while n < 2:
        z.append(arr[n])
        n += 1
    if z[0] != z[1] and z[0] == arr[-1]:
        return z[1]
    elif z[0] != z[1] and z[0] != arr[-1]:
        return z[0]
    else:
        for num in arr:
            if num not in z:
                return num
