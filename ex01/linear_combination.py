from matrix import Vector

def linear_combination(u, coefs):
    if len(u) != len(coefs):
        print("linear_combination: Input arrays doesn't have have the same length!")
        return
    dim = len(u[0])
    return [sum(coef * v[j] for v, coef in zip(u, coefs)) for j in range(dim)]

if __name__ == "__main__":
    import numpy as np

    print("------------------------- linear_combination -----------------------------\n")
    u1 = [-42., 42.]
    v1 = [-1]
    print(f"\n([-42., 42.]), [-1.]: my linear_combination: {linear_combination([u1], v1)}")
    print(f"([-42., 42.]), [-1.]: numpy.dot: {np.dot(np.array(u1).reshape(2, 1), v1)}\n")

    u2_1 = [-42.]
    u2_2 = [-42.]
    u2_3 = [-42.]
    v2 = [-1., 1., 0.]
    print(f"([-42.][-42.][-42.]), [-1., 1., 0.]: my linear_combination: {linear_combination([u2_1, u2_2, u2_3], v2)}")
    print(f"([-42.][-42.][-42.]), [-1., 1., 0.]: numpy.dot: {np.dot(np.transpose((u2_1, u2_2, u2_3)) , np.array(v2).T)}\n")

    u3_1 = [1., 0., 0.]
    u3_2 = [0., 1., 0.]
    u3_3 = [0., 0., 1.]
    v3 = [10., -2., 0.5]
    print(f"([1., 0., 0.][0., 1., 0.][0., 0., 1.]), [10., -2., 0.5]: my linear_combination: {linear_combination([u3_1, u3_2, u3_3], v3)}")
    print(f"([1., 0., 0.][0., 1., 0.][0., 0., 1.]), [10., -2., 0.5]: numpy.dot: {np.dot(np.transpose((u3_1, u3_2, u3_3)) , np.array(v3).T)}\n")


    u4_1 = [1., 2., 3.]
    u4_2 = [0., 10., -100.]
    v4 = [10., -2.]
    print(f"([1., 2., 3.][0., 10., -100.]), [10., -2.]: my linear_combination: {linear_combination([u4_1, u4_2], v4)}")
    print(f"([1., 2., 3.][0., 10., -100.]), [10., -2.]:  numpy.dot: {np.dot(np.transpose((u4_1, u4_2)) , np.array(v4).T)}\n")
