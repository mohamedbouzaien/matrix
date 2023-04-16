from matrix import Vector

def dot(v1: Vector, v2: Vector) -> float:
    if v1.shape() != v2.shape():
        print("dot: different shapes!")
        return
    return sum(x * y for x, y in zip(v1.data, v2.data))

if __name__ == '__main__':
    import numpy as np
    
    u = Vector([2, 3])
    v = Vector([5, 7])
    print(f"[2, 3]' and '[5, 7]': custom dot: {dot(u, v)}")
    print(f"[2, 3]' and '[5, 7]': numpy dot: {np.dot(u.data, v.data)}\n")

    u = Vector([0., 0.])
    v = Vector([1., 1.])
    print(f"[0., 0.]' and '[1., 1.]': custom dot: {dot(u, v)}")
    print(f"[0., 0.]' and '[1., 1.]': numpy dot: {np.dot(u.data, v.data)}\n")

    u = Vector([1., 1.])
    v = Vector([1., 1.])
    print(f"[1., 1.]' and '[1., 1.]': custom dot: {dot(u, v)}")
    print(f"[1., 1.]' and '[1., 1.]': numpy dot: {np.dot(u.data, v.data)}\n")

    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    print(f"[-1., 6.]' and '[3., 2.]': custom dot: {dot(u, v)}")
    print(f"[-1., 6.]' and '[3., 2.]': numpy dot: {np.dot(u.data, v.data)}\n")
