import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from load_image import ft_load
from PIL import Image


def main():
    """
    load an image, crop a specific region, convert to grayscale,
    transpose the image, and display the result.
    """
    img_array = ft_load('../images/animal.jpeg')
    img = Image.fromarray(img_array)
    if array(img_array).size == 0:
        exit(1)

    # Cut image and display informations
    cut_img = img.crop((450, 150, 850, 550)).convert('L')
    cut_array = np.expand_dims(array(cut_img), axis=2)
    print(f"The shape of the image is: {cut_array.shape}")
    print(cut_array)

    # Transpose image and display informations
    transpose_img = transpose_matrice(cut_array)
    transpose_array = array(transpose_img)
    print(f"New shape after Transpose : {transpose_array.shape}")
    print(transpose_array)

    # Display image
    plt.imshow(transpose_img, cmap='gray')
    plt.show()


def transpose_matrice(matrice3d: array) -> array:
    """
    Convert a 3D matrix to a 2D matrix and transpose it.
    """
    matrice2d = matrice3d.reshape(matrice3d.shape[0], -1)
    rows = len(matrice2d)
    cols = len(matrice2d)
    new_matrice = []

    for j in range(0, cols):
        new_row = []
        for i in range(0, rows):
            new_row.append(matrice2d[i][j])
        new_matrice.append(new_row)

    return new_matrice


if __name__ == '__main__':
    main()
