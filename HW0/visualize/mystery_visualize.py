import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

def colormapArray(X, colors):
    """
    Basically plt.imsave but return a matrix instead

    Given:
        a HxW matrix X
        a Nx3 color map of colors in [0,1] [R,G,B]
    Outputs:
        a HxW uint8 image using the given colormap. See the Bewares
    """
    X_normalized = (X - np.nanmin(X)) / (np.nanmax(X) - np.nanmin(X))
    X_normalized = np.clip(X_normalized, 0, 1)
    indices = (X_normalized * (len(colors) - 1)).astype(int)
    colormapped_image = (colors[indices] * 255).astype(np.uint8)
    return colormapped_image

if __name__ == "__main__":
    # Solve 3.1: Nonlinear correction and visualization
    data2 = np.load("mysterydata/mysterydata2.npy")
    corrected_sqrt = np.sqrt(data2)
    corrected_log1p = np.log1p(data2)
    plt.imsave("mysterydata2_sqrt.png", corrected_sqrt[:, :, 0], cmap='gray')
    plt.imsave("mysterydata2_log1p.png", corrected_log1p[:, :, 0], cmap='gray')
    print("Saved corrected images for mysterydata2.npy")

    # Solve 3.2: Handling NaN and Inf values in mysterydata3.npy
    data3 = np.load("mysterydata/mysterydata3.npy")
    finite_fraction = np.mean(np.isfinite(data3))
    print(f"Fraction of finite values: {finite_fraction}")

    if finite_fraction < 1:
        data3_cleaned = np.nan_to_num(data3, nan=np.nanmin(data3), posinf=np.nanmax(data3), neginf=np.nanmin(data3))
    else:
        data3_cleaned = data3

    for i in range(9):
        vmin, vmax = np.nanmin(data3_cleaned[:, :, i]), np.nanmax(data3_cleaned[:, :, i])
        plt.imsave(f"vis3_{i}.png", data3_cleaned[:, :, i], vmin=vmin, vmax=vmax, cmap='gray')
    print("Saved cleaned images for mysterydata3.npy")

    # Solve 3.3: Custom colormap visualization for mysterydata4.npy
    data4 = np.load("mysterydata/mysterydata4.npy")
    colors = np.load("mysterydata/colors.npy")
    for i in range(9):
        colormap_image = colormapArray(data4[:, :, i], colors)
        cv2.imwrite(f"vis4_{i}.png", cv2.cvtColor(colormap_image, cv2.COLOR_RGB2BGR))
    print("Saved colormap applied images for mysterydata4.npy")
