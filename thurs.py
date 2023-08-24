def partition (param):
    if param % 2 == 0:
        return (param,None)
    else:
        return (None,param)


print(partition(20))