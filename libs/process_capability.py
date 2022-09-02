"""工程能力指数Cp, Cpkの算出"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 16            #グラフのフォントサイズ

file_path = 'data.csv'
df = pd.read_csv(file_path)

df.index = np.arrange(1, len(df) + 1)