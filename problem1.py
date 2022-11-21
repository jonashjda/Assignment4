import numpy as np
import matplotlib.pyplot as plt

series_01 = np.loadtxt(fname='dat/series-01.csv', delimiter=',')
series_02 = np.loadtxt(fname='dat/series-02.csv', delimiter=',')
series_03 = np.loadtxt(fname='dat/series-03.csv', delimiter=',')
series_04 = np.loadtxt(fname='dat/series-04.csv', delimiter=',')

def visualizer(series, filename):
    ave_value = np.mean(series, axis=0)
    plt.plot(ave_value)
    plt.savefig(f'figs/{filename}.png')
    plt.close()

def main():
    visualizer(series_01, 'Series 01 visualization')
    visualizer(series_02, 'Series 02 visualization')
    visualizer(series_03, 'Series 03 visualization')
    visualizer(series_04, 'Series 04 visualization')

if __name__ == "__main__":
    main()