from typing import List, Tuple

class Vector():
    def __init__(self, data: List[float]):
        self.data = data

    def shape(self) -> int:
        return len(self.data)

    def print_vector(self):
        print(self.data)

    def reshape_to_vector(self, new_shape: int) -> 'Vector':
        rows = self.shape()
        new_rows, new_cols = new_shape
        if rows != new_rows * new_cols:
            print("reshape_to_vector: Dimensions error!")
            return
        reshaped_vector = []
        start = 0
        for _ in range(new_rows):
            row = self.data[start:start+new_cols]
            reshaped_vector.append(row)
            start += new_cols
        return Vector(reshaped_vector)
    
    def add(self, v: 'Vector') -> None:
        if self.shape() != v.shape():
            print("add: different shapes!")
            return
        self.data = [self.data[i] + v.data[i] for i in range(self.shape())]

    def sub(self, v: 'Vector') -> None:
        if self.shape() != v.shape():
            print("sub: different shapes.")
            return
        self.data = [self.data[i] - v.data[i] for i in range(self.shape())]

    def scl(self, a: float) -> None:
        self.data = [a * x for x in self.data]

class Matrix():
    def __init__(self, data: List[List[float]] = None, col: int = None, row: int = None):
        if data is not None:
            self.data = data
        elif col is not None and row is not None:
            self.data = [[0.0] * col for _ in range(row)]
        else:
            print("Matrix init: missing attribute!")
            return

    def shape(self) -> Tuple[int, int]:
        num_rows = len(self.data)
        num_cols = len(self.data[0]) if num_rows > 0 else 0
        return (num_rows, num_cols)

    def is_square(self) -> bool:
        num_rows, num_cols = self.shape()
        return num_rows == num_cols

    def print_matrix(self):
        print(self.data) 

    def reshape_to_matrix(self, new_shape: int) -> 'Matrix':
        rows, cols = self.shape()
        new_rows, new_cols = new_shape
        if rows * cols != new_rows * new_cols:
            print("reshape_to_matrix: Dimensions error!")
            return
        flat_matrix = [elem for row in self.data for elem in row]
        reshaped_matrix = []
        start = 0
        for _ in range(new_rows):
            row = flat_matrix[start:start+new_cols]
            reshaped_matrix.append(row)
            start += new_cols
        return Matrix(reshaped_matrix)

    def add(self, m: 'Matrix') -> None:
        if self.shape() != m.shape():
            print("add: different shapes!")
            return
        self.data = [[self.data[i][j] + m.data[i][j] for j in range(self.shape()[1])] for i in range(self.shape()[0])]

    def sub(self, m: 'Matrix') -> None:
        if self.shape() != m.shape():
            print("sub: different shapes!")
            return
        self.data = [[self.data[i][j] - m.data[i][j] for j in range(self.shape()[1])] for i in range(self.shape()[0])]

    def scl(self, a: float) -> None:
        self.data = [[a * x for x in row] for row in self.data]

