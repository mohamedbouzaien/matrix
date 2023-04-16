from matrix import Vector

def norm_1(v: Vector) -> float:
    return sum(abs(x) for x in v.data)

def norm(v: Vector) -> float:
    return sum(x**2 for x in v.data)**0.5

def norm_inf(v: Vector) -> float:
    return max(abs(x) for x in v.data)

if __name__ == '__main__':
    import numpy as np
    
    u = Vector([-1., 6.])
    print(f"[-1., 6.]': my norm_1: {norm_1(u)}")
    print(f"[-1., 6.]': numpy norm_1: {np.linalg.norm(u.data, ord=1)}\n")
    print(f"[-1., 6.]': my norm: {norm(u)}")
    print(f"[-1., 6.]': numpy norm: {np.linalg.norm(u.data, ord=2)}\n")
    print(f"[-1., 6.]': my inf_norm: {norm_inf(u)}")
    print(f"[-1., 6.]': numpy inf_norm: {np.linalg.norm(u.data, np.inf)}\n")

    u = Vector([0., 0., 0.])
    print(f"[0., 0., 0.]': my norm_1: {norm_1(u)}")
    print(f"[0., 0., 0.]': numpy norm_1: {np.linalg.norm(u.data, ord=1)}\n")
    print(f"[0., 0., 0.]': my norm: {norm(u)}")
    print(f"[0., 0., 0.]': numpy norm: {np.linalg.norm(u.data, ord=2)}\n")
    print(f"[0., 0., 0.]': my inf_norm: {norm_inf(u)}")
    print(f"[0., 0., 0.]': numpy inf_norm: {np.linalg.norm(u.data, np.inf)}\n")

    u = Vector([1., 2., 3.])
    print(f"[1., 2., 3.]': my norm_1: {norm_1(u)}")
    print(f"[1., 2., 3.]': numpy norm_1: {np.linalg.norm(u.data, ord=1)}\n")
    print(f"[1., 2., 3.]': my norm: {norm(u)}")
    print(f"[1., 2., 3.]': numpy norm: {np.linalg.norm(u.data, ord=2)}\n")
    print(f"[1., 2., 3.]': my inf_norm: {norm_inf(u)}")
    print(f"[1., 2., 3.]': numpy inf_norm: {np.linalg.norm(u.data, np.inf)}\n")

    u = Vector([-1., -2.])
    print(f"[-1., -2.]': my norm_1: {norm_1(u)}")
    print(f"[-1., -2.]': numpy norm_1: {np.linalg.norm(u.data, ord=1)}\n")
    print(f"[-1., -2.]': my norm: {norm(u)}")
    print(f"[-1., -2.]': numpy norm: {np.linalg.norm(u.data, ord=2)}\n")
    print(f"[-1., -2.]': my inf_norm: {norm_inf(u)}")
    print(f"[-1., -2.]': numpy inf_norm: {np.linalg.norm(u.data, np.inf)}\n")
