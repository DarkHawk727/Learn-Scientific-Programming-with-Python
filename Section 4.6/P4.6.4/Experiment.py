import sys
import numpy as np
import matplotlib.pyplot as plt

class Experiment():
    def __init__(self, description):
        self.description = description

        self.x = np.array([])
        self.y = np.array([])

        self.m = None
        self.c = None


    def load_data(self, filepath):
        try:
            with open(filepath, 'r') as data:
                x, y = [], []
                for line in data.readlines()[1:]:
                    try:
                        x.append(float(line.split()[0]))
                        y.append(float(line.split()[1]))
                    except (IndexError, ValueError):
                        print('Invalid Data!')
                        sys.exit(1)
        except FileNotFoundError:
            print('File not found!')
            sys.exit(1)

        self.x = np.array(x)
        self.y = np.array(y)

    
    def set_data(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)

    
    def fit_line(self, func_x = lambda x: x, func_y = lambda y: y):
        self.tx = func_x(self.x)
        self.ty = func_y(self.y)

        t_x_bar = np.mean(self.tx)
        t_y_bar = np.mean(self.ty)

        t_x2_bar = np.mean(self.tx ** 2)
        t_x_y_bar = np.mean(self.tx * self.ty)

        self.m = (t_x_y_bar - t_x_bar*t_y_bar) / (t_x2_bar - t_y_bar**2)
        self.c = t_y_bar - self.m * t_x_bar

        t_y2_bar = np.mean(self.ty ** 2)
        r_2 = (t_x_y_bar - t_x_bar*t_y_bar)**2 / (t_x2_bar - t_x_bar**2) / (t_y2_bar - t_y_bar ** 2)

        return self.m, self.c, r_2


    def plot_data(self, best_fit=False, fig_filename=None):
        if best_fit:    
            if self.c is None or self.m is None:
                self.fit_line()
            plt.scatter(self.tx, self.ty)
            x_fit = np.array([min(self.tx), max(self.ty)])
            y_fit = self.m * x_fit + self.c
            plt.plot(x_fit, y_fit, 'k', lw=2)
        else:
            plt.scatter(self.x, self.y)
        
        if fig_filename:
            plt.savefig(fig_filename)
        else:
            plt.show()