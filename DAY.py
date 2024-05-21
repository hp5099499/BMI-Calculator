import pandas as pd 

d={'col1':[1,2,3,23,4],'col2':[2,13,4,7,23],'col3':[3,7,8,9,6],'col5':[3,7,8,9,6],'col5':[3,7,8,9,6],'col6':[3,7,8,9,6]}
df=pd.DataFrame(data=d)
print(df)
print(df.shape[1])

# import numpy as np
# x=[31,345,2,5,4,3,456,3,5655,34,65,46,44]
# y=np.mean(x)
# print(y)

# import pandas as pd 
# s=pd.read_csv("data.csv",header=0,sep=",")
# # print(s.head())
# # s.dropna(axis=0,inplace=True)
# # # print(s.info())
# # s["Order ID"]=s["Order ID"].astype(object)
# # s["Age"]=s["Age"].astype(int)
# pd.set_option('display.max_column',None)
# print(s.describe())


# plot the graph using csv file

#Three lines to make our compiler able to draw:
# import sys
# import matplotlib
# matplotlib.use('TkAgg')

# import pandas as pd
# import matplotlib.pyplot as plt

# health_data = pd.read_csv("data1.csv", header=0, sep=",")

# health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='area')
# plt.ylim(ymin=0)
# plt.xlim(xmin=0)
# plt.title('Pulse vs Calorie graph')
# plt.show()

# #Two lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()


# PLOT THE GRAPH USING THE X AND Y AXIS

# # importing the required module
# import matplotlib.pyplot as plt
  
# # x axis values
# x = [1,2,3]
# # corresponding y axis values
# y = [2,4,1]
  
# # plotting the points 
# plt.plot(x, y)
  
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
  
# # giving a title to my graph
# plt.title('My first graph!')
  
# # function to show the plot
# plt.show()


# slope aand intercept

# def slope(X1,Y1,X2,Y2):
#     S=(Y2-Y1)/(X2-X1)
#     return S

# print(slope(20,40,30,10 ))


# slope  and intercept in csv file 

# import pandas as pd 
# import numpy as np
 

# data=pd.read_csv("data1.csv",header=0,sep=",")
# x=data['Average_Pulse']
# y=data['Calorie_Burnage']
# slope=np.polyfit(x,y,1)
# print(slope)


# def fun(x):
#     return 2*x+80
# print(fun(34))


# # percentile

# import pandas as pd 
# import numpy as np
# data=pd.read_csv("data1.csv" ,header=0,sep=",")
# Max_Pulse=data['Max_Pulse']
# percentile10=np.percentile(Max_Pulse,10)
# print(percentile10)

# Standard deviations

# std=np.std(data)
# print(std)

# COEFFICIENT OF VARIATION

# cv=np.std(data)/np.mean(data)
# print(cv)

# variance
# var=np.var(data)
# print(var)


# perfect linear relationship(correlation coefficient=1)

# import sys 
# import matplotlib
# matplotlib.use('TkAgg')


# import pandas as pd
# import matplotlib.pyplot as plt 
# data=pd.read_csv("data1.csv" ,header=0,sep=",")

# data.plot(x="Average_Pulse",y="Calorie_Burnage",kind='scatter')
# plt.show()

# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()


# perfect  negative linear relationship(correlation coefficient=-1)

# import sys 
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# import pandas as pd 
# #  correlation coefficient=0
# corr=pd.read_csv("data1.csv",header=0,sep=",")

# # correlation coefficient=-1
# # negative_corr =  {'Hours_Work_Before_Training': [10,9,8,7,6,5,4,3,2,1],
# # 'Calorie_Burnage': [220,240,260,280,300,320,340,360,380,400]}
# # negative_corr=pd.DataFrame(data=negative_corr)
# corr.plot(x="Hours_work",y="Calorie_Burnage", kind="scatter")
# plt.show()
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

# # correlation matrix
# import pandas as pd
# data=pd.read_csv("data1.csv",header=0,sep=",")
# corr=round(data.corr(),2)
# print(corr)

# Use Seaborn to Create a Heatmap

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# full_health_data = pd.read_csv("data1.csv", header=0, sep=",")
# correlation_full_health = full_health_data.corr()

# axis_corr = sns.heatmap(
# correlation_full_health,
# vmin=-1, vmax=1, center=0,
# cmap=sns.diverging_palette(50, 500, n=500),
# square=True
# )

# plt.show()

# correlation and casuality
# import sys
# import matplotlib
# matplotlib.use('TkAgg')
# import pandas as pd
# import matplotlib.pyplot as plt
# d=[20,40,50,60,70,80,90]
# I=[20,40,50,60,70,80,90]
# t={"d":[20,40,50,60,70,80,90],"I":[20,40,50,60,70,80,90]}
# t=pd.DataFrame(data=t)
# t.plot(x="d",y="I",kind='scatter')
# plt.show()
# correlation_beach = t.corr()
# print(correlation_beach)

