#-------------------------------------------------------------------------------
# Name:        GridSearchExample
# Purpose:
#
# Author:      rf
#
# Created:     04/24/2016
# Copyright:   (c) rf 2016
# Licence:     Apache Licence 2.0
#-------------------------------------------------------------------------------


import numpy as np
from PreTrainingChain import ChainClassfier
from sklearn import grid_search
from util import make_sample

if __name__ == '__main__':
    pre_train_size = 1
    pre_test_size = 1
    train_size = 2000
    test_size = 2000

    sample = make_sample(pre_train_size+pre_test_size+train_size+test_size)
    x_pre_train, x_pre_test, x_train, x_test, _ = np.split(sample.data,
        [pre_train_size,
        pre_train_size + pre_test_size,
        pre_train_size + pre_test_size + train_size,
        pre_train_size + pre_test_size + train_size + test_size])

    _, _, y_train, y_test, _ = np.split(sample.target,
        [pre_train_size,
        pre_train_size + pre_test_size,
        pre_train_size + pre_test_size + train_size,
        pre_train_size + pre_test_size + train_size + test_size])

    pc = ChainClassfier([784,400,150,10])
    #gridsearch for hidden layers and learning epoch.
    result = grid_search.GridSearchCV(pc, {'n_units': ([784,400,150,10], [784,300,150,10]),
                                           'epoch': (10, 14)}, verbose=3, n_jobs=1, cv=2)
    result.fit(x_train, y_train)
    print(result.best_params_)

