import pandas as pd
import statistics
import csv
df=pd.read_csv("StudentsPerformance.csv")
height_list=df["math score"].to_list()
weight_list=df["writing score"].to_list()
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)
height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)
print("mean/median/mode of the math score is {}, {} and {} respectivly".format(height_mean,height_median,height_mode))
print("mean/median/mode of the writing score is {}, {} and {} respectivly".format(weight_mean,weight_median,weight_mode))