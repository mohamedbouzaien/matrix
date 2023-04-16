from matrix import Matrix

def determinant(matrix: Matrix) -> float:
    if not matrix.is_square():
        print("determinant: non square matrix!")
        return
    rows, cols = matrix.shape()
    if rows == 1:
        return matrix.data[0][0]
    elif rows == 2:
        return matrix.data[0][0] * matrix.data[1][1] - matrix.data[0][1] * matrix.data[1][0]
    elif rows == 3:
        return (
            matrix.data[0][0] * matrix.data[1][1] * matrix.data[2][2]
            + matrix.data[0][1] * matrix.data[1][2] * matrix.data[2][0]
            + matrix.data[0][2] * matrix.data[1][0] * matrix.data[2][1]
            - matrix.data[0][2] * matrix.data[1][1] * matrix.data[2][0]
            - matrix.data[0][1] * matrix.data[1][0] * matrix.data[2][2]
            - matrix.data[0][0] * matrix.data[1][2] * matrix.data[2][1]
        )
    elif rows == 4:
        result = 0
        for i in range(4):
            minor_matrix_data = [[matrix.data[row][col] for col in range(cols) if col != i]
                for row in range(1, rows)]
            result += matrix.data[0][i] * determinant(Matrix(minor_matrix_data)) * (-1) ** i
        return result
    else:
        print("determinant: unsupported dimension!")
        return

if __name__ == "__main__":
    import numpy as np

    u = Matrix([[1, -1], [-1, 1]])
    print(f"\n[[1, -1], [-1, 1]]: custom determinent: {determinant(u)}")
    print(f"[[1, -1], [-1, 1]]: numpy det: {np.round(np.linalg.det(u.data))}")

    u = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
    print(f"\n[[2, 0, 0], [0, 2, 0], [0, 0, 2]]: custom determinent: {determinant(u)}")
    print(f"[[2, 0, 0], [0, 2, 0], [0, 0, 2]]: numpy det: {np.round(np.linalg.det(u.data))}")

    u = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
    print(f"\n[[8, 5, -2], [4, 7, 20], [7, 6, 1]]: custom determinent: {determinant(u)}")
    print(f"[[8, 5, -2], [4, 7, 20], [7, 6, 1]]: numpy det: {np.round(np.linalg.det(u.data))}")

    u = Matrix([[8, 5, -2, 4], [4, 2.5, 20, 4.], [8., 5., 1., 4.], [28., -4., 17., 1.]])
    print(f"\n[[8, 5, -2], [4, 7, 20], [7, 6, 1]]: custom determinent: {determinant(u)}")
    print(f"[[8, 5, -2], [4, 7, 20], [7, 6, 1]]: numpy det: {np.round(np.linalg.det(u.data))}")
