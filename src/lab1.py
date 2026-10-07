import os
import json
import matplotlib.pyplot as plt
import pandas as pd

#===PATHS===#
DATA_PATH = "data/sample-points.csv"
OUTPUT_PATH = "output/"
SUMMARY_PATH = os.path.join(OUTPUT_PATH, "summary.json")
PLOT_PATH = os.path.join(OUTPUT_PATH, "scatter_plot.png")

points = open(DATA_PATH)
data = pd.read_csv(points)
