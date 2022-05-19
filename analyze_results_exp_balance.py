from core import calculate_metrics
from core import plot_streams_bexp

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
streams = []

directory = "balance_exp/"
mypath = "streams/%s" % directory
streams += ["%s%s" % (directory, os.path.splitext(f)[0]) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
streams.sort()

method_names = [
                "DSE",
                "LearnppCDS",
                "LearnppNIE",
                "KMeanClustering",
                "REA",
                "OUSE",
                # "MLPClassifier",
                ]

methods_alias = [
                "DSE",
                "L++CDS",
                "L++NIE",
                "KMC",
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
                    "balance_exp/svm",
                    "balance_exp/knn",
                    "balance_exp/gnb",
                    "balance_exp/dtc"
                   ]

for experiment_name in experiment_names:

    calculate_metrics(method_names, streams, metrics, experiment_name, recount=True)
    plot_streams_bexp(method_names, streams, metrics, experiment_name, methods_alias=methods_alias, metrics_alias=metrics_alias)
