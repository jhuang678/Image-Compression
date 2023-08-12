######################################################################
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import KMeansLearner as km
from PIL import Image
######################################################################

class ImageCompressor(object):

    def __init__(self, verbose = False):
        self.verbose = verbose
        if self.verbose:
            print("\nInitialized Image Compressor")
            print("Author: ", self.author())

    def author(self):
        return "Jeffrey Huang"

    def read_image_into_array(self, bmp_path: str = "image.bmp"):
        # Given the image path, read image and store it as an array,.
        # Returns the 3 dimensional image to array.
        img = Image.open(bmp_path)
        img_3Darray = np.array(img, dtype='int32')
        img.close()
        return img_3Darray

    def display_image_from_3dim_array(self, img_3Darray, img_path:str = "img.png"):
        # Display the image with input of 3 dimensional array
        new_img_array = img_3Darray.astype(dtype='uint8')
        img = Image.fromarray(new_img_array, 'RGB')
        plt.imshow(np.asarray(img))
        fig = plt.gcf()
        fig.savefig(img_path)
        # plt.show()
        plt.close(fig)

    def compress_array_from_3D_to_2D(self, array_3D):
        # Compress image array into a flattened '2-dimensional' matrix
        x, y, z = array_3D.shape
        array_2D = np.reshape(array_3D, (x * y, z), order="C")
        assert len(array_2D.shape) == 2
        if self.verbose: print("Compress from", array_3D.shape, "array into", array_2D.shape)
        return array_2D

    def read_bmp(self, bmp_path:str = "img.bmp", img_path:str = "3D_array.png"):
        mpl.rc("savefig", dpi=100)
        self.img_3Darray = self.read_image_into_array(bmp_path)

        if self.verbose: print("Shape of the matrix:", self.img_3Darray.shape)

        self.display_image_from_3dim_array(self.img_3Darray, img_path = img_path)

        self.pixels = self.compress_array_from_3D_to_2D(self.img_3Darray)

        if self.verbose: print("3D-array image saved successfully.")
        if self.verbose: print("Please use bmp_kmeans_compress(k = int, norm = int) to compress image.")

    def kmeans_compress(self, k: int = 2, norm: int = 2, img_path: str = "compressed_img.png", verbose=True):
        learner = km.KmeansLearner(verbose = verbose)
        CLASS, CENTROID = learner.train_data(self.pixels, k=k, norm = norm)
        CENTROID_dict = {}
        for i in set(CLASS):
            CENTROID_dict[i] = CENTROID[i]
        img_2Darray_clustered = np.array([CENTROID_dict[i] for i in CLASS])

        x, y, z = self.img_3Darray.shape

        img_3Darray_clustered = np.reshape(img_2Darray_clustered, (x, y, z), order="C")
        self.display_image_from_3dim_array(img_3Darray_clustered, img_path=img_path)
        print("Finished compressing! Please see " + img_path)

if __name__ == "__main__":
    print("This is a Image K-Means Compressor.")
