import csv
from matplotlib import pyplot as plt
import pandas as pd
from pymop import ZDT1
from pymop.factory import get_problem

from data_Utils import *
from draw_Utils import drawBook
from metric_Utils import *
from utils import transData


def main():
    path = '/Users/dayiyi/Documents/Code/MOEAD框架/results/2023-03-05 ZDT DE:rand:1:bin/ZDT4(0).csv'
    name = 'DTLZ1(0).csv'
    _, dataA = load_data(path)
    for i in range(len(dataA)):
        dataA[i] = dataA[i][10:]
    dataA = transData(dataA)

    pf = get_problem("zdt1").pareto_front()
    pf = get_problem("zdt1").pareto_front(n_pareto_points=10)

    midwest = pd.read_csv('/Users/dayiyi/Documents/Code/MOEAD框架/results/2023-03-05 ZDT DE:rand:1:bin/ZDT4(0).csv')
    categories = np.unique(midwest['F1'])

    db = drawBook()
    db.draw(dataA)
    db.show()


if __name__ == '__main__':
    main()
