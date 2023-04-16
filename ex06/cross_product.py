from matrix import Vector

def cross_product(u: Vector, v: Vector) -> Vector:
    if u.shape() != 3 or v.shape() != 3:
        print("cross_product: Not a 3D Vector1!")
        return
    return Vector([
        u.data[1] * v.data[2] - u.data[2] * v.data[1],
        u.data[2] * v.data[0] - u.data[0] * v.data[2],
        u.data[0] * v.data[1] - u.data[1] * v.data[0]
    ])

if __name__ == "__main__":
    import numpy as np

    u = Vector([-1., 6., 0])
    v = Vector([3., 2., 0])
    print(f"[-1., 6., 0]' and '[3., 2., 0]': custom cross_product: {cross_product(u, v).data}")
    print(f"[-1., 6., 0]' and '[3., 2., 0]': numpy cross: {np.cross(u.data, v.data)}\n")

    u = Vector([0., 0., 1])
    v = Vector([1., 0., 0])
    print(f"[0., 0., 1]' and '[1., 0., 0]': custom cross_product: {cross_product(u, v).data}")
    print(f"[0., 0., 1]' and '[1., 0., 0]': numpy cross: {np.cross(u.data, v.data)}\n")

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(f"[1., 2., 3.]' and '[4., 5., 6.]': custom cross_product: {cross_product(u, v).data}")
    print(f"[1., 2., 3.]' and '[4., 5., 6.]: numpy cross: {np.cross(u.data, v.data)}\n")

    u = Vector([4., 2., -3])
    v = Vector([-2., -5., 16.])
    print(f"[4., 2., -3]' and '[-2., -5., 16.]': custom cross_product: {cross_product(u, v).data}")
    print(f"[4., 2., -3]' and '[-2., -5., 16.]': numpy cross: {np.cross(u.data, v.data)}\n")
