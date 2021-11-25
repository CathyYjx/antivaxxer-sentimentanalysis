import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

filename_dict = {"vaccine tweets 7_30.csv":"Apr 17", "vaccine tweets 37.csv":"Apr 24", "vaccine tweets 44.csv":"May 01", "vaccine tweets 51.csv":"May 08",
"vaccine tweets 58.csv":"May 15","vaccine tweets 65.csv":"May 22","vaccine tweets 72.csv":"May 29","vaccine tweets 79.csv":"Jun 05",
"vaccine tweets 86.csv":"Jun 12","vaccine tweets 93.csv":"Jun 19","vaccine tweets 100.csv":"Jun 26","vaccine tweets 107.csv":"Jul 03",
"vaccine tweets 114.csv":"Jul 10","vaccine tweets 121.csv":"Jul 17","vaccine tweets 128.csv":"Jul 24","vaccine tweets 135.csv":"Jul 31",
"vaccine tweets 142.csv":"Aug 07","vaccine tweets 149.csv":"Aug 14","vaccine tweets 156.csv":"Aug 21"}
#"vaccine tweets 205.csv":"Oct 09","vaccine tweets 212.csv":"Oct 16","vaccine tweets 219.csv":"Oct 23","vaccine tweets 226.csv":"Oct 30"


df_merge = pd.DataFrame()
for filename in filename_dict:
    df_current = pd.read_csv(r'/Users/cathy/Desktop/vaccine only no geo tagged data/'+filename, names=['tweet','sentiment_score'],lineterminator='\n')
    df_current["date"] = filename_dict[filename]
    df_merge = pd.concat([df_merge, df_current], axis=0)

df_merge.to_csv(r'/Users/cathy/Desktop/merged_mar_to_aug.csv')
