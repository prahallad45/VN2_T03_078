"""
# convert list/tuple/set to list/tuple/set

CRUD - retrieve
data - list,tuple, set
state - input data
Behaviour - convert into
"""
# convert list to tuple, set


def convert():
    result = tuple(x)
    return result


x = [1, 5, "mani"]
print("After converting list to tuple:", convert())


def convert():
    result = set(y)
    return result


y = [96, "jani", 45]
print("After converting list to set:", convert())


# convert tuple to list, set


def convert():
    result = list(a)
    return result


a = (1, 8, 12)
print("After converting tuple to list:", convert())


def convert():
    result = set(b)
    return result


b = ("karna", "bar", 12)
print("After converting tuple to set:", convert())


