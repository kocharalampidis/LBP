import cv2 as cv
import numpy as np


# create a loop for every histogram list loaded
# comparing the hist_test with every hist in each list
# returns a list with calculated distances from every comparison
def compare(beans_list, hazelnuts_list, chickpeas_list, blackeyed_list, cashews_list, hist_test):
    # create a list of lists, for every list histogram we got from function: loaded_hists()
    l = beans_list, hazelnuts_list, chickpeas_list, blackeyed_list, cashews_list

    # create placeholder for the arrays
    dists = [[] for x in range(len(l))]

    #     compare the hist_test, with every element in each of the lists of trained_histograms
    #     create a list -> "dists", with the results.py from every comparison
    for i in range(0, len(l)):
        for j in range(0, len(l[i])):
            dists[i].append((cv.compareHist(np.array(hist_test, dtype=np.float32),
                                            np.array(l[i][j], dtype=np.float32),
                                            cv.HISTCMP_INTERSECT)))

    return dists
