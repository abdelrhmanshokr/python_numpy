# import numpy as np 

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
# you own documentation which is handy
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

import numpy as np
import urllib.request

urllib.request.urlretrieve(
    'https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv',
    'climate.txt'
)

climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
# print(climate_data.shape)

weights = np.array([0.3, 0.2, 0.5])
yields = climate_data @ weights
print(yields)
print(yields.shape)

# we can add yields to climate_data as a forth column and save it as new array climate_results
climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)
print(climate_results)

# now let's save it as a txt file let's save the climate_results
np.savetxt(
    'climate_results.txt',
    climate_results,
    fmt='%.2f',
    delimiter=',',
    header='temperature, rainfall,humidity, yield_apples',
    comments=''
)

