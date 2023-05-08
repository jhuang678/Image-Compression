# Image K-Means Compressor

This project implements the K-means clustering algorithm to compress images. The implementation is done without using any external libraries for K-means clustering.

## Table of Contents
- [Usage](#usage)
- [Output](#outputn)


## Usage
To compress an image, first create an instance of `ImageCompressor` class. You can then read the image using the `read_bmp` method. After reading the image, you can call `kmeans_compress` method to compress the image.
```python
from ImageCompressor import ImageCompressor
compressor = ImageCompressor()
compressor.read_bmp("input_image.bmp", "input_image_3D.png")
compressor.kmeans_compress(k=16, norm=2, img_path="compressed_image.png")
```

You can adjust the compression level by changing the `k` parameter. A higher value of `k` will result in better quality but larger file size. The `norm` parameter determines the normalization method used in the K-means algorithm.

## Output
The output of the `kmeans_compress` method is the compressed image. It is saved as a PNG file specified in the img_path parameter.

