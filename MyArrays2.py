import numpy as np


grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# ROWS - grades for each student
# COLS - grades for each test
"""

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()


g = grades.mean(axis=0)  # mean by test       AXIS = 0 BY COL
print("Average of each test: ", g)


h = grades.mean(axis=1)  # mean by student    AXIS = 1 BY ROW
print("Average for each student: ", h)


numbers = np.array([1, 4, 9, 16, 25, 36])
sqrt = np.sqrt(numbers)
print(sqrt)


numbers2 = np.array((1, 7) * 10)
add = np.add(numbers, numbers2)
print(add)


multiply = np.multiply(numbers2, 5)
print(multiply)


numbers3 = numbers2.reshape(2, 3)
numbers4 = np.array([2, 4, 6])
multiply2 = np.multiply(numbers3, numbers4)
print(multiply2)


THis works b/c numbers4 has the same length as each row of numbers3, so NumPy can apply the multiply operation by treating numbers4 as if it were the following array:

array([[2,4,6], [2,4,6]])






#INDEXING & SLICING

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])


#to get just the grade 96
a = grades[0,1]
print(a)


#gives you a 1-D array
b = grades[1]
print(b)


#select multiple sequential rows            SLICING: remember it does NOT include the upper limit
firstTwo = grades[0:2]
print(firstTwo)



#select multiple NON sequential rows
someTwo = grades[[1,3]]
print(someTwo)



#all row but only 1st column                CONSECUTIVE = :         NONCCONSECUTIVE = ,
c = grades[:,0]
print(c)


#all row but only 1st & 2nd columns
d = grades[:2,0]
print(d)


#all rows & columns 0-2 consecutive         SLICING 
e = grades[:,1:3]
print(e)


#specific columns using a list of column indices
f = grades[:, [0,2]]
print(f)
"""

# USe NumPy random-number gen to create an array of 12 rando grades in the range 60-100, then reshape the result into a 3 x 4 array.
# Calculate avg all the grades, avg of grades for each test & avg of grade for each student

import random

grades = np.array([[random.randint(60, 100) for x in range(12)]])

grades2 = grades.reshape(3, 4)

avgAll = grades2.mean()

avgTest = grades2.mean(axis=0)

avgStudent = grades2.mean(axis=1)

print(grades)
print(grades2)
print(avgAll)
print(avgTest)
print(avgStudent)


# Correct version from Prof B
grades3 = np.random.randint(60, 101, 12).reshape(3, 4)

print(grades3.mean())

print(grades3.mean(axis=0))

print(grades3.mean(axis=1))


# Shallow copies(view)
# array method view returns a new array object w/ a view of the original array

numbers = np.arange(1, 6)
# array([1,2,3,4,5])

numbers2 = numbers.view()
# array([1,2,3,4,5])

numbers[1] *= 10
print(numbers2)
# array([1,20,3,4,5])


# similarly, chaingn a calue in the view also changes that value in the orginial array
numbers2[1] /= 10
print(numbers)


# SLICE VIEWS
# Slices also create views. Let's make numbers2 a slice that views only the first 3 elements of numbers:

numbers2 = numbers[0:3]


# to verify if it is a view, lets modify an element in the original array and see the view array
numbers[1] *= 20

print(numbers2)
# array([1, 40, 3])


# DEEP COPIES (copy)
# array method copy returns a new array object w/ a deep copy of the original array

numbers = np.arange(1, 6)
numbers2 = numbers.copy()


# to prove that numbers2 has a seperate copy of the data in numbers, let's modify an element in numbers,
# then display both arrays:
numbers *= 10

print(numbers)
# array([1,20,3,4,5])

print(numbers2)
# array([1,2,3,4,5])


"""The array methods reshape & resize both enable you to change an array's dimensions.
Method reshape returns a view(shallow copy) of the original array w/ the new dimensions.
It does not modify the original array."""

grades = np.array([[87, 96, 70], [100, 87, 90]])

a = grades.reshape(1, 6)
print(a)
# array([87, 96, 70, 100, 87, 90])


b = grades.resize(1, 6)
print(b)


# Method flatten deep copies the original array's data:
flattened = grades.flatten()


# method ravel produces a view (shallow copy) of the original array,
# which shares the grades array's data:

raveled = grades.ravel()


# confirm that they share the same data
raveled[0] = 100
raveled[6] = 99
print(raveled)


# since it is a view and they share the same data, we can look at grades to see
# that the 6th element has been updates
print(grades)


# You can quickly transpose an array's rows & columns that is "flip" the array,
# so the rows become the columns and the columns become the rows
# the T attribute returns a transposed view (shallow copy) of the array

transposed = grades.T

print(transposed)


grades = np.array([[87, 96, 70], [100, 87, 90]])
grades2 = np.array([[94, 77, 90], [100, 81, 82]])


# we can combine grades and grades2 w/ NumPy's hstack
h_grades = np.hstack((grades, grades2))


# new array
print(h_grades)


# old array is not affects
print(grades)


# VSTACK


# let's assume that grades2 represents 2 more students' grades on the 3 exams
v_grades = np.vstack((grades, grades2))
print(v_grades)