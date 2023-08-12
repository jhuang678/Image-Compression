######################################################################
import matplotlib as mpl
mpl.use('TkAgg')
import ImageCompressor as ic


#####################################################################

if __name__ == '__main__':

    compressor = ic.ImageCompressor(verbose=True)
    compressor.read_bmp(bmp_path="wdw.bmp", img_path="wdw.png")
    compressor.kmeans_compress(k=2, norm=1, img_path="wdw_l1k2.png")
    compressor.kmeans_compress(k=4, norm=1, img_path="wdw_l1k4.png")
    compressor.kmeans_compress(k=6, norm=1, img_path="wdw_l1k6.png")
    compressor.kmeans_compress(k=8, norm=1, img_path="wdw_l1k8.png")

    compressor.kmeans_compress(k=2, norm=2, img_path="wdw_l2k2.png")
    compressor.kmeans_compress(k=4, norm=2, img_path="wdw_l2k4.png")
    compressor.kmeans_compress(k=6, norm=2, img_path="wdw_l2k6.png")
    compressor.kmeans_compress(k=8, norm=2, img_path="wdw_l2k8.png")

    print("Done!")

