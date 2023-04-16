from matrix import Vector
from dot import dot
from norm import norm

def angle_cos(u: Vector, v: Vector) -> float:
    if len(u.data) != len(v.data):
        print("angle_cos: vectors size error!")
        return
    norm_u = norm(u)
    norm_v = norm(v)
    if norm_u == 0.0 or norm_v == 0.0:
        print("angle_cos: zero vectors error")
        return
    return dot(u, v) / (norm_u * norm_v)

if __name__ == '__main__':
    import numpy as np
    
    u = Vector([2, 3])
    v = Vector([5, 7])
    print(f"[2, 3]' and '[5, 7]': custom angle_cos: {angle_cos(u, v)}")
    print(f"[2, 3]' and '[5, 7]': numpy to calc cos: {np.dot(u.data, v.data) / (np.linalg.norm(u.data) * np.linalg.norm(v.data))}\n")

    u = Vector([1., 0.])
    v = Vector([1., 0.])
    print(f"[1., 0.]' and '[1., 0.]': custom angle_cos: {angle_cos(u, v)}")
    print(f"[1., 0.]' and '[1., 0.]': numpy to calc cos: {np.dot(u.data, v.data) / (np.linalg.norm(u.data) * np.linalg.norm(v.data))}\n")

    u = Vector([1., 0.])
    v = Vector([0., 1.])
    print(f"[1., 0.]' and '[0., 1.]': custom angle_cos: {angle_cos(u, v)}")
    print(f"[1., 0.]' and '[0., 1.]': numpy to calc cos: {np.dot(u.data, v.data) / (np.linalg.norm(u.data) * np.linalg.norm(v.data))}\n")

    u = Vector([-1., 1.])
    v = Vector([ 1., -1.])
    print(f"[-1., 1.]' and '[ 1., -1.]': custom angle_cos: {angle_cos(u, v)}")
    print(f"[-1., 1.]' and '[ 1., -1.]': numpy to calc cos: {np.dot(u.data, v.data) / (np.linalg.norm(u.data) * np.linalg.norm(v.data))}\n")

    u = Vector([2., 1.])
    v = Vector([4., 2.])
    print(f"[2., 1.]' and '[4., 2.]': custom angle_cos: {angle_cos(u, v)}")
    print(f"[2., 1.]' and '[4., 2.]': numpy to calc cos: {np.dot(u.data, v.data) / (np.linalg.norm(u.data) * np.linalg.norm(v.data))}\n")

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(f"[1., 2., 3.]' and '[4., 5., 6.]': custom angle_cos: {angle_cos(u, v)}")
    print(f"[1., 2., 3.]' and '[4., 5., 6.]': numpy to calc cos: {np.dot(u.data, v.data) / (np.linalg.norm(u.data) * np.linalg.norm(v.data))}\n")
