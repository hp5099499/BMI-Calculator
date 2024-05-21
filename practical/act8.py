# import numpy as np
# import pandas as pd
# data =np.array(['g','r','e','e','n','l','e','a','v','e','s'])

# #creating series of an array
# s=pd.Series(data)
# print(s)

# # accessing the elements through index number(slicing) in fixed size data
# print(s[:5])

# #  in fixed size data
# sd=pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20])
# # accessing a element using index element
# print(sd[13])





# # making data frames
# ps=pd.read_csv("data1.csv")
# se=pd.Series(ps['Duration'])
# data=se.head(10)
# print(data)

# # Indexing a Series using .loc[] :
# print(data.loc[3:6])

# # Indexing a Series using .iloc[] :
# print(data.iloc[3:6])





# # Binary Operation on Series
# data=pd.Series([2,4,6,8,10],index=['a','b','c','d','e'])
# data1=pd.Series([3,5,7,9,1],index=['a','b','d','e','f'])
# print(data,'\n\n' ,data1)

# # adding/sutracting  the seres
# print(data.add(data1,fill_value=0))
# print(data.subtract(data1,fill_value=0))




# # Conversion Operation on Series-- to convert a datatype of series
# ps.dropna(inplace=True)
# before=ps.dtypes
# ps['Duration']=ps['Duration'].astype(str)
# ps['Calorie_Burnage']=ps['Calorie_Burnage'].astype(str)
# after=ps.dtypes
# print('BEFORE CHANGING THE DATA TYPE "\n"',before,"\n")
# print('AFTER CHANGING THE DATA TYPE "\n"',after,"\n")



# # a series into list
# import re                     #regex module      
# ps1=pd.read_csv("data.csv")
         
# mp_before=type(ps1['Gender'])
# maxp_list=ps1['Gender'].tolist()
# mp_after=type(maxp_list)
# print("Data type before conversion ={}\n Data type after conversion={}".format(mp_before,mp_after))
# print(maxp_list)

# # creating a pandas DATAframe -- using list
# s=['green',' leaves', 'gets',' golden',' after ','few',' days',' when',' trees' ,'shed',' their ','leaves']
# df=pd.DataFrame(s)
# print(df)






import numpy as np
import pandas as pd 
# data=pd.read_csv("data.csv")
# # grouping=np.groupby(["Status","gender"])
# # print(grouping)

# df1=pd.DataFrame({'A':['A1','A2','A3','A4'],'B':['B1','B2','B3','B4']})
# print('df1:\n', df1)
# df2=pd.DataFrame({'C':['C1','C2','C3','C4'],'D':['D1','D2','D3','D4']})
# print('df2:\n', df2)
# print('After concatinating')
# print(pd.concat([df1,df2],axis=1))

# data1={'Name':['Ajeet','Mohit',"Rahul","Raju"],'Age':[23,25,23,22]}
# data2={'Address':['Bihar','Jhansi','Nepal','Odisha'],'Qualification':['B.sc','b.a.','ITI','12th']}
# df=pd.DataFrame(data1,index=['k1','k2','k3','k4'])
# df1=pd.DataFrame(data2,index=['k1','k2','k3','k4'])
# print(df , "\n\n" ,df1)
# print(pd.concat([df,df1],axis=1))





# students= [['Himanshu',800],['Keerti',900],['Vikram',850],['RAKESH',980]]
# data=pd.DataFrame(students,columns= ['Students Names','Students Marks'])
# DATA1=data.assign(Percentage=lambda x:(x['Students Marks']/1000*100))
# print(DATA1)

student=[['Himanshu',70,80,90],['Keerti',75,85,95],['Vikram',72,82,92],['Rakesh',20,30,40]]
data1=pd.DataFrame(student,columns= ['Student Names','Maths','Science','Computer'])
DATA2=data1.assign(Marks_Obtained=lambda x:(x['Maths']+x['Science']+x['Computer']))
print(DATA2)

 
# df=pd.DataFrame({
#     'ID':[1,2,3,4,5],
#     'Names':["Rahul",'Prinshi','vikas',"Madan","Rajeev"],
#     'Age':[21,22,23,24,23],
#     'Monthly_income':[3300,2300,3400,1400,1700]})
# df['Monthly_income']=df.apply(lambda x:x['Monthly_income']+200,axis=1)
# print(df)