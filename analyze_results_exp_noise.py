from core import calculate_metrics
from core import plot_streams_nexp

import numpy as np

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
streams = []

directory = "noise_exp/"
mypath = "streams/%s" % directory
streams += ["%s%s" % (directory, os.path.splitext(f)[0]) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
streams.sort()

method_names = [
                "DSE",
                "KMeanClustering",
                "LearnppCDS",
                "LearnppNIE",
                "REA",
                "OUSE",
                # "MLPClassifier",
                ]

methods_alias = [
                "DSE",
                "KMC",
                "L++CDS",
                "L++NIE",
                "REA",
                "OUSE",
                # "MLPC",
                ]

metrics_alias = [
           "$Gmean_s$",
           "Precision",
           "Recall",
           "Specificity",
          ]

metrics = [
           "g_mean",
           "precision",
           "recall",
           "specifity",
          ]

experiment_names = [
                    "noise_exp/svm",
                    "noise_exp/knn",
                    "noise_exp/gnb",
                    "noise_exp/dtc"
                   ]

for experiment_name in experiment_names:

    calculate_metrics(method_names, streams, metrics, experiment_name, recount=True)
    plot_streams_nexp(method_names, streams, metrics, experiment_name, methods_alias=methods_alias, metrics_alias=metrics_alias)
