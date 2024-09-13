import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from load_image import ft_load


def main():
    """
    Load an image, crop a specific region, convert to Black and White,
    and display the result.
    """
    img_array = ft_load('../images/animal.jpeg')
    img = Image.fromarray(img_array)
    if img_array.size == 0:
        exit(1)

    print(img_array)

    zoom_img = img.crop((450, 150, 850, 550)).convert('L')
    zoom_img_array = np.expand_dims(np.array(zoom_img), axis=2)

    print(f"New shape after splicing: {zoom_img_array.shape}")
    print(zoom_img_array)

    plt.imshow(zoom_img, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
