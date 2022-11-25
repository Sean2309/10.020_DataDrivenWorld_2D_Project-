
import seaborn as sns
options = {
    "var_types": [
        "univariate",
        "bivariate"
    ],
    "graphs": [
    "Hist",
    "KDE",
    "Ecdf",
    "Bar",
    "Scatter",
    "Violin",
    "Line"
    ],
    "vars": ['Life_Expectancy', 'Mean_Years_Of_Schooling', 'CPI_Food',
       'Net_FDI', 'Infant_Mortality_Rate', 'Unemployment',
       'Access_To_Electricity', 'Fertility_Rate',
       'Immunization_Measles', 'Labor_Force_Gender_Ratio',
       'Corruption_Perception_Index', 'Prevalence_of_undernourishment'],
    "years": ["2016", "2017", "2018", "2019", "2020"]
}

PLOTS_TO_FUNC = {
    "Hist": sns.histplot,
    "KDE": sns.kdeplot,
    "Ecdf": sns.ecdfplot,
    "Bar": sns.barplot,
    "Scatter": sns.scatterplot,
    "Violin": sns.violinplot,
    "Line": sns.lineplot
}

cat_cols_order_dict = {
    "Prevalence_of_undernourishment": ["0-20", "20-40","40-60","60-80","80-100"],
    "Life_Expectancy": ["50-60","60-70","70-80","80-90"],
    "Mean_Years_Of_Schooling": ["0 to 5", "5 to 10","10 to 15"],
    "CPI_Food": ["0-200", "200-400","400-600","600-800","800-1000", ">1000"],
    "Net_FDI": ["(-155000)-(-100000)","(-100000)-(-50000)","(-50000)-0","0-50000", "50000-100000"],
    "Infant_Mortality_Rate": ["0-20", "20-40","40-60","60-80","80-100", "100-120", "120-140"],
    "Unemployment": ["0 to 5", "5 to 10","10 to 15","15 to 20","20 to 25","25 to 30"],
    "Access_To_Electricity": ["0-20", "20-40","40-60","60-80","80-100"],
    "Fertility_Rate": ["0 to 1", "1 to 2","2 to 3","3 to 4","4 to 5","5 to 6","6 to 7"],
    "Immunization_Measles": ["0-20", "20-40","40-60","60-80","80-100"],
    "Labor_Force_Gender_Ratio": ["0-20", "20-40","40-60","60-80","80-100", "100-120"],
    "Corruption_Perception_Index": ["0-20", "20-40","40-60","60-80","80-100"]
}
