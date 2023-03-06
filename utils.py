def weakly_dominates(x, y, minimum=True):
    """
    Compute x dominated y or not
    :param y:
    :param x:
    :param minimum: maximize problem or minimize problem
    :return: True or False
    """
    if minimum:
        for i in range(len(x)):
            if x[i] > y[i]:
                return False
        return True
    else:
        for i in range(len(x)):
            if x[i] < y[i]:
                return False
        return True


def transData(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])
    return data

