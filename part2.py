# PART 2
# Lesson 4: Data Analysis Process - Case Study 1

# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
# red wine data
wine_red = pd.read_csv('data/winequality-red.csv', sep = ';')
wine_red.info()

# shape(row, column)
print(wine_red.shape)

# duplicated
print("duplicated:", sum(wine_red.duplicated()))

# unique value in one column
print(wine_red['quality'].unique())

# mean of column
print(wine_red['density'].mean())

# load data
# white wine data
wine_white = pd.read_csv('data/winequality-white.csv', sep = ';')
wine_white.info()

# shape(row, column)
print(wine_white.shape)

# duplicated
print("duplicated:", sum(wine_white.duplicated()))

# unique value in one column
print(wine_white['quality'].unique())

# appending data
# combine the red and white wine datasets
# 컬럼을 하나 만들어서, 컬러 값을 추가한다.
# red wine
color_red = np.repeat('red', 1599)
color_white = np.repeat('white', 4898)

# add datasets
wine_red['color'] = color_red
wine_white['color'] = color_white

# confirm
print(wine_red.head())
print(wine_white.head())

# combine dataframe
wine_df = wine_red.append(wine_white, ignore_index =True)
print(wine_df.head())

# save as dataset
wine_df.to_csv('data/winequality_edited.csv', index = False)
print(wine_df.shape)
print(wine_df.info())

# x, y variable
x = sorted(wine_df['quality'].unique())
y = wine_df.groupby('quality')['alcohol'].mean()

# bar chart
#plt.bar(x, y)
#plt.show()

# scatter plot
#plt.scatter(wine_df['quality'], wine_df['fixed acidity'])
#plt.show()

# 14. Pandas Query
# load data
df = pd.read_csv('data/winequality_edited.csv')
print(df.info())

# row count
print(df.shape[0])

# by alcohol content
print(df['alcohol'].median())

# using query
low_alcohol = df.query('alcohol < 10.3')
high_alcohol = df.query('alcohol >= 10.3')

# check samples
num_samples = df.shape[0]
print(num_samples == low_alcohol['quality'].count() + high_alcohol['quality'].count())

# low_alcohol quality mean
print(low_alcohol['quality'].mean())
print(high_alcohol['quality'].mean())

