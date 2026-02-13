# x = multiplicera talen
# antal tal = n
# formel = x ^ 1/n


def geomean(list):
    x = 1
    n = 0
    for num in list:
        x = x * num
        n = n + 1

    mean = x ** (1 / n)
    print(mean)


geomean([1, 2, 3, 10])
