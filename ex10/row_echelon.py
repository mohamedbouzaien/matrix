from matrix import Matrix

def row_echelon(self) -> 'Matrix':
    rowCount = len(self.data)
    columnCount = len(self.data[0])
    for lead, r in enumerate(range(rowCount)):
        if lead >= columnCount:
            return self
        i = r
        while abs(self.data[i][lead]) < 1e-8:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return self
        self.data[i], self.data[r] = self.data[r], self.data[i]
        lv = self.data[r][lead]
        self.data[r] = [mrx / float(lv) for mrx in self.data[r]]
        for i in range(rowCount):
            if i != r:
                lv = self.data[i][lead]
                self.data[i] = [iv - lv*rv for rv, iv in zip(self.data[r], self.data[i])]
    return self

if __name__ == "__main__":
    import sympy as sp
    
    u = Matrix([[1, 0], [0, 1]])
    print(f"\n[[1, 0], [0, 1]]: custom row_echelon: {row_echelon(u).data}")
    print(f"[[1, 0], [0, 1]]: sympy rref: {sp.Matrix(u.data).rref()[0]}")

    u = Matrix([[1, 2], [3, 4]])
    print(f"\n[[1, 2], [3, 4]]: custom row_echelon: {row_echelon(u).data}")
    print(f"[[1, 2], [3, 4]]: sympy rref: {sp.Matrix(u.data).rref()[0]}")

    u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(f"\n[[1, 0, 0], [0, 1, 0], [0, 0, 1]]: custom row_echelon: {row_echelon(u).data}")
    print(f"[[1, 0, 0], [0, 1, 0], [0, 0, 1]]: sympy rref: {sp.Matrix(u.data).rref()[0]}")
  
    u = Matrix([[1, 2], [3, 4], [5, 6]])
    print(f"\n[[1, 2], [3, 4], [5, 6]]: custom row_echelon: {row_echelon(u).data}")
    print(f"[[1, 2], [3, 4], [5, 6]]: sympy rref: {sp.Matrix(u.data).rref()[0]}")
