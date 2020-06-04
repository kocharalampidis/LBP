from numpy import loadtxt, mean

# loading the classified histograms from each list, created in load_folders() function
# returns newly created lists containing histograms, in order to compare them with a test histogram
def load_hists(beans_list, hazelnuts_list, chickpeas_list, blackeyed_list, cashews_list):

    loaded_beans_hists = []
    for i in range(0, len(beans_list)):
        loaded_beans_hists.append(loadtxt(beans_list[i]))
    print('loaded_beans_hists length:', len(beans_list))
    # =================================================================
    loaded_chickpeas_hists = []
    for i in range(0, len(chickpeas_list)):
        loaded_chickpeas_hists.append(loadtxt(chickpeas_list[i]))
    print('loaded_chickpeas_hists length:', len(chickpeas_list))
    # =================================================================

    loaded_hazelnuts_hists = []
    for i in range(0, len(hazelnuts_list)):
        loaded_hazelnuts_hists.append(loadtxt(hazelnuts_list[i]))
    print('loaded_hazelnuts_hists of length:', len(hazelnuts_list))
    # =================================================================

    loaded_blackeyed_hists = []
    for i in range(0, len(blackeyed_list)):
        loaded_blackeyed_hists.append(loadtxt(blackeyed_list[i]))
    print('loaded_blackeyed_hists length:', len(blackeyed_list))

    # =================================================================

    loaded_cashews_hists = []
    for i in range(0, len(cashews_list)):
        loaded_cashews_hists.append(loadtxt(cashews_list[i]))
    print('loaded_cashews_hists length:', len(cashews_list), '\n')

    return loaded_beans_hists, loaded_hazelnuts_hists, loaded_chickpeas_hists, loaded_blackeyed_hists, loaded_cashews_hists