from os import name
import numpy as np 

# line = '*'
# max_length = int(input('enter a value'))
# tree_height = 0
# print(max_length / 2)

# while tree_height <= max_length / 2:
#     print(line)
#     print('from up top')
#     line += '**'
#     tree_height += 1

# while tree_height != 0:
#     line = line [:-2]
#     tree_height -= 1
#     print(line)
#     print('from down below')


# python has its own built in code docs using Docstrings which goes as follows
# when the help function is called to your documented function it prints 
# your own documentation which is handy
"""One line describing what the code does

arguments:(a list of arguments in the code)

"""

'''
numerical computing with Numpy
numpy is a library that helps us work with numberical data in python
it much easier to work with numpy instead of using python 
it's faster and easier to use as it's implemented inernally using C++
notice that all elements in a mumpy array should have the same data type 
and we can check its type using .dtype
'''

# import numpy as np
# import urllib.request

# urllib.request.urlretrieve(
#     'https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv',
#     'climate.txt'
# )

# climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
# # print(climate_data.shape)

# weights = np.array([0.3, 0.2, 0.5])
# yields = climate_data @ weights
# print(yields)
# print(yields.shape)

# # we can add yields to climate_data as a forth column and save it as new array climate_results
# climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)
# print(climate_results)

# # now let's save it as a txt file let's save the climate_results
# np.savetxt(
#     'climate_results.txt',
#     climate_results,
#     fmt='%.2f',
#     delimiter=',',
#     header='temperature, rainfall, humidity, yield_apples',
#     comments=''
# )

# # arithmatic operations over np arrays 
# # print(np.random.rand(2, 3))


# lesson 3 a 100 numpy exercises
# import numpy as np
# print(np.__version__)

# null_vector = np.zeros(12)
# print(null_vector)
# print('{} size in memory'.format(null_vector.size * null_vector.itemsize))

# help(print)

# create a null vector with some value
# null_vector_2 = np.zeros(10)
# null_vector_2[4] = 1
# print(null_vector_2)

# create a vector with a range 
# range_vector = np.arange(10, 50, 1, dtype=None)
# print(range_vector)

# reverse order on a vector
# print(range_vector[:: -1])

# create 3*3 matrix ranging from 0 to 8
# count = 0
# three_by_three_matrix = np.zeros((3, 3))
# for i in range(3):
#     for j in range(3):
#         three_by_three_matrix[i][j] = count
#         count += 1

# print(three_by_three_matrix)

# or with another easier method using numpy
# three_by_three_matrix_from_0_to_8 = np.arange(9).reshape((3, 3))
# print(three_by_three_matrix_from_0_to_8)

# Find indices of non-zero elements from [1,2,0,0,4,0]
# wanted_array = [1,2,0,0,4,0]
# for i in wanted_array:
#     if i != 0:
#         print('index of a non-zero element is {}'.format(wanted_array.index(i   )))
#         print('value of a non-zero element is {}'.format(i))


# Create a 3x3 identity matrix 
# identity_matrix = np.identity(3)
# print(identity_matrix)


# Create a 3x3x3 array with random values
# random_values_matrix = np.arange(27).reshape((3, 3, 3))
# for i in range(3):
#     for j in range(3):
#         for z in range(3):
#             random_values_matrix[i][j][z] = np.random.randint(100)  

# print(random_values_matrix)


# Create a 10x10 array with random values and find the minimum and maximum values
# random_values_matrix = np.random.randint(0, 10, size=(10, 10), dtype=int)
# print('random values matrix', random_values_matrix)
# min_item = random_values_matrix[0, 0]
# max_item = random_values_matrix[0, 0]
# print('first item', min_item)
# for i in range(10):
#     print('i', i)
#     for j in range(10):
#         print('j', j)
#         print('current item', random_values_matrix[i, j])
#         if random_values_matrix[i, j] < min_item:
#             min_item = random_values_matrix
#             print('new min', min_item)
#         elif random_values_matrix[i, j] > max_item:
#             max_item = random_values_matrix[i, j]
#             print('new max', max_item)

# print('min item', min_item)
# print('max item', max_item)


# Create a random vector of size 30 and find the mean value
# random_vector = np.random.randint(0, 30, size=(30, 1), dtype=int)
# # mean = total sum / length
# array_length = random_vector.shape[0]
# total_sum = np.sum(random_vector)
# mean = total_sum / array_length
# print('mean', mean)


# Create a 2d array with 1 on the border and 0 inside
# all_ones_array_size = (4, 4)
# all_ones_array = np.ones(all_ones_array_size)
# for i in range(all_ones_array.shape[0]):
#     for j in range(all_ones_array.shape[1]):
        # if i > 0 and i < all_ones_array.shape[0] - 1 and j > 0 and j < all_ones_array.shape[1] - 1:
        #     all_ones_array[i][j] = 0
