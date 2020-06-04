import os
import glob


# loading folders, checking if folders exists, for each path variable
# creating a list of contents from each folder  and printing msg of len for each folder
# returns the lists containing histograms in .csv format
def load_folders(beans, hazelnuts, chickpeas, blackeyed, cashews):


    if (os.path.isdir(beans)):
        beans_list = glob.glob(beans + '*.csv')
        print('beans_list of length:', len(beans_list))

    else:
        print('beans folder does not exists')
    #   =================================================================================
    if (os.path.isdir(hazelnuts)):
        hazelnuts_list = glob.glob(hazelnuts + '*.csv')
        print('hazelnuts_list of length:', len(hazelnuts_list))

    else:
        print('hazelnuts folder does not exists')
    #   =================================================================================
    if (os.path.isdir(chickpeas)):
        chickpeas_list = glob.glob(chickpeas + '*.csv')
        print('chickpeas_list of length:', len(chickpeas_list))

    else:
        print('chickpeas folder does not exists')
    #   =================================================================================
    if (os.path.isdir(blackeyed)):
        blackeyed_list = glob.glob(blackeyed + '*.csv')
        print('blackeyed_list of length:', len(blackeyed_list))

    else:
        print('blackeyed folder does not exists')
    #   =================================================================================

    if (os.path.isdir(cashews)):
        cashews_list = glob.glob(cashews + '*.csv')
        print('cashews_list of length:', len(cashews_list))
        print('=========================================')

    else:
        print('cashews folder does not exists')


    return beans_list, hazelnuts_list, chickpeas_list, blackeyed_list, cashews_list
