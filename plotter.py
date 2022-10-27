import matplotlib.pyplot as plt
import pandas as pd
import data_processor as dpr


def main():
    # read in data
    iris = pd.read_csv('iris.data',  header=None)
    iris.columns = ['sepal_width', 'sepal_length', 'petal_width',
                    'petal_length', 'species']
    measurement_names = ['sepal_width', 'sepal_length',
                         'petal_width', 'petal_length']

    # set up subplots
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, axes = plt.subplots(1, 2)

    # make box plot
    ax1.boxplot(iris[measurement_names], labels=measurement_names)
    ax1.set_ylabel('cm')
    fig1.savefig('iris_boxplot.png')

    # make scatter plot
    for species in set(iris['species']):
        iris_subset = iris[iris['species'] == species]
        scatter_plot = ax2.scatter(iris_subset['petal_length'],
                                   iris_subset['petal_width'],
                                   label=species, s=15)

        ax2.legend()
        ax2.set_xlabel('petal_length')
        ax2.set_ylabel('petal_width')
        fig2.savefig('petal_length_v_width_scatter')

    # make multi panel plot
    # left box plot
    axes[0].boxplot(iris[measurement_names], labels=measurement_names)
    axes[0].set_ylabel('cm')

    # right scatter plot
    for species in set(iris['species']):
        iris_subset = iris[iris['species'] == species]
        scatter_plot = axes[1].scatter(iris_subset['petal_length'],
                                       iris_subset['petal_width'],
                                       label=species, s=15)

    axes[1].legend()
    axes[1].set_xlabel('petal_length')
    axes[1].set_ylabel('petal_width')

    # save multi panel
    for i in range(1):
        axes[i].spines['top'].set_visible(False)
        axes[i].spines['right'].set_visible(False)

    fig3.savefig('multi_panel_figure.png')


if __name__ == '__main__':
    main()
