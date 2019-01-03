name = "Ted"
for character in name:
    print(character)


shows = ["GOT", "Narcos", "Vice"]
for show in shows:
    print(show)


people = {"Michael":"Dad","Janice":"Mom","David":"Brother","Ashley":"Sister"}
for relative in people:
    print(relative)


tv = ["GOT", "Narcos", "Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i = i + 1
print(tv)


# something I'm testing
import math
matrix1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix2 = [1, 2, 3, 2, 3, 2, 3, 2, 3]
i = 0
n = 0
# to multiply each corresponding index between matrix 1 and matrix 2
for x in matrix1:
    exp = x*matrix2[i]
    i = i + 1
    print(exp)


# to do each index in matrix1 with EVERY index in matrix2
matrix1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix2 = [1, 2, 3, 2, 3, 2, 3, 2, 3]
i = 0
n = 0
for x in matrix1:
    for y in matrix2:
        exp = x*y
        print(exp)


# to enter a number to be inserted in each index of matrix2 to be multiplied with corresponding indexes in matrix1
matrix1 = [1, 2, 3, 2, 3, 2, 3, 2, 3]
matrix2 = []
print(len(matrix1))
i = 0
n = input("enter number")
for x in matrix1:
    matrix2.insert(i, n)
    exp = x*matrix2[i]
    i = i + 1
    print(exp)


# to enter a new set of numbers (as a string) to be inserted in each index of matrix2 to be multiplied with
# corresponding indexes in matrix1
i = 0
p = []
matrix1 = [float(x) for x in input("enter string of numbers separated by commas for matrix1").split(",")]
matrix2 = [float(y) for y in input("enter string of numbers separated by commas for matrix2").split(",")]
for z in matrix1:
    n = matrix1[i]
    m = matrix2[i]
    w = n*m
    p.insert(i, w)
    i = i + 1
print(p)