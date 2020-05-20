from ensembles import KMeanClustering
from ensembles import LearnppCDS
from ensembles import LearnppNIE
from ensembles import REA
from ensembles import OUSE
from ensembles import DeterministicSamplingEnsemble
from sklearn.neural_network import MLPClassifier
from sklearn.base import clone

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

from core import evaluation
from scipy.io import arff

from joblib import Parallel, delayed
import time

import logging
import traceback
import warnings
import os
from os import listdir
from os.path import isfile, join
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
warnings.simplefilter("ignore")


def evaluate_method(classifier, stream_name, method_name, initial_size, step_size, experiment_name):

    # if os.path.exists("results/raw_conf/%s/%s/%s.csv" % (experiment_name, stream_name, method_name)):
    #     return

    logging.basicConfig(filename='exp.log', filemode="a", format='%(asctime)s - %(levelname)s: %(message)s', level='DEBUG')

    try:
        logging.info("Start %s %s", stream_name, method_name)
        print(stream_name, method_name)
        start = time.time()
        data, meta = arff.loadarff("streams/%s.arff" % stream_name)
        if data is None:
            print("Empty data")
            raise Exception

        classes = meta[meta.names()[-1]][1]
        evl = evaluation.Evaluation(classifier=classifier, stream_name="%s" % stream_name, method_name=method_name, experiment_name=experiment_name, tqdm=False)
        evl.test_and_train(data=data, classes=classes, initial_size=initial_size, step_size=step_size)
        evl.save_to_csv_confmat()
        logging.info("End %s %s %f", stream_name, method_name, time.time()-start)
        print("End", stream_name, method_name, time.time()-start)

    except Exception as ex:
        logging.exception("Exception in %s %s", stream_name, method_name)
        print(str(ex))
        traceback.print_exc()
        print("Exception in ", stream_name, method_name)


cores = open('/proc/cpuinfo').read().count('processor\t:')


base_classifiers = [
                    SVC(probability=True),
                    KNeighborsClassifier(),
                    GaussianNB(),
                    DecisionTreeClassifier(),
                    ]
experiment_names = [
                    "svm",
                    "knn",
                    "gnb",
                    "dtc",
                    ]

for base_classifier, experiment_name in zip(base_classifiers, experiment_names):

    methods = [
               DeterministicSamplingEnsemble(base_classifier=base_classifier),
               KMeanClustering(base_classifier=base_classifier),
               LearnppCDS(base_classifier=base_classifier),
               LearnppNIE(base_classifier=base_classifier),
               REA(base_classifier=base_classifier),
               OUSE(base_classifier=base_classifier),
               MLPClassifier(hidden_layer_sizes=(10)),
               ]

    names = [
               "DSE",
               "KMeanClustering",
               "LearnppCDS",
               "LearnppNIE",
               "REA",
               "OUSE",
               "MLPClassifier",
               ]

    step_size = 500
    initial_size = 2*step_size

    directory = "sl_5d/incremental/"
    mypath = "streams/%s" % directory
    streams = ["%s%s" % (directory, os.path.splitext(f)[0]) for f in listdir(mypath) if isfile(join(mypath, f))]

    directory = "sl_5d/sudden/"
    mypath = "streams/%s" % directory
    streams += ["%s%s" % (directory, os.path.splitext(f)[0]) for f in listdir(mypath) if isfile(join(mypath, f))]

    print("Start", directory)
    start = time.time()

    Parallel(n_jobs=-1)(
        delayed(evaluate_method)(clone(classifier), stream_name, name, initial_size, step_size, experiment_name)
        for classifier, name in zip(methods, names) for stream_name in streams)

    end = time.time()
    print("End %f" % (end-start))
