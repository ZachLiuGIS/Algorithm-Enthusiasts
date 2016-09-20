lst_1 = [[0] * 5] * 5
print(lst_1)

lst_1[0][0] = 1
print(lst_1)
# * create reference, so result is [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]

# this is the correct way
lst_2 = [[0] * 5 for i in range(5)]
print(lst_2)

lst_2[0][0] = 1
print(lst_2)
