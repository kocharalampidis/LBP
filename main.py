from camera_frame import cam_frame
from compare import compare
from load_folders import load_folders
from load_hists import load_hists
from results import results

# change path variables according to
path_beans_train = '../Dataset/Train_Hists/beans_hist/'
path_hazelnuts_train = '../Dataset/Train_Hists/hazelnuts_hist/'
path_chickpeas_train = '../Dataset/Train_Hists/chickpeas_hist/'
path_blackeyed_train = '../Dataset/Train_Hists/blackeyed_hist/'
path_cashews_train = '../Dataset/Train_Hists/cashews_hist/'

beans_list, hazelnuts_list, chickpeas_list, blackeyed_list, cashews_list = load_folders(path_beans_train,
                                                                                        path_hazelnuts_train,
                                                                                        path_chickpeas_train,
                                                                                        path_blackeyed_train,
                                                                                        path_cashews_train)

beans_hist, hazelnuts_hist, chickpeas_hist, blackeyed_hist, cashews_hist = load_hists(beans_list,
                                                                                      hazelnuts_list,
                                                                                      chickpeas_list,
                                                                                      blackeyed_list,
                                                                                      cashews_list)
hist_test = cam_frame()
dists = compare(beans_hist, hazelnuts_hist, chickpeas_hist, blackeyed_hist, cashews_hist, hist_test)

results(dists)
