from core import calculate_metrics
from core import plot_table_matplotlib_params

import numpy as np

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
streams = []

directory = "param_setup/"
mypath = "streams/%s" % directory
streams += ["%s%s" % (directory, os.path.splitext(f)[0]) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
streams.sort()

method_names = []
methods_alias = []
# for ratio in np.linspace(0.25, 0.75, 11):
#     method_names.append("DSE-%f" % ratio)
#     methods_alias.append("%0.2f" % ratio)

us_names = [
        "CNN",
        "ENN",
        "RENN",
        "AllKNN",
        "IHT",
        "NM",
        "NCR",
        "OSS",
        # "RUS",
        "TL",
    ]

os_names = [
        # "ADASYN",
        # "BSMOTE",
        # "ROS",
        # "SMOTE",
        "SVMSMOTE",
    ]

method_names = []

for oname in os_names:
    for uname in us_names:
        method_names.append("DSE_"+oname+"-"+uname)
methods_alias = method_names

metrics_alias = [
           "Gmean",
           "F-score",
           "Precision",
           "Recall",
           "Specifity",
          ]

metrics = [
           "g_mean",
           "f1_score",
           "precision",
           "recall",
           "specifity",
          ]

experiment_names = ["ps_s/svm", "ps_s/knn", "ps_s/gnb", "ps_s/dtc"]
# experiment_names = ["ps_b/svm", "ps_b/knn", "ps_b/gnb", "ps_b/dtc"]


for experiment_name in experiment_names:
    calculate_metrics(method_names, streams, metrics, experiment_name, recount=False)

plot_table_matplotlib_params(method_names, streams, metrics, experiment_names, methods_alias=methods_alias, metrics_alias=metrics_alias)
