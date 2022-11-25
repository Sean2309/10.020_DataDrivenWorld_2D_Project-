# put in any code you need for your server or backend
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from .constants import *

df = pd.read_csv("dataset.csv")
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
    var_x = form.var_x.data # e.g Prevalence_of_undernourishment
    var_hue = form.var_hue.data # e.g Corruption_Perception_Index
    var_year = form.var_year.data # 2019

    plot = PLOTS_TO_FUNC.get(graph)
    if var_hue:
        plot(data=df, x=f"{var_x}_{var_year}_Cat", hue=f"{var_hue}_{var_year}_Cat",order=cat_cols_order_dict[var_x], hue_order=cat_cols_order_dict[var_hue])
    else:
        plot(data=df, x=f"{var_x}_{var_year}_Cat", order=cat_cols_order_dict[var_x])

def generate_bivariate_graph(form):
    var_type = form.var_type.data
    graph = form.graph.data
    var_x = form.var_x.data # e.g Prevalence_of_undernourishment
    var_hue = form.var_hue.data # .g Corruption_Perception_Index
    var_y = form.var_y.data # e.g Life_Expectancy
    var_year = form.var_year.data # Year e.g 2020

    plot = PLOTS_TO_FUNC.get(graph)
    plot(data=df, x=f"{var_x}_{var_year}_Cat", y=f"{var_y}_{var_year}", hue=f"{var_hue}_{var_year}_Cat", order=cat_cols_order_dict[var_x], hue_order=cat_cols_order_dict[var_hue])




