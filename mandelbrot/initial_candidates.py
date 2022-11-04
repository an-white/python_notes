import numpy as np

np.warnings.filterwarnings("ignore")


def complex_matrix(x_min, x_max, y_min, y_max, pixel_density):
    re = np.linspace(x_min, x_max, int((x_max - x_min) * pixel_density))
    im = np.linspace(y_min, y_max, int((y_max - y_min) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j
