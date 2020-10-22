from core import calculate_metrics
from core import plot_streams_matplotlib, drift_metrics_table_mean
from core import pairs_metrics_multi

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

stream_sets = []
streams_aliases = []
streams = []

# directory = "sl_5d/incremental/"
# mypath = "streams/%s" % directory
# streams += ["%s%s" % (directory, os.path.splitext(f)[0]) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
#
# directory = "sl_1d/incremental/"
# mypath = "streams/%s" % directory
# streams += ["%s%s" % (directory, os.path.splitext(f)[0]) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
#
# directory = "moa_5d/incremental/"
# mypath = "streams/%s" % directory
# streams += ["%s%s" % (directory, os.path.splitext(f)[0]) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
#
# directory = "moa_1d/incremental/"
# mypath = "streams/%s" % directory
# streams += ["%s%s" % (directory, os.path.splitext(f)[0]) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
#
# stream_sets += [streams]
# streams_aliases += ["incremental"]
#
# streams = []
# directory = "sl_5d/sudden/"
# mypath = "streams/%s" % directory
# streams += ["%s%s" % (directory, os.path.splitext(f)[0]) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
#
# directory = "sl_1d/sudden/"
# mypath = "streams/%s" % directory
# streams += ["%s%s" % (directory, os.path.splitext(f)[0]) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
#
# directory = "moa_5d/sudden/"
# mypath = "streams/%s" % directory
# streams += ["%s%s" % (directory, os.path.splitext(f)[0]) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
#
# directory = "moa_1d/sudden/"
# mypath = "streams/%s" % directory
# streams += ["%s%s" % (directory, os.path.splitext(f)[0]) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
#
# stream_sets += [streams]
# streams_aliases += ["sudden"]
#
streams = []                                                # step init
# streams += ["real/abalone-17_vs_7-8-9-10"]                  # 250 500
# streams += ["real/elecNormNew"]                             # 500 1000
# streams += ["real/jm1"]                                     # 100 200
# streams += ["real/kc1"]                                     # 100 200
# streams += ["real/kc2"]                                     # 50 100
# streams += ["real/kr-vs-k-three_vs_eleven"]                 # 250 500
# streams += ["real/kr-vs-k-zero-one_vs_draw"]                # 250 500
# streams += ["real/page-blocks0"]                            # 500 1000
# streams += ["real/segment0"]                                # 100 200
# streams += ["real/shuttle-1vs4"]                            # 100 200
# streams += ["real/vehicle0"]                                # 100 200
# streams += ["real/yeast1"]                                  # 150 300
# streams += ["real/yeast3"]                                  # 150 300
# streams += ["real/wisconsin"]                               # 50 100
# streams += ["real/australian"]                              # 50 100
# streams += ["real/pima"]                                    # 50 100
# streams += ["real/heart"]                                   # 52 52
# streams += ["real/glass0"]                                  # 30 60
# streams += ["real/glass-0-1-2-3_vs_4-5-6"]                  # 30 60
# streams += ["real/glass1"]                                  # 30 60
# streams += ["real/yeast-0-2-5-7-9_vs_3-6-8"]                # 100 200
# streams += ["real/vowel0"]                                  # 100 200
# streams += ["real/yeast-0-2-5-6_vs_3-7-8-9"]                # 100 200
# streams += ["real/yeast-0-3-5-9_vs_7-8"]                    # 70 140
# streams += ["real/yeast-2_vs_4"]                            # 60 120
# streams += ["real/yeast-0-5-6-7-9_vs_4"]                    # 60 120
# streams += ["real/shuttle-5vsA"]                            # 1000 2000
# streams += ["real/shuttle-1vsA"]                            # 1000 2000
# streams += ["real/shuttle-4-5vsA"]                          # 1000 2000
# streams += ["real/shuttle-4vsA"]                            # 1000 2000

streams += ["real/covtypeNorm-1-2vsAll-pruned"]                  # 1000 2000
streams += ["real/poker-lsn-1-2vsAll-pruned"]                    # 1000 2000

stream_sets += [streams]
streams_aliases += ["real"]


method_names = [
                "MLPClassifier",
                "KMeanClustering",
                "REA",
                "OUSE",
                "LearnppNIE",
                "LearnppCDS",
                "DSE",
                ]

methods_alias = [
                "MLPC",
                "KMC",
                "REA",
                "OUSE",
                "L++NIE",
                "L++CDS",
                "DSE",
                ]

metrics_alias = [
           "Gmean",
           "F-score",
           "Precision",
           "Recall",
           "Specificity",
          ]

metrics = [
           "g_mean",
           "f1_score",
           "precision",
           "recall",
           "specifity",
          ]

drift_metrics = [
           "recovery",
           "performance_loss",
          ]

drift_metrics_alias = [
           "recovery time",
           "performance loss",
          ]

experiment_names = [
                    "svm",
                    "knn",
                    "gnb",
                    "dtc"
                    ]

for streams, streams_alias in zip(stream_sets, streams_aliases):
    for experiment_name in experiment_names:

        calculate_metrics(method_names, streams, metrics, experiment_name, recount=True)
        plot_streams_matplotlib(method_names, streams, metrics, experiment_name, gauss=5, methods_alias=methods_alias, metrics_alias=metrics_alias)

    # pairs_metrics_multi(method_names, streams, metrics, experiment_names, methods_alias=methods_alias, metrics_alias=metrics_alias, streams_alias=streams_alias)


# for streams, streams_alias in zip(stream_sets[0:-1], streams_aliases[0:-1]):
#     for experiment_name in experiment_names:
#         calculate_metrics(method_names, streams, drift_metrics, experiment_name, recount=True)
#
#     drift_metrics_table_mean(method_names, streams, drift_metrics, experiment_names, methods_alias=methods_alias, metrics_alias=drift_metrics_alias, streams_alias=streams_alias)