if __name__ == '__main__':
    import numpy as np
    
    print("----------------------- Vector -----------------------------\n")
    
    u = Vector([2, 3])
    v = Vector([5, 7])
    U = u.data
    u.add(v)
    print(f"[2, 3]' and '[5, 7]': custom add: {u.data}")
    print(f"[2, 3]' and '[5, 7]': numpy add: {np.add(U, v.data)}\n")

    u = Vector([1, 1])
    v = Vector([1, 1])
    U = u.data
    u.add(v)  
    print(f"[1, 1]' and '[1, 1]': custom add: {u.data}")
    print(f"[1, 1]' and '[1, 1]': numpy add: {np.add(U, v.data)}\n")

    u = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    v = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) 
    U = u.data
    u.add(v)
    print(f"'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' and '[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]': custom add: {u.data}")
    print(f"'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' and '[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]': numpy add: {np.add(U, v.data)}\n")

    u = Vector([2, 3])
    v = Vector([5, 7])
    U = u.data
    u.add(v)
    print(f"[2, 3]' and '[5, 7]': custom add: {u.data}")
    print(f"[2, 3]' and '[5, 7]': numpy add: {np.add(U, v.data)}\n")

    u = Vector([1, 1])
    v = Vector([1, 1])
    U = u.data
    u.add(v)  
    print(f"[1, 1]' and '[1, 1]': custom add: {u.data}")
    print(f"[1, 1]' and '[1, 1]': numpy add: {np.add(U, v.data)}\n")

    u = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    v = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) 
    U = u.data
    u.add(v)
    print(f"'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' and '[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]': custom add: {u.data}")
    print(f"'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' and '[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]': numpy add: {np.add(U, v.data)}\n")

    u = Vector([2, 3])
    v = Vector([5, 7])
    U = u.data
    u.sub(v)
    print(f"[2, 3]' and '[5, 7]': custom sub: {u.data}")
    print(f"[2, 3]' and '[5, 7]': numpy sub: {np.subtract(U, v.data)}\n")

    u = Vector([1, 1])
    v = Vector([1, 1])
    U = u.data
    u.sub(v)  
    print(f"[1, 1]' and '[1, 1]': custom sub: {u.data}")
    print(f"[1, 1]' and '[1, 1]': numpy sub: {np.subtract(U, v.data)}\n")

    u = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    v = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) 
    U = u.data
    u.sub(v)
    print(f"'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' and '[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]': custom sub: {u.data}")
    print(f"'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' and '[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]': numpy sub: {np.subtract(U, v.data)}\n")

    u = Vector([2, 3])
    p = 2.
    U = u.data
    u.scl(p)
    print(f"[2, 3]' and '2.': custom scl: {u.data}")
    print(f"[2, 3]' and '2.': numpy multiply: {np.multiply(U, p)}\n")

    u = Vector([1, 1])
    p = -3.
    U = u.data
    u.scl(p)  
    print(f"[1, 1]' and '-3: custom scl: {u.data}")
    print(f"[1, 1]' and '-3: numpy multiply: {np.multiply(U, p)}\n")

    u = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    p = 42.
    U = u.data
    u.scl(p)
    print(f"'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' and '42.': custom scl: {u.data}")
    print(f"'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' and '42': numpy sub: {np.multiply(U, p)}\n")
    
    print("----------------------- Matrix -----------------------------\n")
     
    u = Matrix([[1., 2.], [3., 4.]])
    v = Matrix([[7., 4.], [-2., 2.]])
    U = u.data
    u.add(v)
    print(f"'[[1., 2.], [3., 4.]]' and '[[7., 4.], [-2., 2.]]': custom add: {u.data}")
    print(f"'[[1., 2.], [3., 4.]]' and '[[7., 4.], [-2., 2.]]': numpy add: {str(np.add(U, v.data).tolist())}\n")
    
    u = Matrix([[42, 42], [-42, 12]])
    v = Matrix([[42, 42], [-42, 12]])
    U = u.data
    u.add(v)
    print(f"'[[42, 42], [-42, 12]]' and '[[42, 42], [-42, 12]]': custom add: {u.data}")
    print(f"'[[42, 42], [-42, 12]]' and '[[42, 42], [-42, 12]]': numpy add: {str(np.add(U, v.data).tolist())}\n")

    u = Matrix([[1., 2.], [3., 4.]])
    v = Matrix([[7., 4.], [-2., 2.]])
    U = u.data
    u.sub(v)
    print(f"'[[1., 2.], [3., 4.]]' and '[[7., 4.], [-2., 2.]]': custom sub: {u.data}")
    print(f"'[[1., 2.], [3., 4.]]' and '[[7., 4.], [-2., 2.]]': numpy sub: {str(np.subtract(U, v.data).tolist())}\n")
    
    u = Matrix([[42, 42], [-42, 12]])
    v = Matrix([[42, 42], [-42, 12]])
    U = u.data
    u.sub(v)
    print(f"'[[42, 42], [-42, 12]]' and '[[42, 42], [-42, 12]]': custom sub: {u.data}")
    print(f"'[[42, 42], [-42, 12]]' and '[[42, 42], [-42, 12]]': numpy sub: {str(np.subtract(U, v.data).tolist())}\n")

    u = Matrix([[1., 2.], [3., 4.]])
    p = 2.
    U = u.data
    u.scl(p)
    print(f"'[[1., 2.], [3., 4.]]' and '[[7., 4.], [-2., 2.]]': custom scl: {u.data}")
    print(f"'[[1., 2.], [3., 4.]]' and '[[7., 4.], [-2., 2.]]': numpy multiply: {str(np.multiply(U, p).tolist())}\n")
    
    u = Matrix([[42, 42], [-42, 12]])
    p = -12
    U = u.data
    u.scl(p)
    print(f"'[[42, 42], [-42, 12]]' and '[[42, 42], [-42, 12]]': custom sub: {u.data}")
    print(f"'[[42, 42], [-42, 12]]' and '[[42, 42], [-42, 12]]': numpy sub: {str(np.multiply(U, p).tolist())}\n")
