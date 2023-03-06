import csv


def load_data(filePath):
    with open(filePath) as f:
        f_csv = csv.reader(f)
        heads = next(f_csv)
        data = []
        for row in f_csv:
            data.append(row)
    return heads, data
