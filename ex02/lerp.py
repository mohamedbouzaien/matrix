def lerp(u, v, t):
    if type(u) != type(v):
        print("lerp: Input objects doesn't have the same type.")
        return
    if not (0 <= t <= 1):
        print("lerp: t must be between 0 and 1.")
        return
    if isinstance(u, (int, float, complex)):
        return u * (1 - t) + v * t
    elif isinstance(u, list):
        if len(u) != len(v):
            print("lerp: Input lists doesn't have the same length.")
            return
        return [[u[i] * (1 - t) + v[i] * t] for i in range(len(u))]
    else:
        print("lerp: Input objects aren't numbers nor lists.")
        return

if __name__ == "__main__":
    import numpy as np

    print("----------------------- Vector -----------------------------\n")
    print(f"\nmy lerp: (0., 1., 0.): {lerp(0., 1., 0.)}")
    print(f"numpy interp (0., 1., 0.): {np.interp(0., [0., 1.], [0., 1.])}")
    
    print(f"\nmy lerp: (0., 1., 1.): {lerp(0., 1., 1.)}")
    print(f"numpy interp: (0., 1., 1.): {np.interp(1., [0., 1.], [0., 1.])}")

    print(f"\nmy lerp: (0., 42., 0.5): {lerp(0., 42., 0.5)}")
    print(f"numpy interp: (0., 42., 0.5): {np.interp(0.5, [0., 1.], [0., 42.])}")
   
    print(f"\nmy lerp: (-42., 42., 0.5): {lerp(-42., 42., 0.5)}")
    print(f"numpy interp: (-42., 42., 0.5): {np.interp(0.5, [0., 1.], [-42, 42.])}")

    print("----------------------- Matrix -----------------------------\n")
    print(f"\nmy lerp: ([-42., 42.],[42., -42.], 0.5): {lerp([-42., 42.], [42., -42.], 0.5)}")
    print(f"numpy interp: ([-42., 42.], [42., -42.], 0.5): {str(np.array([[np.interp(0.5, [0., 1.], [-42., 42.])], [np.interp(0.5, [0., 1.], [42., -42.])]]).tolist())}")
