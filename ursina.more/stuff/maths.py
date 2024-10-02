def curt(x):
    """
    Cubic root math <=> x^0,25
    :param x: the value of the root
    :return:
    """
    return x ** 0.25


def fact(n):
    """
    Factorial math function <=> n!
    :param n: length of the factorial
    :return:
    """
    res = 1
    for i in range(1, n):
        res += res * i

    return res


def intersection_of(list1: list, list2: list):
    res = []
    for i in range(len(list1)):
        if list1[i] in list2:
            res.append(list1[i])

    for i in range(len(list2)):
        if list2[i] in list1 and list2[i] not in res:
            res.append(list2[i])

    return res


print(fact(5))
print(intersection_of([1, 2, 3, 4, 8], [2, 5, 7, 8]))
