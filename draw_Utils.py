import matplotlib.pyplot as plt


class drawBook:
    def __init__(self):
        self.fig = None
        self.large = 22
        self.med = 16
        self.small = 12
        params = {'axes.titlesize': self.large,
                  'legend.fontsize': self.med,
                  'figure.figsize': (16, 10),
                  'axes.labelsize': self.med,
                  'xtick.labelsize': self.med,
                  'ytick.labelsize': self.med,
                  'figure.titlesize': self.large}
        plt.rcParams.update(params)
        plt.style.use('ggplot')

    def draw(self, data, title='figure'):
        # Draw Plot for Each Category
        self.fig = plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
        for i, data_ in enumerate(data):
            plt.scatter(data_[1], data_[0], s=20)
        # Decorations
        plt.gca().set(xlim=(0.0, 1), ylim=(0.0, 1), xlabel='F1', ylabel='F2')
        plt.xticks(fontsize=self.small)
        plt.yticks(fontsize=self.small)
        plt.title(title, fontsize=self.large)

    def show(self):
        plt.show()

    def clean(self):
        self.fig.clf()


