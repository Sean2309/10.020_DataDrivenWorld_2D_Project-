# put in any code you need for your server or backend
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from constants import *

df = pd.read_csv("././Datasets/Processed/All_DF_Processed_with_Cat_Cols.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)
print(df.head())

def rotate_axis(
    fig,
) -> bool:
    """
    Dynamic rotation of x axis labels
    """
    num_labels = len(fig.get_xticklabels())
    if num_labels >= 6:
        return True
    else:
        return False

# save_fig: Saving the generated plot into a destination folder
def save_fig(
    fig,
    dest_path,
    file_name
):
    locs, labels = plt.xticks()
    if rotate_axis(fig):
        plt.setp(labels,rotation=45, horizontalalignment="right")
    else:
        plt.setp(labels, horizontalalignment="right")

    plt.savefig(os.path.join(dest_path, file_name), dpi=300, bbox_inches="tight")
    plt.close()

def generate_univariate_graph(form):
    # Goal: Generate an image called graph.png in /assets
    var_type = form.var_type.data
    graph = form.graph.data
    var1 = form.var1.data
    var2 = form.var2.data

    plot = PLOTS_TO_FUNC.get(graph)
    fig = plot(data=df, x=var1, order=cat_cols_order_dict.get(var1))
    save_fig(fig, "./assets", "graph.png")

var_type= "univariate",
graph= "Hist",
var1= 'Life_Expectancy'

plot = PLOTS_TO_FUNC.get(graph)
fig = plot(data=df, x=var1, order=cat_cols_order_dict.get(var1))
save_fig(fig, "./assets", "graph.png")





