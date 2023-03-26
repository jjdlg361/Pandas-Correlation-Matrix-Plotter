import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_correlation_matrix(data):
    corr = data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(corr.values, cmap="YlGnBu")

    # Set x and y ticks
    ax.set_xticks(np.arange(len(corr.columns)))
    ax.set_yticks(np.arange(len(corr.columns)))
    ax.set_xticklabels(corr.columns)
    ax.set_yticklabels(corr.columns)

    # Rotate x tick labels
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Add colorbar
    cbar = ax.figure.colorbar(im, ax=ax)

    # Set title and show plot
    ax.set_title("Correlation Matrix")
    plt.show()

# Example usage
data = pd.read_csv("data.csv")
plot_correlation_matrix(data)