# print(all_ones_array)


# How to add a border (filled with 0's) around an existing array?
# random_values_matrix = np.random.randint(0, 10, size=(2, 5), dtype=int)
# random_values_matrix_shape_of_x = random_values_matrix.shape[0] + 2
# random_values_matrix_shape_of_y = random_values_matrix.shape[1] + 2

# all_zeros_array_size = (random_values_matrix_shape_of_x, random_values_matrix_shape_of_y)
# all_zeros_array = np.zeros(all_zeros_array_size)
# # print(random_values_matrix) 

# for i in range(all_zeros_array.shape[0]):
#     for j in range(all_zeros_array.shape[1]):
#         if i > 0 and i < all_zeros_array.shape[0] - 1 and j > 0 and j < all_zeros_array.shape[1] - 1:
#             all_zeros_array[i][j] = random_values_matrix[i - 1][j - 1]

# print(all_zeros_array)


# Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
# five_by_5_array = np.random.randint(0, 22, size=(5, 5), dtype=int)
# wanted_numbers_arary = [1, 2, 3, 4]
# for i in range(five_by_5_array.shape[0]):
#         for j in range(five_by_5_array.shape[1]):
#                 if i == j + 1:
#                         five_by_5_array[i][j] = wanted_numbers_arary[j]
# print(five_by_5_array)


# Create a 8x8 matrix and fill it with a checkerboard pattern
# checkboard_size = (8, 8) 
# checkerboard = np.zeros(checkboard_size)
# for i in range(checkerboard.shape[0]):
#         for j in range(checkerboard.shape[1]):
#                 if (i + j) % 2 != 0:
#                         checkerboard[i][j] = 1
# print(checkerboard)


# Normalize a 5x5 random matrix
# random_array = np.random.randint(0, 20, size=(5, 5), dtype=int)
# print(random_array)

# pandas 
from urllib.request import urlretrieve 
import pandas as pd 


italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'
urlretrieve(italy_covid_url, 'italy-covid.csv')

covid_df = pd.read_csv('italy-covid.csv')
print(type(covid_df))
print(covid_df.info())
print(covid_df.describe())
print(covid_df.shape)
print(covid_df.columns)


# retirieving data from a data frame 
print(covid_df.new_cases)
print(covid_df[['date', 'new_cases']])
print(covid_df.at[24, 'new_cases'])
# to access one row 
print(covid_df.loc[200])


# analyzing data from a data frame 
# total number of cases and deaths
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()
print('total cases', total_cases)
print('total deaths', total_deaths)


# querying and sorting data 
# high_new_cases = covid_df.new_cases > 1000
# print('high new cases', covid_df[high_new_cases])
# this is the same as
high_new_cases = covid_df[covid_df.new_cases > 1000] 
print('high new cases', high_new_cases)


# working with dates 
print(covid_df['date'])
# it's an object type so pandas has no idea it's a date 
# so we need to convert it into a date first to deal with it as such
covid_df['date'] = pd.to_datetime(covid_df.date)
print(covid_df.date)
# now it's a datetime format 
# as it's in format we can extract various details
# like adding a new row like year or month like so
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
print(covid_df)


# grouping and aggregation
# summarize data month wise
# covid_month_df = covid_df.groupby('month')[]


# trying sort_values in another file
laborex_file = pd.read_excel('laborex.xlsx')
grouped_new_file = laborex_file.sort_values(['name', 'price'], axis=0, inplace=False)
print(laborex_file)
print('new grouped file', grouped_new_file.first)
# grouped_new_file.describe()
# grouped_new_file.to_excel(r'new grouped file.xlsx', index=False)


# Data visualization with matplotlib and seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# line chart 
years = [2011, 2012, 2013, 2014, 2015, 2016]
yield_apples = [1, 2.25, 6.245, 7.142, 5.200, 6.635]
yield_oranges = [5, 7.25, 4.22, 8.142, 6.200, 12.635]
# label x_axis and y_label
plt.xlabel('years')
plt.ylabel('yield')
# chart title and legend
plt.title('apples and oranges yield chart')
plt.legend(['apples', 'oranges'])
# plotting a new chart plt.plot(x_axis, y_axis)
# marker argument is used to add marking to the chart
plt.plot(years, yield_apples, marker='o')
plt.plot(years, yield_oranges, marker='x')
plt.savefig('data visualizaiton.png')



# # trying SQLtie that ships with python
# import sqlite3

# # create a connection to the DB
# connection = sqlite3.connect('client.DB')
