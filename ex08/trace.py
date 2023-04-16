from matrix import Matrix

def trace(m: Matrix) -> float:
    if not m.is_square():
        print("trace: Square Matrix needed!")
        return
    return sum(m.data[i][i] for i in range(m.shape()[0]))

if __name__ == '__main__':
    import numpy as np
    
    u = Matrix([[-1., 6.],[3., 2.]])
    print(f"'[[-1., 6.],[3., 2.]]': custom trace: {trace(u)}")
    print(f"'[[-1., 6.],[3., 2.]]': numpy trace: {np.trace(u.data)}\n")

    u = Matrix([[1., 0.],[0., 1.]])
    print(f"'[[1., 0.],[0., 1.]]': custom trace: {trace(u)}")
    print(f"'[[1., 0.],[0., 1.]]': numpy trace: {np.trace(u.data)}\n")

    u = Matrix([[2., -5., 0.],[4., 3., 7.],[-2., 3., 4.]])
    print(f"'[[2., -5., 0.],[4., 3., 7.],[-2., 3., 4.]]': custom trace: {trace(u)}")
    print(f"'[[2., -5., 0.],[4., 3., 7.],[-2., 3., 4.]': numpy trace: {np.trace(u.data)}\n")

    u = Matrix([[-2., -8., 4.],[1., -23., 4.],[0., 6., 4.]])
    print(f"'[[2., -5., 0.],[4., 3., 7.],[0., 6., 4.]]': custom trace: {trace(u)}")
    print(f"'[[2., -5., 0.],[4., 3., 7.],[0., 6., 4.]]': numpy trace: {np.trace(u.data)}\n")
