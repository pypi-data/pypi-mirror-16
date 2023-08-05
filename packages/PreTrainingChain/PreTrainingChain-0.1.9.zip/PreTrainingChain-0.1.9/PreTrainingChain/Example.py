#-------------------------------------------------------------------------------
# Name:        Example
# Purpose:
#
# Author:      rf
#
# Created:     11/08/2015
# Copyright:   (c) rf 2015
# Licence:     Apache Licence 2.0
#-------------------------------------------------------------------------------

import numpy as np
from PreTrainingChain import ChainClassfier
from util import make_sample


if __name__ == '__main__':
    pre_train_size = 1
    pre_test_size = 200
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

    #input layer=784, hidden_layer 1st = 400, hidden_layer 2nd = 300,
    #hidden_layer 3rd = 150, hidden_layer 4th = 100, output layer = 10
    pc = ChainClassfier([784,400,150,10])

    #x_pre_train: sample data for pre-training
    #if x_pre_train == numpy.array([]), pre-training is skkiped.
    #x_train: sample data for learn as deep network
    #y_train: sample target for learn as deep network (e.g. 0-9 for MNIST)
    #x_train: sample data for test as deep network
    #y_train: sample target for test as deep network (e.g. 0-9 for MNIST)
    #isClassification: Classification problem or not
    pc.fit(x_train, y_train, x_pre_train=x_pre_train)
    print('test_accuracy: {0}'.format(pc.score(x_test, y_test)))

