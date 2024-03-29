import matplotlib.pyplot as plt

from initial_candidates import complex_matrix


def sequence(c, z=0):
    while True:
        yield z
        z = z ** 2 + c


def mandelbrot(candidate):
    return sequence(z=0, c=candidate)


def julia(candidate, parameter):
    return sequence(z=candidate, c=parameter)


def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2


def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]


if __name__ == '__main__':
    c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=21)
    members = get_members(c, num_iterations=20)

    """
    plt.scatter(members.real, members.imag, color="black", marker=",", s=1)
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
    """
    c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
    plt.imshow(is_stable(c, num_iterations=20), cmap="binary")
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()