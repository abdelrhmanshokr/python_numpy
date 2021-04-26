import numpy as np 

line = '*'
max_length = int(input('enter a value'))
tree_height = 0
print(max_length / 2)

while tree_height <= max_length / 2:
    print(line)
    print('from up top')
    line += '**'
    tree_height += 1

while tree_height != 0:
    line = line [:-2]
    tree_height -= 1
    print(line)
    print('from down below')


# python has its own built in code docs using Docstrings which goes as follows
# when the help function is called to your documented function it prints 
# you own documentation which is handy
"""One line describing what the code does

arguments:(a list of arguments in the code)

"""


