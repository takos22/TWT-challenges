# def matrixSum(m):
#     m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
#     t = 0
#     for i in m:
#         for j in i:
#             if not j: break
#             t += j
#     return t

matrixSum = lambda m:sum([sum(i[:(i.index(0)if 0 in i else len(i))])for i in[[m[j][i]for j in range(len(m))]for i in range(len(m[0]))]])

print(matrixSum([
    [1, 1, 1, 0],
    [0, 5, 0, 1],
    [2, 1, 3, 10]
]))
print(matrixSum([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]))
print(matrixSum([[0]]))
print(matrixSum([
    [1, 0, 3],
    [0, 2, 1],
    [1, 2, 0]
]))
