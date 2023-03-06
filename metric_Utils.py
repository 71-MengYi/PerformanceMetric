from functools import reduce

import numpy as np

from utils import weakly_dominates


def InvertedGenerationalDistance(PF, X):
    """
    D-metric
    反世代距离评价指标(Inverted Generational Distance, IGD) 是一个综合性能评价指标。
    它主要通过计算每个在真实 Pareto前沿面上的点(个体)到算法获取的个体集合之间的最小距离和，来评价算法的收敛性能和分布性能。
    值越小，算法的综合性能包括收敛性和分布性能越好。
    :param PF: 均匀分布在真实 Pareto 面上的点集
    :param X: 算法获取的最优 Pareto 最优解集
    :return: Inverted Generational Distance
    """
    def d(p):
        minimum = np.Inf
        for i in range(len(X)):
            temp = np.sum(np.sqrt((np.array(p) - np.array(X[i])) ** 2))
            minimum = min(minimum, temp)
        return minimum
    sum_d = 0
    for Pi in PF:
        sum_d += d(Pi)
    return sum_d / len(PF)


def C_metric(A, B, minimum=True):
    """
    cover-metric
    衡量A支配B的解所占比例
    :param A:
    :param B:
    :param minimum:
    :return:
    """
    count = 0
    # TODO 解决AB数量不相等的问题
    for i in range(len(A)):
        if weakly_dominates(A[i], B[i], minimum):
            count += 1
    return count / len(A)


def HV(reference_point):
    def calculate_hyper_volume(front):
        def volume(individualF):
            hyper_cuboid_sides = []
            for i in range(len(reference_point)):
                side_length = abs(individualF[i] - reference_point[i])
                hyper_cuboid_sides.append(side_length)
            return reduce(lambda x, y: x*y, hyper_cuboid_sides, 1)

        sum_ = 0
        for i in range(len(front)):
            sum_ += volume(front[i])
        return sum_ / len(front)
    return calculate_hyper_volume

