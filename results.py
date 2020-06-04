from numpy import mean
def results(dists):
    mean_results = {'beans': 0, 'hazelnuts': 0, 'chickpeas': 0, 'blackeyed': 0, 'cashews': 0}
    min_results = {'beans': 0, 'hazelnuts': 0, 'chickpeas': 0, 'blackeyed': 0, 'cashews': 0}

    c = 0
    for k, v in mean_results.items():
        mean_results[k] = mean(dists[c][:])
        min_results[k] = min(dists[c][:])
        c = c + 1

    print('closest mean distance:')
    print(min(mean_results, key=mean_results.get))

    print('closest minimum distance:')
    print(min(min_results, key=min_results.get))

    print('\n \n \n')
    print('rest of measurments')
    print('mean distances:')
    print(mean_results,"\n")

    print('min distances:')
    print(min_results)