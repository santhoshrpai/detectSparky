__author__ = 'kannan'

import cPickle, numpy, gzip
feature = numpy.array([[0.2, 0.3, 0.5, 1.4], [1.3, 2.1, 0.3, 0.1], [0.3, 0.5, 0.5, 1.4]], dtype = 'float32')
label = numpy.array([2, 0, 1])
with gzip.open('filename.pkl.gz', 'wb') as f:
    cPickle.dump((feature, label), f)