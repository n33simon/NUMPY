#Read Evaluate Print Loop - REPL
#activate REPL in command palette to enter interactive mode
#caution, you annot save it in file, it is the interavtive mode

import numpy as np


integers = np.array([1,2,3])

print(type(integers))
print(integers)


#LIST COMPREHENSION
#create a 1 dimensional array from a list comprehension
#that produces even integers from 2 through 20


integers = np.array([x for x in range(2,21,2)])
print(integers)



integers = np.array([[1,2,3], [4,5,6]])
print(integers)



floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print(floats)