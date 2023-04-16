from matrix import Matrix

def transpose(m) -> 'Matrix':
    num_rows, num_cols = m.shape()
    return [[m.data[j][i] for j in range(num_rows)] for i in range(num_cols)]

if __name__ == "__main__":
    import numpy as np
    
    u = Matrix([[1, 0], [0, 1]])
    print(f"\n[[1, 0], [0, 1]]: custom transpose: {transpose(u)}")
    print(f"[[1, 0], [0, 1]]: numpy transpose: {np.array(u.data).T.tolist()}")

    u = Matrix([[1, 2], [3, 4]])
    print(f"\n[[1, 2], [3, 4]]: custom transpose: {transpose(u)}")
    print(f"[[1, 2], [3, 4]]: numpy transpose: {np.array(u.data).T.tolist()}")

    u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(f"\n[[1, 0, 0], [0, 1, 0], [0, 0, 1]]: custom transpose: {transpose(u)}")
    print(f"[[1, 0, 0], [0, 1, 0], [0, 0, 1]]: numpy transpose: {np.array(u.data).T.tolist()}")
  
    u = Matrix([[1, 2], [3, 4], [5, 6]])
    print(f"\n[[1, 2], [3, 4], [5, 6]]: custom transpose: {transpose(u)}")
    print(f"[[1, 2], [3, 4], [5, 6]]: numpy transpose: {np.array(u.data).T.tolist()}")
