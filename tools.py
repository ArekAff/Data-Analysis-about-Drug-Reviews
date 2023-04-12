import numpy as np
import pandas as pd

#For plotting
import matplotlib.pyplot as plt
import seaborn as sns

#For text processing
from textblob import TextBlob

df = pd.read_csv('drugsComTrain_raw.tsv',sep='\t')