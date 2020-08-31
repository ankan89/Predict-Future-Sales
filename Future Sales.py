import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data1 = pd.read_csv("/Users/Ankan/Desktop/DataScience/GitHub/Predict-Future-Sales/item_categories.csv")
data2 = pd.read_csv("/Users/Ankan/Desktop/DataScience/GitHub/Predict-Future-Sales/items.csv")
data3 = pd.read_csv("/Users/Ankan/Desktop/DataScience/GitHub/Predict-Future-Sales/sales_train.csv")
data4 = pd.read_csv("/Users/Ankan/Desktop/DataScience/GitHub/Predict-Future-Sales/sample_submission.csv")
data5 = pd.read_csv("/Users/Ankan/Desktop/DataScience/GitHub/Predict-Future-Sales/shops.csv")
data6 = pd.read_csv("/Users/Ankan/Desktop/DataScience/GitHub/Predict-Future-Sales/test.csv")

# read csv data
df1 = data1
df2 = data2

Right1_join = pd.merge(df1,df2,on='item_category_id',how='right')

# read csv data
df3 = Right1_join
df4 = data3

Right2_join = pd.merge(df3,df4,on='item_id',how='right')

# read csv data
df5 = Right2_join
df6 = data6

Right3_join = pd.merge(df5,df6,on='item_id',how='right')

print(Right3_join.info())

# # read csv data
# df7 = Right3_join
# df8 = data6
#
# Right4_join = pd.merge(df7,df8,on='item_id',how='right')
#
# print(Right4_join.info())
#
# # read csv data
# df9 = Right4_join
# df10 = data6
#
# Right5_join = pd.merge(df9,df10,on='item_id',how='right')
#
# print(Right5_join.info())





