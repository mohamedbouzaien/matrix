from matrix import Matrix, Vector
def mul_vec(a: Matrix, u: Vector) -> Vector:
    if a.shape()[1] != u.shape():
        print("mul_vec: shape error!")
        return
    result = [0.0] * a.shape()[0]
    for i in range(a.shape()[0]):
        for j in range(a.shape()[1]):
            result[i] += a.data[i][j] * u.data[j]
    return Vector(result)

def mul_mat(a: Matrix, b: Matrix) -> Matrix:
    if a.shape()[1] != b.shape()[0]:
        print("mul_vec: shape error!")
        return
    result = Matrix(col=b.shape()[1], row=a.shape()[0])
    for i in range(a.shape()[0]):
        for j in range(b.shape()[1]):
            for k in range(a.shape()[1]):
                result.data[i][j] += a.data[i][k] * b.data[k][j]
    return result

if __name__ == '__main__':
    import numpy as np
    
    print("----------------------- Vector -----------------------------\n")
    
    u = Matrix([[1., 0.], [0., 1.]])
    v = Vector([4., 2.])
    print(f"'[[1., 0.], [0., 1.]]' and '[4., 2.]': custom mul_vec: {mul_vec(u, v).data}")
    print(f"'[[1., 0.], [0., 1.]]' and '[4., 2.]': numpy multiply: {np.array(u.data) @ np.array(v.data)}\n")
    
    u = Matrix([[2., 0.], [0., 2.]])
    v = Vector([4., 2.])
    print(f"'[[2., 0.], [0., 2.]]' and '[4., 2.]': custom mul_vec: {mul_vec(u, v).data}")
    print(f"'[[2., 0.], [0., 2.]]' and '[4., 2.]': numpy multiply: {np.array(u.data) @ np.array(v.data)}\n")
    
    u = Matrix([[2., -2.], [-2., 2.]])
    v = Vector([4., 2.])
    print(f"'[[2., -2.], [-2., 2.]]' and '[4., 2.]': custom mul_vec: {mul_vec(u, v).data}")
    print(f"'[[2., -2.], [-2., 2.]]' and '[4., 2.]': numpy multiply: {np.array(u.data) @ np.array(v.data)}\n")
    
    u = Matrix([[2., 0.], [0., 2.]])
    v = Vector([4., 2.])
    print(f"'[[2., 0.], [0., 2.]]' and '[4., 2.]': custom mul_vec: {mul_vec(u, v).data}")
    print(f"'[[2., 0.], [0., 2.]]' and '[4., 2.]': numpy multiply: {np.array(u.data) @ np.array(v.data)}\n")
    
    print("----------------------- Matrix -----------------------------\n")
    
    u = Matrix([[1., 0.], [0., 1.]])
    v = Matrix([[1., 0.], [0., 1.]])
    print(f"'[[1., 0.], [0., 1.]]' and '[[1., 0.], [0., 1.]]': custom mul_mat: {mul_mat(u, v).data}")
    print(f"'[[1., 0.], [0., 1.]]' and '[[1., 0.], [0., 1.]]': numpy matmul: {np.matmul(np.array(u.data), np.array(v.data))}\n")

    u = Matrix([[1., 0.], [0., 1.]])
    v = Matrix([[2., 1.], [4., 2.]])
    print(f"'[[1., 0.], [0., 1.]]' and '[[2., 1.], [4., 2.]]': custom mul_mat: {mul_mat(u, v).data}")
    print(f"'[[1., 0.], [0., 1.]]' and '[[2., 1.], [4., 2.]]': numpy matmul: {np.matmul(np.array(u.data), np.array(v.data))}\n")

    u = Matrix([[3., -5.], [6., 8.]])
    v = Matrix([[2., 1.], [4., 2.]])
    print(f"'[[3., -5.], [6., 8.]]' and '[[2., 1.], [4., 2.]]': custom mul_mat: {mul_mat(u, v).data}")
    print(f"'[[3., -5.], [6., 8.]]' and '[[2., 1.], [4., 2.]]': numpy matmul: {np.matmul(np.array(u.data), np.array(v.data))}\n")
