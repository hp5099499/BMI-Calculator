import numpy as np
import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use('Agg')
import sys

s=pd.read_csv("Financial Sample.csv",header=0,sep=",")
# print(s.head(10))
# print(s.tail(10))
# print(s.info())
# print(s.shape)
# print(s.describe())
# s["Units Sold"]=s["Units Sold"].astype(int)
# print(s.info())
# s.plot(x ='Sales', y='Profit', kind='area')
# plt.ylim(ymin=0)
# plt.xlim(xmin=0)
# plt.show('Sales  vs  Profit')
# plt.show()
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

print(s['Sales'])