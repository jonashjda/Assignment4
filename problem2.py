import numpy as np
import matplotlib.pyplot as plt

series_01 = np.loadtxt(fname='dat/series-01.csv', delimiter=',')
series_02 = np.loadtxt(fname='dat/series-02.csv', delimiter=',')
series_03 = np.loadtxt(fname='dat/series-03.csv', delimiter=',')
series_04 = np.loadtxt(fname='dat/series-04.csv', delimiter=',')

def visualizer(series, filename, plotcolor, plotlinewidth, ylabel, xlabel, title):
    ave_value = np.mean(series, axis=0)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.plot(ave_value, color=plotcolor, linewidth=plotlinewidth)
    plt.savefig(f'figs/{filename}.png')
    plt.close()

def main():
    visualizer(series_01, 'Series 01 visualization2', 'red', 3, 'Y-axis', 'X-axis', 'Series 01')
    visualizer(series_02, 'Series 02 visualization2', 'blue', 4, 'Y-axis', 'X-axis', 'Series 02')
    visualizer(series_03, 'Series 03 visualization2', 'green', 5, 'Y-axis', 'X-axis', 'Series 03')
    visualizer(series_04, 'Series 04 visualization2', 'yellow', 5, 'Y-axis', 'X-axis', 'Series 04')

if __name__ == "__main__":
    main()