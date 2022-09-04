"""工程能力指数Cp, Cpkの算出"""

from turtle import color, title
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 16            #グラフのフォントサイズ

file_path = 'data.csv'
df_new = pd.read_csv(file_path)
df_new.index = np.arrange(1, len(df) + 1)     #インデックスを1から振りなおす

# DF = df[['RM', 'LSTART', 'PRICE']]
# DF.hist()
plt.tight_layout()

class ProcessMangement(object):
    """生産管理に関するクラス"""

    def __init__(self, df: pd.DataFrame) -> None:
        self.ave = df.mean()                                                                  #平均値
        self.sigma = np.std(df.values, ddof=1)                                                #標準偏差
        self.usl = self.ave + 3 * self.sigma                                                  #上側規格値
        self.lsl = self.ave - 3 * self.sigma                                                  #下側規格値
        self.cp = (self.usl - self.lsl) / (6 * self.sigma)                                    #工程能力指数Cp
        self.fig = plt.figure()                                                               #描画全体の領域(Figureインスタンスの生成)

    def figure_init(self, df: pd.DataFrame) -> None:
        """グラフ描画のための初期化"""
        ax = self.fig.add_subplot(1, len(DF.columns), i, title = col + ": cp = {:.2f}".format(cp))
        ax.hist(df.values, bins = 10, density = False, color = 'b', rwidth = 0.9)

    
    def display_normgraph(self) -> None:
        """正規分布グラフの表示"""
        x = np.linspace(self.lsl, self.usl, num = 1000)                                                 #正規分布のx軸
        y = np.exp(-(x - self.ave) ** 2 / (2 * self.sigma ** 2)) / (np.sqrt(2 * np.pi) * self.sigma)    #正規分布のy軸

#Cpの算出
def calc_Cp(df :pd.DataFrame) -> float:
    """工程能力指数Cpの算出"""

    ave = df.mean()                                                                  #平均値
    sigma = np.std(df.values, ddof=1)                                                #標準偏差
    usl = ave + 3 * sigma                                                            #上側規格値
    lsl = ave - 3 * sigma                                                            #下側規格値
    cp = (usl - lsl) / (6 * sigma)                                                   #工程能力指数Cp

    
    
    # ax2 = ax.twinx()
    # ax2.plot(x, y, c = 'r')

    # ax.grid()
    # plt.tight_layout()

    return ave, sigma, cp




