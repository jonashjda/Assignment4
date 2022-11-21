import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='dat/series-01.csv', delimiter=',')

def groupedPlots(data):
    fig = plt.figure()
    for i in range(8):
        axes = fig.add_subplot(2, 4, i+1)
        plt.title(f"Row {i + 1}")
        axes.plot(data[i])

    plt.tight_layout()
    plt.savefig('figs/groupedplots.png')

def stackedPlots(data):
    plt.figure()
    for i in range(8):
        plt.plot(data[i + 1])
    plt.title("Stacked rows")
    plt.savefig('figs/stackedplots.png')

def main():
    groupedPlots(data)
    stackedPlots(data)

if __name__ == "__main__":
    main()