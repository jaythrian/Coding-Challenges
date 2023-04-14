"""
You are given an array (which will have a length of at least 3,
but could be very large) containing integers. The array is
either entirely comprised of odd integers or entirely comprised
of even integers except for a single integer N. Write a method
that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)

"""


def outlier(arr):
    oddArr = []
    evenArr = []
    for i in arr:
        if i % 2 == 0:
            evenArr.append(i)
        else:
            oddArr.append(i)

    if len(oddArr) == 1:
        return oddArr[0]
    else:
        return evenArr[0]


arr = [2, 4, 0, 100, 11, 4, 2602, 36]

a = outlier(arr)
print(a)