# #Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()


# linear regression -- relatioship is used to predict the outcome of events
# uses least square method to plot line ina way to minimize the distance(residuals,error)of all data points
# import sys
# import matplotlib
# matplotlib.use('TkAgg')

# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import stats
# data=pd.read_csv("data1.csv",header=0,sep=",")
# x=data['Average_Pulse']
# y=data['Calorie_Burnage']
# slope, intercept,r,p,std_err=stats.linregress(x,y)
# def myfunc(x):
#     return slope*x+intercept
# mymodel=list(map(myfunc,x))
# plt.scatter(x,y)
# plt.plot(x,slope*x+intercept)
# plt.ylim(ymin=0,ymax=369)
# plt.xlim(xmin=0,xmax=965    )
# plt.xlabel("Average_Pulse")
# plt.ylabel("Calorie_Burnage")
# plt.show()

# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()\


# #regression table--Linear Regression Table in Python
# P-value is a statistical number to conclude if there is a relationship between Average_Pulse and Calorie_Burnage.
# import pandas as pd 
# import statsmodels.formula.api as smf
# data=pd.read_csv("data1.csv",header=0,sep=",")
# model=smf.ols('Calorie_Burnage ~ Average_Pulse',data=data)
# results=model.fit()
# print(results.summary())

# def predict(Average_Pulse):
#     return(0.3296 * Average_Pulse+346.8662)
# print(predict(120))
# print(predict(230))
# print(predict(430))
# print(predict(130))

# def predict(Average_Pulse,Duration):
#     return(0.3296 * Average_Pulse+5.8434*Duration-334.5194)
# print(predict(120,60))
# print(predict(230,45))
# print(predict(430,30))
# print(predict(130,15))

# import numpy as np
# data=[106,121,152,234,347]
# std=np.std(data)
# var=np.var(data)
# print("Standard variation and variance of 5 states is:",std,"and",var)

# data1=[1450,1250,1776,1388,1340]
# std1=np.std(data1)
# var1=np.var(data1)
# print("Standard variation and variance of 5 tallest skyscrapers is:",std1,"and",var1)

# data2=[7.7,7.4,7.3,7.9]
# std2=np.std(data2)
# var2=np.var(data2)
# print("Standard variation and variance of scores is:",std2,"and",var2)

# data3=[112,100,127,120,134,118,105,110]
# std3=np.std(data3)
# var3=np.var(data3)
# print("Standard variation and variance of heighest temperature in 8 specific states is:",std3,"and",var3)

# arr =np.array([1,2,3,4,5],ndmin=2)
# arr =np.array([1,2,3,4,5])
# print(arr[1]+arr[0])
# print(arr.ndim)
# print(arr)

# dtype define type of array
# arr=np.array([[2,3,4,5,6],[1,2,3,4,5]],dtype="i4")
# # print arrayy
# print(arr)
# # indexing
# print(arr[1,2])
# # type of array
# print(arr.ndim)
# # slicing
# print(arr[0:2,1:4])
# # astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
# arr=np.array([1,2,0])
# new=arr.astype('bool')
# print(new)
# print(new.dtype)

# # copy and view
# import numpy as np
# arr =np.array([1,2,3,4,45])
# # copy() oringinal array
# x=arr.copy()
# arr[0]=23
# print(arr)
# print(x)
# # VIEW(): change the original array, and display both arrays.
# y=arr.view()
# # NumPy array has the attribute base that returns None if the array owns the data.
# print(y.base)


# import numpy as np
# arr=np.array([1,2,3,4,5,5,15])
# print(arr)
# # shape that returns a tuple with each index having the number of corresponding elements.
# print(arr.shape)


# import numpy as np
# arr=np.array([1,2,3,4,52,4,6,8,10,12,23,45])
# reshape()--create the array in matrix form
# 2d model
# new =arr.reshape(4,4)
# print(new)

# 3d model---reshape(matrix,row,column)
# new =arr.reshape(4,3,1)
# reshape(-1)-- convert array in one dimension
# new =arr.reshape(4,3,1)
# base in basic format
# new =(arr.reshape(4,3,1).base)
# print(new)

# iterative arrays 
# import numpy as np
# # in 2d only
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   for y in x:
#     print(y)

# # in 3d 
# arr=np.array([[[1,2,3,4,5],[2,3,4,5,6]],[[2,4,6,8,7],[4,5,6,7,8]]])
# for x in arr:
#  for y in x:
#   for z in y:
 
#     print(z)


# import numpy as np
# arr=np.array( [[1,2,3,4],[5,6,7,8]])
# # nditer() is a helping function that can be used from very basic to very advanced iterations
# # for x in np.nditer(arr):
# #     print(x)

# # change the data type of the element, extra space is called buffer
# # for Y in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
# #     print(Y)

# for x in np.nditer(arr[:,::2]):
#     print(x)