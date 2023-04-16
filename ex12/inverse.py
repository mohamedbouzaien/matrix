from matrix import Matrix

def inverse(m: Matrix) -> Matrix:
    n = len(m.data)
    inv = Matrix(col=n, row=n)
    for i in range(n):
        inv.data[i][i] = 1

    for i in range(n):
        if m.data[i][i] == 0:
            for j in range(i + 1, n):
                if m.data[j][i] != 0:
                    m.data[i], m.data[j] = m.data[j], m.data[i]
                    inv.data[i], inv.data[j] = inv.data[j], inv.data[i]
                    break
            else:
                print("inverse: Matrix is singular!")
                return

        pivot = m.data[i][i]
        for j in range(n):
            m.data[i][j] /= pivot
            inv.data[i][j] /= pivot

        for j in range(n):
            if j == i:
                continue
            factor = m.data[j][i]
            for k in range(n):
                m.data[j][k] -= factor * m.data[i][k]
                inv.data[j][k] -= factor * inv.data[i][k]
    return inv

if __name__ == '__main__':
    import numpy as np
    
    u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    U = np.linalg.inv(u.data)
    print(f"\n[[1, 0, 0], [0, 1, 0], [0, 0, 1]]: custom inverse: {inverse(u).data}")
    print(f"[[1, 0, 0], [0, 1, 0], [0, 0, 1]]: numpy inv: {U.dot(u.data).tolist()}")

    u = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
    U = np.linalg.inv(u.data)
    print(f"\n[[2, 0, 0], [0, 2, 0], [0, 0, 2]]: custom inverse: {inverse(u).data}")
    print(f"[[2, 0, 0], [0, 2, 0], [0, 0, 2]]: numpy inv: {U.dot(u.data).tolist()}")

    u = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
    U = np.linalg.inv(u.data)
    print(f"\n[[8, 5, -2], [4, 7, 20], [7, 6, 1]]: custom inverse: {inverse(u).data}")
    print(f"[[8, 5, -2], [4, 7, 20], [7, 6, 1]]: numpy inv: {U.dot(u.data).tolist()}")
