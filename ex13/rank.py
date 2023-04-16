from matrix import Matrix

def rank(matrix: Matrix) -> int:
    m = Matrix(data=[row.copy() for row in matrix.data])
    n, _ = m.shape()
    rank = 0
    col = 0
    for row in range(n):
        if col >= len(m.data[row]):
            break
        pivot = row
        while m.data[pivot][col] == 0:
            pivot += 1
            if pivot == n:
                pivot = row
                col += 1
                if col == len(m.data[row]):
                    break
        if col < len(m.data[row]):
            m.data[pivot], m.data[row] = m.data[row], m.data[pivot]
            pivot_value = m.data[row][col]
            m.data[row] = [val / pivot_value for val in m.data[row]]
            for i in range(n):
                if i != row:
                    factor = m.data[i][col]
                    for j in range(col + 1, len(m.data[row])):
                        m.data[i][j] -= factor * m.data[row][j]
                    m.data[i][col] = 0.0
            col += 1
            rank += 1
    return rank

if __name__ == '__main__':
    import numpy as np
    
    u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(f"\n[[1, 0, 0], [0, 1, 0], [0, 0, 1]]: custom rank: {rank(u)}")
    print(f"[[1, 0, 0], [0, 1, 0], [0, 0, 1]]: numpy matrix_rank: {np.linalg.matrix_rank(u.data)}")

    u = Matrix([[1, 2, 0, 0], [2, 4, 0, 0], [-1, 2, 1, 1]])
    print(f"\n[[1, 2, 0, 0, 0], [2, 4, 0, 0], [-1, 2, 1, 1]]: custom rank: {rank(u)}")
    print(f"[[1, 2, 0, 0, 0], [2, 4, 0, 0], [-1, 2, 1, 1]]: numpy inv: {np.linalg.matrix_rank(u.data)}")

    u = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
    print(f"\n[[8, 5, -2], [4, 7, 20], [7, 6, 1]]: custom rank: {rank(u)}")
    print(f"[[8, 5, -2], [4, 7, 20], [7, 6, 1]]: numpy inv: {np.linalg.matrix_rank(u.data)}")
