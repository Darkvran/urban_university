def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
    return matrix


func_res = get_matrix(10, 10, '*')
print(func_res)