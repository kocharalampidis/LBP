import cv2 as cv
import numpy as np
from skimage import feature
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from skimage.color import rgb2gray


def cam_frame():

    # Image-Segmentation - Clustering
    def ImgSeg_Clustering(img):
        img_n = img.reshape(img.shape[0] * img.shape[1], img.shape[2])
        kmeans = KMeans(n_clusters=2, random_state=0).fit(img_n)
        pic2show = kmeans.cluster_centers_[kmeans.labels_]
        img_seg = pic2show.reshape(img.shape[0], img.shape[1], img.shape[2])

        return img_seg



    cap = cv.VideoCapture('http://192.168.1.4:8080/video/mjpeg')
   

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()



        # Display the resulting frame
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

    # img filtering for salt & pepper and img segmentation
    median = cv.medianBlur(frame, 5)
    # img = ImgSeg_Clustering(median/255)

    # config variables for lbp computation
    gray = rgb2gray(median)
    numPoints = 8
    radius = 2

    # create lbp image
    lbp_test = feature.local_binary_pattern(gray, numPoints, radius, method="default")

    plt.subplot(231), plt.imshow(gray, cmap='gray'), plt.title('gray img')
    plt.subplot(232), plt.imshow(lbp_test, cmap='gray'), plt.title('lbp')
    plt.show()

    hist_test, _ = np.histogram(lbp_test.ravel(), bins=np.arange(256),
                                range=255, density=True)
    return hist_test
