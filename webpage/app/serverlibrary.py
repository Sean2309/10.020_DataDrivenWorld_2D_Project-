# put in any code you need for your server or backend
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from constants import *

df = None # dataframe shd be loaded here

def generate_univariate_graph(form):
    # Goal: Generate an image called graph.png in /assets
    var_type = form.var_type.data
    graph = form.graph.data
    var1 = form.var1.data
    var2 = form.var2.data

    plot = PLOTS_TO_FUNC.get(graph)
    plot(data=df, x=var1, order=cat_cols_order_dict[var1])





